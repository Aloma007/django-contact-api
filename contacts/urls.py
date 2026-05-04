from django.urls import path
from . import views

urlpatterns = [
    # Shows everyone (GET) or adds a new person (POST)
    path('api/contacts/', views.contact_api, name='contact_api'),

    # Shows, updates, or deletes ONE specific person using their ID number
    path('api/contacts/<int:pk>/', views.contact_detail_api, name='contact_detail_api'),

    # Your HTML webpage route
    path('pages/contacts/', views.html_contact_list, name='html_contacts'),
]