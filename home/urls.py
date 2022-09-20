from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('training/', views.training, name= 'training'),
    path('register/', views.registerform, name= 'register'),
    path('login/', views.loginform, name= 'account'),
    path('logout/', views.logoutfunc, name= 'logout'),
    path('update/', views.userupdate, name= 'update'),
    path('profile/', views.profile, name= 'profile'),
    path('upchange/', views.userpasswordchange, name= 'upchange'),
    path('enquires/', views.enquires, name= 'enquires'),
    path('allproduct/', views.allproduct, name= 'allproduct'),
    path('pendraw/', views.pendraw, name= 'pendraw'),
    path('giftbox/', views.giftbox, name= 'giftbox'),
    path('greetcard/', views.greetcard, name= 'greetcard'),
    path('picframe/', views.picframe, name= 'picframe'),
    path('searchbar/', views.searchbar, name= 'searchbar'),
    path('prod_det/<str:id>', views.prod_det, name= 'prod_det'),


    path('reset_password/', auth_views.PasswordResetView.as_view(template_name = 'accounts/password_reset.html'), name = 'reset_password'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name = 'accounts/password_reset_sent.html'), name = 'password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'accounts/password_reset_guide.html'), name = 'password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name = 'accounts/password_reset_done.html'), name = 'password_reset_complete'),
]