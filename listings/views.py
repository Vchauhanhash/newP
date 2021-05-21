from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from .models import Listing


def index(request):
    listings = Listing.objects.all()

    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }

    return render(request, 'listings/listings.html', context)


def listing(request):
    return render(request, 'listings/listing.html')


def search(request):
    return render(request, 'listings/search.html')
