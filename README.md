# Python with flask

# Crear un entorno virtual con python

1. Utilizaremos en este caso pipenv para este objetivo, en la carpeta de nuestro proyecto corremos el siguiente comando `pipenv install`.
2. Al correr este comando vemos que se crean 2 archivos que son [Pipfile](./Pipfile) y [Pipfile.lock](./Pipfile.lock), estos contienen los requisitos completos de nuestro proyecto y la configuracion de nuestro entorno virtual.
3. Comandos para manejar nuestros entrornos:
    - Sirve para listar todos los entornos virtuales que tenemos `pipenv --venv`.
    - Activar el entorno virtual `pipenv shell`.
    - Instalar paquetes dentro de nuestro entorno `pip install <PAQUETE 1> <PAQUETE 2> <PAQUETE 3>`.
    - Ver todos los paquetes que tenemos instaladas `pipenv graph`.
    - Para salir de nuestro entorno virtual `exit`.
    - Eliminar un entorno virtual `pipenv --rm`.
    - Para instalar todos los paquetes de nuestro proyecto `pipenv install`.
