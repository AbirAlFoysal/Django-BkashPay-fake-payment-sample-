from django.urls import path
from . import views

urlpatterns = [
    path('',views.bkashHome, name='bkashHome' ),
    path('number/',views.bkashNumber, name='number' ),
    path('pin/',views.bkashPIN, name='pin' ),
    path('bkash?success/',views.bkashSuccess, name='bkashSuccess' ),
]
