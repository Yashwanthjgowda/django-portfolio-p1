from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

def home(request):
    """
    Renders the main homepage.
    """
    return render(request, 'home.html')

def contact(request):
    """
    Handles the contact form submission.
    """
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        content = request.POST.get('content')

        # Basic validation checks
        if not (2 < len(name) < 30):
            messages.error(request, 'Name length should be greater than 2 and less than 30 characters.')
            return redirect('home')  # Redirect back to the home view
        
        if not (1 < len(email) < 30):
            messages.error(request, 'Invalid email. Please try again.')
            return redirect('home')
        
        # Check if number is a valid length, assuming it's a string
        if not (9 < len(number) < 13):
            messages.error(request, 'Invalid number. Please try again.')
            return redirect('home')

        # Save the contact form data to the database
        ins = Contact(name=name, email=email, content=content, number=number)
        ins.save()

        # Set a success message
        messages.success(request, 'Thank you for contacting me! Your message has been saved.')
        
        # Redirect to the home page after a successful POST request
        return redirect('home')

    # If it's a GET request, do nothing and let the home page handle rendering
    return redirect('home')