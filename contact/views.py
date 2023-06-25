from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages 

# Create your views here.
def contact_view(request):
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thanks. We are going to contact you soon.')
            return redirect('contact:contact')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})