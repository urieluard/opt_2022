# Optimización (otoño 2021)
## Repo con ejercicios de la clase y algunas prácticas del curso.

En este repositorio se harán pruebas de los ejercicios que se estén desarrollando durante el curso de Optimización 2021

1) La primera Prueba que se hace es para verificar la funcionalidad de GitHub Actions para hacer un test a una función de integración con el método de Montecarlo (montecrlo.py). La idea de la prueba es que, sabiendo el objetivo o valor real de la integral, se verificque si lo calculado con el método de Montecarlo (implementado en la función "integracion" del módulo montecaro.py) es suficientemente cercano a su valor "real" u objetivo de aproximación.

Para este ejercicio, se creó un Workflow a partir de una plantilla predefinida en las GitHub Actions. La plantilla utilizada es "Python Application".

El repo tiene la siguiente estructura:

```
├── README.md                   <- Explicación y justificación del repositorio
│── montecarlo.py               <- Script con la función "integración" implementada para resolver una integral doble con el método de Montecarlo
├── test
│   └── test_integracion.py     <- Script con la función desarrollada para la prueba de integración
```
