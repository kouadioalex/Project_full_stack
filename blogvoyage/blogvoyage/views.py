from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail
from django.shortcuts import render
from .forms_cont import ContactForms


def home_view(request):
    return render(request, 'homes.html')

def contact_view(request):
    form_contact= ContactForms()
    if request.method== 'POST':
        form_contact=ContactForms(request.POST)
        if form_contact.is_valid():
            nom= form_contact.cleaned_data['nom']
            prenom= form_contact.cleaned_data['prenom']
            email= form_contact.cleaned_data['email']
            message= form_contact.cleaned_data['message']
           
            titre= f'Blog | {nom} {prenom} {email}'
            send_mail(titre, message, 'blog.bahalex@gmail.com', ['blog.bahalex@gmail.com'] )
            
        return HttpResponseRedirect(reverse('remercis'))
        
    return render(request, 'contacts.html', {'formulaire':form_contact })

def remerciment_view(request):
    return HttpResponse("je vous remerçis de nous avoir contacté")

