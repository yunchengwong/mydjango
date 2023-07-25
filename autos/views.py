from django.shortcuts import render, redirect, get_object_or_404

from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Auto, Make

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .forms import MakeForm

# Create your views here.

class MainView(LoginRequiredMixin, View):
  def get(self, request):
    auto_list = Auto.objects.all()
    make_count = Make.objects.count()
    context = {'auto_list': auto_list, 'make_count': make_count}
    return render(request, 'autos/auto_list.html', context)

class AutoCreateView(CreateView): # use auto_form.html as template by default
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:main')
  
class AutoUpdateView(UpdateView): 
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:main')

class AutoDeleteView(DeleteView): 
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
  
class MakeDelete(LoginRequiredMixin, View):
  model = Make
  success_url = reverse_lazy('autos:main')
  template = 'autos/make_confirm_delete.html'
  
  def get(self, request, pk):
    make = get_object_or_404(self.model, pk=pk)
    form = MakeForm(instance=make)
    context = {'form': form, 'make': make}
    return render(request, self.template, context)
  def post(self, request, pk):
    make = get_object_or_404(self.model, pk=pk)
    make.delete()
    return redirect(self.success_url)
