from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views
urlpatterns=[
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),

    path('password_change/',
         views.MyPasswordChangeView.as_view(),
         # mypasswordchangeview 재정의 함
         name='password_change'),
    path('password_reset/', views.MyPasswordResetView.as_view(), name='password_reset'),
    path('reset/<uid64>/<token>/', views.MyPasswordResetConfirmView.as_view(), name='password_reset'),

]
'''  # success_url을 대체함  
    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(
             template_name='accounts/password_change_done.html'
         ),
         name='password_change_done'),
'''
