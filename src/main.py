from CargaData import cargar_datos
from modelo import entrenar_modelo
from evaluacion import evaluar_modelo
from vizualizacion import graficar_arbol

def main():
    
    X, y, vino = cargar_datos()

    modelo, X_test, y_test = entrenar_modelo(X, y)

    acc, y_pred = evaluar_modelo(modelo, X_test, y_test)

    graficar_arbol(modelo, X.columns, vino.target_names)

main()
