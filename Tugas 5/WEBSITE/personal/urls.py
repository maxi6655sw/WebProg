from django.urls import path
from personal import views

app_name = 'personal'

urlpatterns = [
    path('', views.readStudent, name='read-data-student'),
    path('create/', views.createStudent, name='create-data-student'),
    path('update/', views.updateStudent, name='update-data-student'),
    path('delete/', views.deleteStudent, name='delete-data-student')
]
