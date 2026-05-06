from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Contact
from .serializers import ContactSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# GENERAL API VIEW (List everyone or Add new) ---
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def contact_api(request):
    if request.method == 'GET':
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)

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