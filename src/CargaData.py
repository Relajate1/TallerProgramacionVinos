import pandas as pd
from sklearn.datasets import load_wine

def cargar_datos():

    vino = load_wine()
    df = pd.DataFrame(vino.data, columns=vino.feature_names)
    df['target'] = vino.target

    # Exploración
    print("Primeros registros:\n", df.head())
    print("\nVariables:\n", df.columns)
    print("\nClases:", vino.target_names)
    print("\nCantidad de datos:", df.shape)
    print("\nEstadísticas:\n", df.describe())

    # Separación
    X = df.drop('target', axis=1)
    y = df['target']

    return X, y, vino