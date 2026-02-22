# ===============================================================
# FASE 1: Importar librerías y carga de datos
# ===============================================================

# --- Importar librerías necesarias ---
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configuraciones generales de visualización
pd.set_option('display.max_columns', None)
sns.set(style="whitegrid", palette="pastel")

# Cargar dataset principal
df = pd.read_csv('niaaa_apparent_per_capita_consumption_1977_2023.csv', sep=',')


# ===============================================================
# fASE 2: INSPECCIÓN INICIAL
# ===============================================================

# Mostrar las primeras filas del dataset
print(df.head())

# Tipos de datos y valores nulos
print("\n--- Información general ---")
df.info()
print("\n--- Valores nulos ---")
print(df.isnull().sum())

# ===============================================================
# fase 3: DETECCIÓN DE DUPLICADOS Y CONSISTENCIA
# ===============================================================

# Duplicados
print(f"\nDuplicados en dataset: {df.duplicated().sum()}")

# Eliminar duplicados si existen
df.drop_duplicates(inplace=True)


# ===============================================================
# FASE 4: LIMPIEZA Y ESTANDARIZACIÓN DE COLUMNAS
# ===============================================================

# Convertir nombres de columnas a minúsculas y reemplazar espacios por "_"
df.columns = df.columns.str.lower().str.title()

# Comprobamos columnas clave
print("\nColumnas:", df.columns.tolist())


# ===============================================================
# fase 5: EXPORTAR DATOS LIMPIOS
# ===============================================================

# Guardar versión limpia para uso posterior
df.to_csv('clean_data.csv', index=False)
print("\n clean_data.csv")

