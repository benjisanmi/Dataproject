# ===============================================================
# ANÁLISIS ESTADÍSTICO DEL CONSUMO DE ALCOHOL EN EE.UU.
# ===============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import statsmodels.api as sm

# ---------------------------------------------------------------
# 1. CARGA DE DATOS
# ---------------------------------------------------------------

df = pd.read_csv("clean_data.csv")

print("\nDataset cargado correctamente. Filas:", len(df))


# ---------------------------------------------------------------
# 2. REGRESIÓN LINEAL TEMPORAL
# ---------------------------------------------------------------

def regression_trend(df, col_target):
    print(f"\n=== REGRESIÓN LINEAL TEMPORAL: {col_target} ===")

    # Media nacional por año
    tmp = df.groupby("Year", as_index=False)[col_target].mean()

    X = sm.add_constant(tmp["Year"])
    y = tmp[col_target]

    model = sm.OLS(y, X).fit()
    print(model.summary())

    # Gráfico
    plt.figure(figsize=(8, 4))
    sns.regplot(x="Year", y=col_target, data=tmp, ci=95, scatter_kws={"s": 40})
    plt.title(f"Tendencia temporal de {col_target}")
    plt.tight_layout()
    plt.show()

    return model


# Ejecutar regresión para el consumo total
regression_trend(df, "Ethanol_All_Drinks_Gallons_Per_Capita")


# ---------------------------------------------------------------
# 3. ANOVA POR DÉCADAS
# ---------------------------------------------------------------

def add_decade(df):
    df["Decade"] = (df["Year"] // 10) * 10
    return df

def anova_decades(df, col_target):
    print(f"\n=== ANOVA POR DÉCADAS: {col_target} ===")

    df = add_decade(df)
    groups = [g[col_target].values for _, g in df.groupby("Decade")]

    f_stat, p_val = stats.f_oneway(*groups)

    print(f"F = {f_stat:.4f} | p-value = {p_val:.6f}")

    # Gráfico
    plt.figure(figsize=(8, 4))
    sns.boxplot(x="Decade", y=col_target, data=df)
    plt.title(f"Distribución por décadas de {col_target}")
    plt.tight_layout()
    plt.show()

    return f_stat, p_val


anova_decades(df, "Ethanol_All_Drinks_Gallons_Per_Capita")


# ---------------------------------------------------------------
# 4. MATRIZ DE CORRELACIONES
# ---------------------------------------------------------------

def correlation_matrix(df):
    print("\n=== MATRIZ DE CORRELACIONES ===")

    cols = [
        "Ethanol_Beer_Gallons_Per_Capita",
        "Ethanol_Wine_Gallons_Per_Capita",
        "Ethanol_Spirit_Gallons_Per_Capita",
        "Ethanol_All_Drinks_Gallons_Per_Capita"
    ]

    corr = df[cols].corr(method="pearson")
    print(corr)

    plt.figure(figsize=(6, 4))
    sns.heatmap(corr, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
    plt.title("Matriz de correlaciones entre tipos de consumo")
    plt.tight_layout()
    plt.show()

    return corr


correlation_matrix(df)


# ---------------------------------------------------------------
# 5. INTERVALOS DE CONFIANZA
# ---------------------------------------------------------------

def confidence_interval(df, col_target, confidence=0.95):
    print(f"\n=== INTERVALO DE CONFIANZA: {col_target} ===")

    data = df[col_target].dropna()
    mean = np.mean(data)
    sem = stats.sem(data)
    margin = sem * stats.t.ppf((1 + confidence) / 2, len(data) - 1)

    print(f"Media = {mean:.4f}")
    print(f"{confidence*100:.0f}% CI = [{mean - margin:.4f}, {mean + margin:.4f}]")

    return mean, mean - margin, mean + margin


confidence_interval(df, "Ethanol_All_Drinks_Gallons_Per_Capita")


# ---------------------------------------------------------------
# FIN DEL ANÁLISIS
# ---------------------------------------------------------------

print("\nAnálisis estadístico completado correctamente.")
