from django.urls import path
from . import views

app_name='classroom'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('thank-you/', views.ThankYouView.as_view(), name='thank-you'),
    path('contact/', views.ContactFormView.as_view(), name='contact'),
    path('create-teacher/', views.TeacherCreateView.as_view(), name='create-teacher'),
    path('list-teacher/', views.TeacherListView.as_view(), name='list-teacher'),
]