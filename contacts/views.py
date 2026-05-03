from django.http import JsonResponse
from .models import Contact


def all_contacts(request):
    # Query the database for all contacts
    contacts_query = Contact.objects.all().values('first_name', 'last_name', 'phone_number')

    # Convert the query to a standard Python list and send it back as JSON
    contacts_list = list(contacts_query)
    return JsonResponse({'contacts': contacts_list})