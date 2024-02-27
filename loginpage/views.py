from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import User  # Assuming your user model is named 'User'

def login_view(request):
    print("Login view called")
    if request.method == 'POST':
        print("POST request received")
        # Retrieve email and password from the login form
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Print debug information to console
        print("Received email:", email)
        print("Received password:", password)

        # Check if the user exists in the database
        try:
            # user = User.objects.get(email=email)
            user = User.objects.get(email=email)  # Retrieve user by email
            print("pass",user.email,user.password)
        except User.DoesNotExist:
            user = None

        # If user exists, authenticate the user
        if user is not None:
            # Use the built-in authenticate function to verify the user's credentials
            user_cred = email == user.email and password==user.password

            if user_cred is True:
                # login(request, user)
                # Redirect to the desired URL after successful login
                return redirect('restaurant:restaurant_view')
 # Assuming 'restaurant_view' is the name of the view function or URL pattern
            else:
                # Authentication failed (password incorrect)
                return render(request, 'index.html', {'error': 'Incorrect password'})
        else:
            # User does not exist
            return render(request, 'index.html', {'error': 'User does not exist'})

    # If request method is not POST, render the login page template
    return render(request, 'index.html')
