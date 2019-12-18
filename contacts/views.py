from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail

# Create your views here.

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']
        listing = request.POST['listing']
        listing_id = request.POST['listing_id']

        ## Making user can NOT make inquery for same home twice , its just once for user for home 
        if request.user.is_authenticated :
            user_id = request.user.id
            has_connected = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_connected :
                messages.error(request, 'You have already made an inquiry for this property')
                return redirect('/listings/'+listing_id)


        contact = Contact(listing = listing, listing_id=listing_id, name=name,
        email=email, message=message, user_id=user_id)

        contact.save()

        ## sending mail to inform realtor that was inqiry made for a property
        send_mail(
        'Property Listing Inquiry', #email subject
        'There has been an inquiry fro' + listing + '. Sign into admin panel for more info', # email body
        'mg69126@gmail.com',# from address wich added in settings , which send from
        [realtor_email, 'mohamedjamaal745@gmail.com'],#realtor email which send to and cover email
        fail_silently=False
        )

        messages.success(request, 'Your request has been submitted, a realtor will get back to you soon . ')
        return redirect('/listings/'+listing_id)