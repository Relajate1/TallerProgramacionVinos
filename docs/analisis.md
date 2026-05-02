# Análisis del modelo de clasificación de vinos

## a. Accuracy del modelo
El modelo obtuvo un accuracy alto (aproximadamente cercano a 0.9), lo que indica un buen desempeño en la clasificación.

## b. Variable raíz del árbol
La variable que aparece en la raíz del árbol es **color_intensity**, lo que indica que es la más importante para la primera división de los datos.

## c. ¿El modelo parece confiable?
Sí, el modelo parece confiable, ya que logra una buena precisión y separa correctamente las clases en varios nodos.

## d. ¿Overfitting o underfitting?
No se observa overfitting significativo, ya que se limitó la profundidad del árbol (max_depth=3), lo que permite una mejor generalización.

## e. Variables más relevantes
Las variables más importantes observadas en el árbol son:
- color_intensity
- proline
- flavanoids

Estas aparecen en los primeros niveles del árbol, por lo que influyen directamente en las decisiones.