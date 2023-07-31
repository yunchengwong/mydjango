# autos

Simple CRUD Application

## Login in Django

(mydjango/urls.py)

```
from django.urls import include, path

urlpatterns = [
  path('accounts/', include('django.contrib.auth.urls')),
]
```

(autos/templates/registration/login.html)

```
{% if form.errors %}
  <p>Your username and password didn't match. Please try again.</p>
{% endif %}

<form method="post" action="{% url 'login' %}">
  {% csrf_token %}
  {{ form.as_p }}
  <input type="submit" value="Login">
  <input type="hidden" name="next" value="{{ next }}"> 
</form>
```

## Model in Autos

(mydjango/autos/models.py)

```
from django.db import models
from django.core import validators

class Auto(models.Model):
    name = models.CharField(max_length=200, validators=[validators.MinValueValidator(2,"Make must be greater than 1 character")])
    mileage = models.PositiveIntegerField()
    comments = models.CharField(max_length=300)
    make = models.ForeignKey('Make', on_delete=models.CASCADE, null=False)
    
    def __str__(self):
        return self.name
    
class Make(models.Model):
    name = models.CharField(max_length=200, validators=[validators.MinValueValidator(2,"Make must be greater than 1 character")], help_text="Enter a Auto manufacturer")
    
    def __str__(self):
        return self.name
```

## R for Read

#### view autos

(mydjango/autos/urls.py)

```
urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
]
```

(mydjango/autos/views.py)

```
class MainView(LoginRequiredMixin, View):
  def get(self, request):
    auto_list = Auto.objects.all()
    make_count = Make.objects.count()
    context = {'auto_list': auto_list, 'make_count': make_count}
    return render(request, 'autos/auto_list.html', context)
```

(mydjango/autos/templates/autos/auto_list.html)

`auto_list`

```
{% if auto_list %}
  <ul>
  {% for auto in auto_list %}
    <li>
      {{ auto.name }} ({{ auto.make }})
      (
        <a href="{% url 'autos:autoUpdate' auto.id %}">
          Update
        </a>
        |
        <a href="{% url 'autos:autoDelete' auto.id %}">
          Delete
        </a>
      )
      <br />
      {{ auto.comments }} ({{ auto.mileage }} miles)
    </li>
  {% endfor %}
  </ul>
{% else %}
  <p>
    There are no autos in the library.
  </p>
{% endif %}
```

`make_count`

```
{% if make_count > 0 %}
  <a href="{% url 'autos:autoCreate' %}">
    Add an auto
  </a>
{% else %}
  <p>
    Please add a make before you add an auto.
  </p>
{% endif %}

<p>
  <a href="{% url 'autos:make' %}">
    View makes
  </a>

  ({{ make_count }}) | 

  <a href="{% url 'autos:makeCreate' %}">
    Add a make
  </a>
</p>
```

#### view makes

(mydjango/autos/urls.py)

```
urlpatterns = [
    path('lookup/', views.MakeView.as_view(), name='make'),
]
```

(mydjango/autos/views.py)

```
class MakeView(LoginRequiredMixin, View):
  def get(self, request):
    make_list = Make.objects.all()
    context = {'make_list': make_list}
    return render(request, 'autos/make_list.html', context)
```

(mydjango/autos/templates/autos/make_list.html)

`make_list`

```
{% if make_list %}
  <ul>
  {% for make in make_list %}
    <li>
      {{ make.name }}
      (
        <a href="{% url 'autos:makeUpdate' make.id %}">
          Update
        </a>
        |
        <a href="{% url 'autos:makeDelete' make.id %}">
          Delete
        </a>
      )
    </li>
  {% endfor %}
  </ul>
{% else %}
  <p>
    There are no makes in the library.
  </p>
{% endif %}
```

## C for Create

#### Django Model Form

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

Execute form validation.

```
form.is_valid()
```

#### ModelForm for autos

(mydjango/autos/forms.py)

```
from django.forms import ModelForm
from .models import Make
  
class MakeForm(ModelForm):
    class Meta:
        model = Make
        fields = '__all__'
```

#### add a make

(mydjango/autos/urls.py)

```
urlpatterns = [
    path('lookup/create/', views.MakeCreate.as_view(), name='makeCreate'),
]
```

