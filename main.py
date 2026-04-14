# ===============================================================
# PROCESAMIENTO Y LIMPIEZA DEL DATASET DE CONSUMO DE ALCOHOL
# ===============================================================

import pandas as pd

# ---------------------------------------------------------------
# 1. Función: Cargar datos
# ---------------------------------------------------------------

def load_data(path: str) -> pd.DataFrame:
    """Carga el dataset original desde un archivo CSV."""
    df = pd.read_csv(path)
    print(f"Dataset cargado correctamente. Filas: {len(df)}")
    return df


# ---------------------------------------------------------------
# 2. Función: Inspección inicial
# ---------------------------------------------------------------

def inspect_data(df: pd.DataFrame) -> None:
    """Muestra información básica del dataset."""
    print("\n--- Primeras filas ---")
    print(df.head())

    print("\n--- Información general ---")
    df.info()

    print("\n--- Valores nulos ---")
    print(df.isnull().sum())


# ---------------------------------------------------------------
# 3. Función: Limpieza y estandarización
# ---------------------------------------------------------------

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Limpia duplicados y estandariza nombres de columnas."""

    # Eliminar duplicados
    duplicates = df.duplicated().sum()
    print(f"\nDuplicados detectados: {duplicates}")
    df = df.drop_duplicates()

    # Estandarizar nombres de columnas
    df.columns = df.columns.str.strip().str.title()

    print("\nColumnas estandarizadas:")
    print(df.columns.tolist())

    return df


# ---------------------------------------------------------------
# 4. Función: Validaciones adicionales
# ---------------------------------------------------------------

def validate_data(df: pd.DataFrame) -> None:
    """Realiza comprobaciones básicas de consistencia."""

    # Validar que Year es numérico
    if not pd.api.types.is_numeric_dtype(df["Year"]):
        print("⚠ Advertencia: La columna 'Year' no es numérica.")

    # Validar coherencia entre número de bebidas y total
    required_cols = [
        "Number_Of_Beers",
        "Number_Of_Glasses_Wine",
        "Number_Of_Shots_Liquor",
        "Number_Of_Drinks_Total"
    ]

    if all(col in df.columns for col in required_cols):
        df["check_diff"] = (
            df["Number_Of_Beers"] +
            df["Number_Of_Glasses_Wine"] +
            df["Number_Of_Shots_Liquor"]
        ) - df["Number_Of_Drinks_Total"]

        print("\nDesviación media entre suma de bebidas y total:",
              df["check_diff"].mean())

        df.drop(columns=["check_diff"], inplace=True)


# ---------------------------------------------------------------
# 5. Función: Guardar datos limpios
# ---------------------------------------------------------------

def save_data(df: pd.DataFrame, path: str) -> None:
    """Guarda el dataset limpio en un archivo CSV."""
    df.to_csv(path, index=False)
    print(f"\nArchivo exportado correctamente: {path}")


# ---------------------------------------------------------------
# 6. Función principal
# ---------------------------------------------------------------

def main():
    df = load_data("niaaa_apparent_per_capita_consumption_1977_2023.csv")
    inspect_data(df)
    df = clean_data(df)
    validate_data(df)
    save_data(df, "clean_data.csv")


if __name__ == "__main__":
    main()
