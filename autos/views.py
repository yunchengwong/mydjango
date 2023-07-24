from django.shortcuts import render

from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Auto, Make

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.

class MainView(LoginRequiredMixin, View):
  def get(self, request):
    auto_list = Auto.objects.all()
    make_count = Make.objects.count()
    context = {'auto_list': auto_list, 'make_count': make_count}
    return render(request, 'autos/auto_list.html', context)

class AutoCreateView(CreateView): # snippet: createview
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:main')
  
class AutoUpdateView(UpdateView): # snippet: updateview
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:main')

class AutoDeleteView(DeleteView): # snippet: deleteview
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:main')
  
class MakeView(LoginRequiredMixin, View):
  def get(self, request):
    make_list = Make.objects.all()
    context = {'make_list': make_list}
    return render(request, 'autos/make_list.html', context)
  
class MakeCreate(LoginRequiredMixin, View):
  def get(self, request):
    context = {'':''}
    return render(request, 'autos/make_form.html', context)
  
class MakeUpdate(LoginRequiredMixin, View):
  def get(self, request):
    context = {'':''}
    return render(request, 'autos/make_form.html', context)
  
class MakeDelete(LoginRequiredMixin, View):
  def get(self, request):
    context = {'':''}
    return render(request, 'autos/make_confirm_delete.html', context)