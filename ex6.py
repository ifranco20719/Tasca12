import subprocess # Importa el módulo subprocess para ejecutar comandos del sistema.

def pex6():
    try: 
        # Intenta ejecutar un comando de shell para iniciar el servidor Django en el puerto 8082.
        subprocess.run(["python3", "django/nouprojecte/manage.py", "runserver", "8082"], check=True)
    except subprocess.CalledProcessError as e:
        # Si ocurre un error al ejecutar el comando, imprime un mensaje de error.
        print("error al imiciar el servidor Django: ", e)