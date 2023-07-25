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

## Notes for Myself

#### Django VSCode Setup

```
$ pip install django
$ django-admin startproject dj4e-samples
$ cd dj4e-samples
$ django-admin startapp autos
```

#### Django App Config

```
ALLOWED_HOSTS = ['yuncheng.pythonanywhere.com']
INSTALLED_APPS = [
	  ...
	  'autos.apps.AutosConfig', 
]
```

#### Overwrite Django Login View

create login page with url `/registration/login.html`

#### Steps for Writing a Django App

1. app/templates/layout.html
2. app/urls.py
3. app/models.py
4. app/forms.py
5. app/views.py
6. app/templates/app/*.html

#### Django Model Form

(https://docs.djangoproject.com/en/4.2/topics/forms/modelforms/)

Creating a form to add a make.
```
form = MakeForm()
```
Create a form instance from POST data.
```
form = MakeForm(request.POST)
form.save()
 ```
Creating a form to change an existing make.
```
make = Make.objects.get(pk=1)
form = MakeForm(instance=make)
```
Create a form to edit an existing Make, but use POST data to populate the form.
```
make = Make.objects.get(pk=1)
form = MakeForm(request.POST, instance=make)
form.save()
```
