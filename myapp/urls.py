from django.urls import path

from myapp import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('getAnswer/', views.get_answer, name='answer')
]