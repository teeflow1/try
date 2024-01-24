from django.shortcuts import render
from django.core.mail import send_mail



def home(request):
    
    if request.method == 'POST':
        name = request.POST['name']    
        lname = request.POST['lname']  
        email = request.POST['email'] 
        subject = request.POST['subject']
        message = request.POST['message']
        
        
        send_mail(
            
           'message from ' + name, #Subject
            message, # message
            #subject, # subject
            email, # from email
           ['temitopeayobami995@gmail.com'], # to email
        )
        return render(request, 'apps/index.html', {'name': name}) 
    else:
        return render(request, 'apps/index.html', {})
          
    
    

def property(request):
    return render(request, 'apps/property.html', {})

def listings(request):
    return render(request, 'apps/listings.html', {})
