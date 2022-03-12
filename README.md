# Optimización II (primavera 2022)
## Repo con ejercicios de la clase y algunas prácticas del curso.

En este repositorio se harán pruebas de los ejercicios que se estén desarrollando durante el curso de Optimización II 2022

1) La primera Prueba que se hace es para comprobar la funcionalidad de GitHub Actions para hacer un docker file y subirlo a docker hub, con mi cuneta y usuario (de acuerdo con las notas del curso)


## Sobre BINDER

1. Crear el archivo de **requirements.txt**. Con [_watermark_](https://github.com/rasbt/watermark) se pueden obtener las versiones de las librerías deseadas
2. Crear el notebook que se quiera lanzar con el boton de Binder
3. Entrar a este [link](https://mybinder.org/) para generar el vínculo que correrá el _launcher_ de Binder

Ejemplo de [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/urieluard/opt_2022/main?labpath=final.ipynb)

Nota: Para editar los botones de Binder ver [aquí](https://mybinder.readthedocs.io/en/latest/howto/badges.html)

### Para crear un paquete y lanzarlo con Binder

Si se desea crear un paquete nuevo (no de las librerías estandar de python), seguir estas [instrucciones](https://github.com/binder-examples/setup.py/blob/master/example_notebook/import_mypackage.ipynb)

Hay que configurar la estructura de carpetas con los módulos y funciones que contenga el paquete o librería implementada ([ver aquí](https://www.tutorialsteacher.com/python/python-package))
