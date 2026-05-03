from django.urls import path
from . import views

urlpatterns = [
    # When someone visits /api/contacts/, trigger the 'all_contacts' view
    path('api/contacts/', views.all_contacts, name='all_contacts'),
]