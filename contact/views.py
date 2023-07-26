from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages 
from django.http import JsonResponse

# Create your views here.
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            if request.headers.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
                return JsonResponse({'success': True, 'message': 'Thanks. We are going to contact you soon.'})
            else:
                messages.success(request, 'Thanks. We are going to contact you soon.')
                return redirect('contact:contact')  # Redirect to the contact page after a successful form submission
        else:
            if request.headers.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
                # If it's an AJAX request and the form is not valid, return a JSON response with errors
                return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})