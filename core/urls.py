from django.urls import path
from .views import *

urlpatterns = [
    #--------------------------------------------------------------------------------------------------------------------#
    # path('user-create/', user_Create, name='user-create'),
    # path('user-login/', user_login, name='user-login'),
    # path('user-logout/', user_logout, name='user-logout'),
    # #--------------------------------------------------------------------------------------------------------------------#
    path('login/', admin_login, name='admin-login'),
    # path('admin-create/', admin_Create, name='admin-create'),
    path("user/", UsersView.as_view(), name="dashboard-user"),
    path('admin-logout/', admin_logout, name='admin-logout'),
    #--------------------------------------------------------------------------------------------------------------------#
]

