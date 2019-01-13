from django.shortcuts import render, redirect
from django.contrib import messages
from contacts.models import Contact
from django.core.mail import send_mail
def contact(request):
	if request.method == "POST":
		listing_id = request.POST['listing_id']
		listing = request.POST['listing']
		name = request.POST['name']
		email =  request.POST['email']
		phone = request.POST['phone']
		message = request.POST['message']
		user_id = request.POST['user_id']
		realtor_email =  request.POST['realtor_email']

		#check enquiry
		if request.user.is_authenticated:
			user_id =request.user.id
			listing_user = Contact.objects.all().filter(listing_id=listing_id,user_id=user_id)
			if listing_user:
				messages.error(request,'Already send')
				return redirect('/listings/'+listing_id)

		contact = Contact(listing_id=listing_id,listing=listing,name=name,email=email,phone=phone,user_id=user_id)
		contact.save()

		send_mail(
			'For Enquiry',
			'This is enquirt for listing '+ listing +'. please check',
			'birle.megha@gmail.com',
			[realtor_email,'mbirle123@gmail.com','meghabirle@gmail.com'],
			fail_silently=False 

			)

		messages.success(request,'Your Enquiry is submitted')
		return redirect('/listings/'+listing_id)
