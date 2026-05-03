from django.http import JsonResponse
from django.shortcuts import render  # <--- Added this new tool here!
from .models import Contact


# --- EXISTING JSON API (Safe and untouched) ---
def all_contacts(request):
    # Query the database for all contacts
    contacts_query = Contact.objects.all().values('first_name', 'last_name', 'phone_number')

    # Convert the query to a standard Python list and send it back as JSON
    contacts_list = list(contacts_query)
    return JsonResponse({'contacts': contacts_list})


# --- BRAND NEW HTML VIEW (Added to the bottom) ---
def html_contact_list(request):
    # 1. Fetch all contacts from the database
    all_my_contacts = Contact.objects.all()

    # 2. Render the HTML file and pass the database records into it
    return render(request, 'contact_list.html', {'contacts': all_my_contacts})