(mydjango/autos/views.py)

```
from .forms import MakeForm

class MakeCreate(LoginRequiredMixin, View):
  def get(self, request):
    form = MakeForm()
    context = {'form': form}
    return render(request, 'autos/make_form.html', context)
  def post(self, request):
    form = MakeForm(request.POST)
    if not form.is_valid():
      context = {'form': form}
      return render(request, 'autos/make_form.html', context)
    form.save()
    return redirect(reverse_lazy('autos:main'))
```

(mydjango/autos/templates/autos/make_form.html)

`form`

```
<form method="post">
  {% csrf_token %}
  <table>
    {{ form.as_table }}
  </table>
  <input type="submit" value="POST">
  <input type="submit" onClick="window.location='{% url 'autos:main' %}'; return false;" value="Cancel">
</form>
```

## U for Update

#### update make

(mydjango/autos/urls.py)

```
urlpatterns = [
    path('lookup/<int:pk>/update/', views.MakeUpdate.as_view(), name='makeUpdate'),
]
```

(mydjango/autos/views.py)

```
class MakeUpdate(LoginRequiredMixin, View):
  model = Make
  success_url = reverse_lazy('autos:main')
  template = 'autos/make_form.html'
  
  def get(self, request, pk):
    make = get_object_or_404(self.model, pk=pk)
    form = MakeForm(instance=make)
    context = {'form': form}
    return render(request, self.template, context)
  def post(self, request, pk):
    make = get_object_or_404(self.model, pk=pk)
    form = MakeForm(request.POST, instance=make)
    if not form.is_valid():
      context = {'form': form}
      return render(request, self.template, context)
    form.save()
    return redirect(self.success_url)
```

## D for Delete

#### update delete

(mydjango/autos/views.py)

```
class MakeDelete(LoginRequiredMixin, View):
  model = Make
  success_url = reverse_lazy('autos:main')
  template = 'autos/make_confirm_delete.html'
  
  def get(self, request, pk):
    make = get_object_or_404(self.model, pk=pk)
    form = MakeForm(instance=make)
    context = {'make': make}
    return render(request, self.template, context)
  def post(self, request, pk):
    make = get_object_or_404(self.model, pk=pk)
    make.delete()
    return redirect(self.success_url)
```

(mydjango/autos/templates/autos/make_confirm_delete.html)

`make`

```
<p>
  Are you sure you want to delete the make: {{ make }}?
</p>

<form method="post">
  {% csrf_token %}
  <input type="submit" value="DELETE">
  <input type="submit" onClick="window.location='{% url 'autos:main' %}'; return false;" value="Cancel">
</form>
```

## Django Generic View

#### add an auto (C)

(mydjango/autos/urls.py)

```
urlpatterns = [
    path('main/create/', views.AutoCreateView.as_view(), name='autoCreate'),
]
```

(mydjango/autos/views.py)

```
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class AutoCreateView(CreateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:main')
```

(mydjango/autos/forms.py)

```
// intentionally left blank
```

(mydjango/autos/templates/auto_form.html)

```
<form method="post">
  {% csrf_token %}
  <table>
    {{ form.as_table }}
  </table>
  <input type="submit" value="POST">
  <input type="submit" onClick="window.location='{% url 'autos:main' %}'; return false;" value="Cancel">
</form>
```

#### update auto (U)

(mydjango/autos/views.py): `UpdateView`

(mydjango/autos/templates/): `auto_form.html`

#### delete auto (D)

(mydjango/autos/views.py): `DeleteView`

(mydjango/autos/templates/): `auto_confirm_delete.html`

## Reference

#### `window.location`

redirect in JS: 

```
window.location='<url>';
```

(https://stackoverflow.com/questions/9903659/difference-between-window-location-and-location-href)

window.location == window.location.href

(https://www.geeksforgeeks.org/difference-between-window-location-href-window-location-replace-and-window-location-assign-in-javascript/)

window.location.replace delete current page from session history, while window.location don't

#### `re-run makemigration`

```
rm */migrations/00*
rm db.sqlite3
pyclean
```

#### `'autos' is not a registered namespace`

(autos/urls.py)

```
app_name = 'autos'
```
