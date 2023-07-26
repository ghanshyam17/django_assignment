# FIRSTAPPLICATION/views.py
from django.shortcuts import render
from .models import Name, ID, Contact, Address



def home(request):
    # Retrieve data from the models
    names = Name.objects.all()
    ids = ID.objects.all()
    contacts = Contact.objects.all()
    addresses = Address.objects.all()

    return render(request, 'home.html', {
        'names': names,
        'ids': ids,
        'contacts': contacts,
        'addresses': addresses,
    })
