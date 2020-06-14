from django.shortcuts import render
from .models import destination

# Create your views here.


def index(request):

    dest1 = destination()
    dest1.name = 'Mumbai'
    dest1.desc = 'The City That Never Sleeps'
    dest1.img = 'destination_4.jpg'
    dest1.price = 700
    dest1.offer = False

    dest2 = destination()
    dest2.name = 'Hyderabad'
    dest2.desc = 'The City Of Love'
    dest2.img = 'destination_2.jpg'
    dest2.price = 650
    dest2.offer = True

    dest3 = destination()
    dest3.name = 'Bangaluru'
    dest3.desc = 'The IT Hub'
    dest3.img = 'destination_6.jpg'
    dest3.price = 750
    dest3.offer = False

    dests = [dest1, dest2, dest3]

    return render(request, "index.html", {'dests': dests})

