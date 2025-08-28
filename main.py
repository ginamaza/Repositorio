import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 
nombreArchivo = "fraud_credit_card.csv"

def leerDataset(nombreArchivo): 
    return pd.read_csv(nombreArchivo)

##FUNCION 1##

def resumen_general(db): 
    print("Dimensiones del dataset:", db.shape) 
    print("\nTipos de datos:\n", db.dtypes) 
    print("\nValores nulos por columna:\n", db.isnull().sum()) 
    print("\nPrimeras filas:\n", db.head()) 
    print("\nÚltimas filas:\n", db.tail()) 


## FUNCION 2 ##
def estadisticas_descriptivas(db):
    print("\nEstadísticas descriptivas:\n", db.describe(include='all'))

## FUNCION 5 ##
def correlaciones(db): 
    corr_matrix = db.corr(numeric_only=True) 
    print("\nMatriz de correlación:\n", corr_matrix) 
    plt.figure(figsize=(7, 5)) 
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f") 
    plt.title('Heatmap de correlaciones') 
    plt.show()


## funcion 4 ##
def valores_faltantes(db):
    print("\nValores faltantes por columna:\n", db.isnull().sum())
    plt.figure(figsize=(7, 5))
    sns.heatmap(db.isnull(), cbar=False, cmap='viridis')
    plt.title('Mapa de calor de valores nulos')
    plt.show()


