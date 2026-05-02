import matplotlib.pyplot as plt
from sklearn import tree
import os

def graficar_arbol(modelo, feature_names, class_names):
    
    carpeta = "grafico"
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)

    plt.figure(figsize=(12, 8))

    tree.plot_tree(
        modelo,
        feature_names=feature_names,
        class_names=class_names,
        filled=True,
        rounded=True,
        fontsize=8
    )

    plt.title("Árbol de decisión - Clasificación de vinos")

    ruta = os.path.join(carpeta, "arbol_vinos.png")

    plt.savefig(ruta, dpi=300, bbox_inches='tight')

    print(f"Gráfico guardado en: {ruta}")

    plt.show()
    