# mydjango

From YouTube course: [Django For Everybody](https://www.youtube.com/watch?v=o0XbHvKxw7Y)

## Running Locally

Once you have Django installed on your local code editor (e.g. VS Code), deploy the project by going into the folder and starting the server:

```
cd mydjango
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

And visit `http://127.0.0.1:8000/`.

If the website return error with message (`Invalid HTTP_HOST header`):

(/mydjango/mydjango/settings.py)
```
ALLOWED_HOSTS = ['127.0.0.1']
```

## Running on PythonAnywhere

Go to PythonAnywhere Files:

(/mydjango/mydjango/settings.py)
```
ALLOWED_HOSTS = ['<username>.pythonanywhere.com']
```

Go to PythonAnywhere Web, update the config files to connect `<username>.pythonanywhere.com` with your project folder:

```
Source code: /home/<username>/mydjango
Working Directory: /home/<username>/mydjango
```

## Getting Started (VS Code)
```
$ pip install django
$ django-admin startproject dj4e-samples
$ cd dj4e-samples
$ django-admin startapp autos
```

(mydjango/settings.py)

```
ALLOWED_HOSTS = ['yuncheng.pythonanywhere.com']
INSTALLED_APPS = [
	  ...
	  'autos.apps.AutosConfig', 
]
```
