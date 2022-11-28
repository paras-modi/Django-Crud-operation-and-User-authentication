from django.urls import path

from Employee import views
#from Employeemanagement import Employee.views

urlpatterns = [
    path('', views.Homepage, name="home"),
    path('register', views.Register, name="register"),
    path('login', views.Login, name="login"),
    path('show', views.Login, name="showing"),
    path('add', views.Add, name="add"),
    path('attach', views.Attach),
    path('edit/<int:id>', views.Edit),
    path('logout',views.log_out,name="logout"),
    path('delete/<int:id>', views.delete),
]