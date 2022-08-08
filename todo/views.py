from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import DetailView, ListView
from .models import Todo

# Create your views here.
# ---------------------------------------------------------------------------- #
#                             FUnctions based views                            #
# ---------------------------------------------------------------------------- #

# ------------------------------- create a todo ------------------------------ #
def create_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        memo = request.POST.get('memo')
        Todo.objects.create(title=title, memo=memo)
        return HttpResponseRedirect('/')
    return render(request, 'todo/todo_list.html')

# --------------------------- check/uncheck a todo complete -------------------------- #
def check_todo(request, pk):
    if request.method == 'POST':
        todo = Todo.objects.get(pk=pk)
        todo.is_completed = True
        todo.save()
        return HttpResponseRedirect('/')
    return render(request, 'todo/todo_list.html')

def uncheck_todo(request, pk):
    if request.method == 'POST':
        todo = Todo.objects.get(pk=pk)
        todo.is_completed = False
        todo.save()
        return HttpResponseRedirect('/completed/')


# ---------------------------------------------------------------------------- #
#                               class based views                              #
# ---------------------------------------------------------------------------- #

# --------------------------------- todo list view (Not done yet) -------------------------------- #
class TodoList(ListView):
    model = Todo
    template_name = 'todo/todolist.html'
    context_object_name = 'todo_list'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todo_list'] = Todo.objects.all().filter(is_completed=False)
        return context
    
# --------------------------- todo list view (done) -------------------------- #
class TodoListDone(ListView):
    model = Todo
    template_name = 'todo/todolist_done.html'
    context_object_name = 'todo_list'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todo_list_done'] = Todo.objects.all().filter(is_completed=True)
        return context
    
# ----------------------------- todo detail view ----------------------------- #
class TodoDetail(DetailView):
    model = Todo
    template_name = 'todo/tododetail.html'
    context_object_name = 'todo_view'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todo_view'] = Todo.objects.get(id=self.kwargs['pk'])
        return context