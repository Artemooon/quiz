from django.urls import path
from . import views

app_name = 'game'

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('quiz/', views.QuizListView.as_view(), name='quiz_list'),
    path('quiz/<int:pk>', views.QuizDetailView.as_view(), name='quiz_detail'),
]