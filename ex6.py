import subprocess

def pex6():
    try:
        subprocess.run(["python3", "django/nouprojecte/manage.py", "runserver", "8082"], check=True)
    except subprocess.CalledProcessError as e:
        print("error al imiciar el servidor Django: ", e)