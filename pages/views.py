from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import price_choices, bedroom_choices, state_choices

from listings.models import Listing
from realtors.models import Realtor

listob = Listing.objects #objects of model Listings
realob = Realtor.objects #objects of model Realtor

def index(request):
    listings = listob.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
    }

    return render(request, 'pages/index.html', context)


def about(request):
    # Get all realtors
    realtors = realob.order_by('-hire_date')

    # Get MVP
    mvp_realtors = realob.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }

    return render(request, 'pages/about.html', context)