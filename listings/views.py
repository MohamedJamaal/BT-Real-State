from django.shortcuts import render, get_object_or_404 
from django.core.paginator import EmptyPage , PageNotAnInteger , Paginator
from .choices import price_choices, state_choices, bedroom_choices
from .models import Listing


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True) ##show page content order by date & published posts

    ## Pagination
    paginator = Paginator(listings , 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    ## show content of page
    context = {
        'listings' : paged_listings
    }
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing , pk=listing_id)

    context = {
        'listing' : listing
    }
    return render(request, 'listings/listing.html', context)

def search(request):

    queryset_list = Listing.objects.order_by('-list_date')

    #Keywords check
    if 'keywords' in request.GET : #check if it exists 
        keywords = request.GET['keywords']
        if keywords :  # searching the word in the description
            queryset_list = queryset_list.filter(description__icontains=keywords)
    
    # city check
    if 'city' in request.GET : #check if it exists in search label
        city = request.GET['city']
        if city :  # searching the exact word in the description
            queryset_list = queryset_list.filter(city__iexact=city)
    
    #state check
    if 'state' in request.GET : #check if it exists 
        state = request.GET['state']
        if state :  # searching the word 
            queryset_list = queryset_list.filter(state__icontains=state)
    
     #bedrooms check
    if 'bedrooms' in request.GET : #check if it exists 
        bedrooms = request.GET['bedrooms']
        if bedrooms :  # searching the less than or equal 
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)
    
    #price check
    if 'price' in request.GET : #check if it exists 
        price = request.GET['price']
        if price :  # searching the less than or equal 
            queryset_list = queryset_list.filter(price__lte=price)
    
    context = {
        'state_choices':state_choices,
        'bedroom_choices':bedroom_choices,
        'price_choices':price_choices,
        'listings':queryset_list,
        'values': request.GET, ## 3shan n5ly search word tsbt fel label w btzwd value attr fel input tag
    }
    return render(request, 'listings/search.html', context)
