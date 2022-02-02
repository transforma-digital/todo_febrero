from datetime import datetime

from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from . import forms, models


def TodoNew(request):
  todoNewForm = forms.TodoNewForm()
  
  context = {
    'form_new': todoNewForm
  }
  
  return render(request, 'todo-new.html', context)


####################################################

def TodoCreated(request):
  todoNewForm = forms.TodoNewForm(request.POST)

  title = todoNewForm['title'].value()
  created = datetime.now()

  context = {
    'title': title
  }

  todo = models.Todo(title=title, created=created, checked=False)
  todo.save()

  return render(request, 'todo-created.html', context)

####################################################

class TodoListView(TemplateView):
  template_name = 'todo-list.html'

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)

      todos = models.Todo.objects.all()
      context['todos'] = todos

      return context


####################################################

class TodoSingleView(FormView):
  template_name = 'todo-single.html'
  form_class = forms.TodoNewForm
  success_url = '/todo/single'

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['todos'] = models.Todo.objects.all()
      return context

  def form_valid(self, form):
      title = form['title'].value()
      created = datetime.now()

      todo = models.Todo(title=title, created=created, checked=False)
      todo.save()

      return self.render_to_response(self.get_context_data())


def TodoDeleteView(request, todo_id):
    todo = models.Todo.objects.filter(id=todo_id)
    todo.delete()
    return redirect('/todo/single/')

def TodoDeleteViewPost(request):
    print(request.POST)
    return redirect('/todo/single/')


def TodoUpdateChecks(request):
    pairs = request.POST.getlist('todo_check')
    
    for pair in pairs:
      tid, val = pair.split(':')

      tid = int(tid)
      val = val == 'True'

      todo = models.Todo.objects.get(id=tid)
      todo.checked = val
      todo.save()
     
    return redirect('/todo/single/')