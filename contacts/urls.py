from django.urls import path
from . import views

urlpatterns = [
    # Existing JSON API route
    path('api/contacts/', views.all_contacts, name='all_contacts'),

    # Brand New HTML web page route
    path('pages/contacts/', views.html_contact_list, name='html_contacts'),
]