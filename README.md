# mydjango

## Project Setup

```
pip install django
git clone https://github.com/yunchengwong/mydjango.git
cd mydjango
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

## Running Locally

Once you have Django installed on your local code editor (e.g. Visual Studio Code), deploy the project by going into the folder and starting the server:

```
cd mydjango
python manage.py runserver
```

And visit `http://127.0.0.1:8000/`.

## Running on PythonAnywhere

Once you have run the project setup with PythonAnywhere Console, go to Files, edit `/mydjango/mydjango/settings.py`:

```
ALLOWED_HOSTS = ['<username>.pythonanywhere.com']
```

Go to Web, update the config files to connect <username>.pythonanywhere.com with your project folder:

```
Source code: /home/<username>/mydjango
Working Directory: /home/<username>/mydjango
```
