from django.urls import path
from . import views

app_name = 'car'

urlpatterns = [

    path('rental-review/',views.rental_review,name='rental-review'),
    path('thank-you/',views.thank_you,name='thank-you'),
]