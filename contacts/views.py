from django.db.models import Q
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Contact
from .serializers import ContactSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination


# GENERAL API VIEW (List everyone or Add new) ---
@api_view(['GET', 'POST'])
#@permission_classes([IsAuthenticated])
def contact_api(request):
    if request.method == 'GET':
        # 1. Grab everyone by default
        contacts = Contact.objects.all()

        # --- NEW SEARCH & FILTERING LOGIC ---
        # 2. Check if the frontend sent a search word
        search_query = request.query_params.get('search', None)

        if search_query is not None:
            # 3. If they did, filter the database.
            # We use Q objects to search BOTH first_name and last_name!
            contacts = contacts.filter(
                Q(first_name__icontains=search_query) |
                Q(last_name__icontains=search_query)
            )

        # --- TRAFFIC CONTROL (Unchanged) ---
        paginator = PageNumberPagination()
        paginator.page_size = 2
        paginated_contacts = paginator.paginate_queryset(contacts, request)

        serializer = ContactSerializer(paginated_contacts, many=True)
        return paginator.get_paginated_response(serializer.data)

    if request.method == 'POST':
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

# SPECIFIC CONTACT API (Read one, Update, or Delete) ---
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def contact_detail_api(request, pk):
    # First, try to find the specific person using their ID
    try:
        contact = Contact.objects.get(pk=pk)
    except Contact.DoesNotExist:
        return Response({'error': 'Contact not found'}, status=404)

    # READ: If they just want to see this specific person's details
    if request.method == 'GET':
        serializer = ContactSerializer(contact)
        return Response(serializer.data)

    # UPDATE: If they are sending new data to change the details
    if request.method == 'PUT':
        serializer = ContactSerializer(contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    # DELETE: If they want to wipe this person from the database
    if request.method == 'DELETE':
        contact.delete()
        return Response({'message': 'Contact deleted successfully'}, status=204)

# --- 3. YOUR HTML VIEW (Safe and untouched) ---
def html_contact_list(request):
    all_my_contacts = Contact.objects.all()
    return render(request, 'contact_list.html', {'contacts': all_my_contacts})