from django.urls import path
from django.contrib.auth import views as auth_views
from .views import MemoList, MemoListDone, MemoDetail, create_memo, check_memo, uncheck_memo, signup
app_name = 'memo'

urlpatterns = [
    path('', MemoList.as_view(), name='memo_list'),
    path('completed/' , MemoListDone.as_view(), name='memo_list_done'),
    path('<int:pk>/', MemoDetail.as_view(), name='memo_detail'),
    path('create/', create_memo, name='create_memo'),
    path('check/<int:pk>/', check_memo, name='check_memo'),
    path('uncheck/<int:pk>/', uncheck_memo, name='uncheck_memo'),
    path('signup/', signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(next_page='memo:memo_list'), name='logout'),

]
