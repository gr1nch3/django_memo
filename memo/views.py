
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.views.generic import DetailView, ListView
from .models import Memo
from .forms import UserCreation
from django.http import JsonResponse
from django.contrib.auth import login

# Create your views here.
# ---------------------------------------------------------------------------- #
#                             Functions based views                            #
# ---------------------------------------------------------------------------- #

# ---------------------------------- sign up --------------------------------- #

def signup(request):
    userform = UserCreation()
    if request.method == 'POST':
        userform = UserCreation(request.POST)
        if userform.is_valid():
            uf = userform.save(commit=False)
            uf.save()

            # Login the user and redirect to the home page
            if uf is not None:
                if uf.is_active:
                    login(request, uf)  # login the user
                    return redirect('memo:memo_list')  # redirect to the home page

        else:
            # used dictionary to know the field and the error
            errors = {}
            # loop through the form fields and add the errors to the dictionary
            for field in userform:
                for error in field.errors:
                    errors[
                        field.name] = error  # add the error to the dictionary as the value and the field name as the key
            return JsonResponse({"status": False, "errors": errors})

    else:
        userform = UserCreation()
    return render(request, 'auth/signup.html', {'form': userform})

# ------------------------------- create a memo ------------------------------ #
def create_memo(request):
    if request.method == 'POST':
        # add login check
        if request.user.is_authenticated:
            title = request.POST.get('title')
            memo = request.POST.get('memo')
            user = request.user
            Memo.objects.create(user=user, title=title, memo=memo)
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/login')
    return render(request, 'memo/memo_list.html')

# --------------------------- check/uncheck a memo complete -------------------------- #
def check_memo(request, pk):
    if request.method == 'POST':
        if request.user.is_authenticated:
            memo = Memo.objects.get(pk=pk)
            memo.is_completed = True
            memo.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/login')
    return render(request, 'memo/memo_list.html')

def uncheck_memo(request, pk):
    if request.method == 'POST':
        if request.user.is_authenticated:
            memo = Memo.objects.get(pk=pk)
            memo.is_completed = False
            memo.save()
            return HttpResponseRedirect('/completed/')
        else:
            return HttpResponseRedirect('/login')


# ---------------------------------------------------------------------------- #
#                               class based views                              #
# ---------------------------------------------------------------------------- #

# --------------------------------- memo list view (Not done yet) -------------------------------- #
class MemoList(LoginRequiredMixin, ListView):
    model = Memo
    template_name = 'memo/memolist.html'
    context_object_name = 'memo_list'
    login_url = '/login'

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)
        context['memo_list'] = Memo.objects.all().filter(is_completed=False).filter(user=user)
        return context

# --------------------------- memo list view (done) -------------------------- #
class MemoListDone(LoginRequiredMixin, ListView):
    model = Memo
    template_name = 'memo/memolist_done.html'
    context_object_name = 'memo_list_done'
    login_url = '/login'

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)
        context['memo_list_done'] = Memo.objects.all().filter(is_completed=True).filter(user=user)
        return context

# ----------------------------- memo detail view ----------------------------- #
class MemoDetail(LoginRequiredMixin, DetailView):
    model = Memo
    template_name = 'memo/memodetail.html'
    context_object_name = 'memo_view'
    login_url = '/login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['memo_view'] = Memo.objects.get(id=self.kwargs['pk'])
        return context