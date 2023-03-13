from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from user.forms import RegisterUserForm, RequestForm
from user.models import Request


def register(request):
    # check if the form was submitted (HTTP POST request)
    if request.method == "POST":
        # create a form object with the submitted data
        form = RegisterUserForm(request.POST)
        # if the form is valid
        if form.is_valid():
            # save the form and create a new user
            form.save()
            # retrieve the username and password from the form's cleaned data
            userName = form.cleaned_data['username']
            userPassword = form.cleaned_data['password1']
            # authenticate the user and log them in
            user = authenticate(username=userName, password=userPassword)
            login(request, user)
            # redirect the user to the requests page
            return redirect('/requests')
        else:
            # if the form is not valid, display an error message for each error
            for error in form.errors:
                messages.info(request, form.errors[error])
    else:
        # if the form was not submitted (HTTP GET request), create a new form object
        form = RegisterUserForm()
    # render the registration page with the form object as a context variable
    return render(request, 'register.html', {'form': form})


def loginUser(request):
    if request.method == "POST":  # check if request method is POST
        # get the username from the POST data
        userName = request.POST['username']
        # get the password from the POST data
        userPassword = request.POST['password']
        user = authenticate(request, username=userName,
                            password=userPassword)  # authenticate user
        if user is not None:  # if authentication is successful
            login(request, user)  # log in the user
            return redirect('/requests')  # redirect to the requests page
        else:  # if authentication is not successful
            # display error message
            messages.info(request, "Username and password doesn't match!")
            return redirect('/login')  # redirect to the login page
    else:  # if request method is not POST
        return render(request, 'login.html', {})  # render the login page


def logoutUser(request):
    # logout the request user
    logout(request)
    # add message on the requests page
    messages.info(request, "You were logout!")
    # redirect to requests page
    return redirect('/requests')


def createRequest(request):
    # Check if the user is authenticated
    usr = request.user
    if usr.is_authenticated:
        if request.method == "POST":
            # If the request is a POST request, get the form data
            form = RequestForm(request.POST)
            print(form.errors)
            if form.is_valid():
                # If the form data is valid, create a request instance
                try:
                    req = super(RequestForm, form).save(commit=False)
                    # Set the creator of the request to the current user
                    req.requestCreator = usr
                    # Save the request instance to the database
                    req.save()
                    # Redirect the user to the requests page
                    return redirect('/requests')
                except:
                    # If there is an error while creating the request, do nothing
                    pass
            else:
                # If the form data is invalid, display the errors to the user
                for error in form.errors:
                    messages.info(request, form.errors[error])
        else:
            # If the request is not a POST request, display an empty form to the user
            form = RequestForm()
        return render(request, 'createRequest.html', {'form': form})
    else:
        # If the user is not authenticated, redirect them to the requests page with a message
        messages.info(request, "You need to be login!")
        return redirect('/requests')


def requests(request):
    # Get all requests
    req = Request.objects.all()
    # render the requests page with all requests
    return render(request, "requests.html", {'requests': req, 'usr': request.user})


def editRequest(request, requestId):
    # Retrieve the request object based on the requestId provided
    req = Request.objects.get(id=requestId)

    # Check if the user is authenticated and if they are the creator of the request
    if (request.user.is_authenticated and request.user.id == req.requestCreator.id):

        # Handle form submission for editing a request
        if request.method == "POST":
            form = RequestForm(request.POST, instance=req)
            if form.is_valid():
                form.save()
                messages.info(request, "Request modified!")
                return redirect("/requests")
            else:
                # If there are form errors, display them as messages
                for error in form.errors:
                    messages.info(request, form.errors[error])

        # Render the edit request form with the existing request object
        else:
            return render(request, "editRequest.html", {'req': req})

    # If the user is not authenticated or not the creator of the request, redirect to requests page
    return redirect("/requests")


def deleteRequest(request, requestId):
    # Get the request
    req = Request.objects.get(id=requestId)
    # If user is authenticated
    if request.user.is_authenticated and request.user.id == req.requestCreator.id:
        # Delete the request and add message Request deleted
        req.delete()
        messages.info(request, "Request deleted!")
    else:
        # if not, add message to say so
        messages.info(request, "You are not the creator of this request!")
    return redirect("/requests")


def seeRequest(request, requestId):
    # Get the request
    req = Request.objects.get(id=requestId)
    # return the seeRequest page with the request
    return render(request, 'seeRequest.html', {'req': req})
