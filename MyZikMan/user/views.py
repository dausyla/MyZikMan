from django.shortcuts import render
from django.shortcuts import render, redirect
from user.forms import UserForm,BandForm
from user.models import User,Band


def createUser(request):
    # if the form has already been filled
    if request.method == "POST":
        # get the form answer
        form = UserForm(request.POST)
        # if the form is valid
        if form.is_valid():
            try:
                # save the answers and create the user
                form.save()
                # Get back to the read page
                return redirect('/read')
            except:
                pass
    # otherwise get the form
    else:
        form = UserForm()
    # go to the form
    return render(request, 'createUser.html', {'form': form})

def createBand(request):
    # if the form has already been filled
    if request.method == "POST":
        # get the form answer
        form = BandForm(request.POST)
        # if the form is valid
        if form.is_valid():
            try:
                # save the answers and create the band
                form.save()
                # Get back to the read page
                return redirect('/read')
            except:
                pass
    # otherwise get the form
    else:
        form = BandForm()
    # go to the form
    return render(request, 'createBand.html', {'form': form})


def read(request):
    # Get all user and band
    users = User.objects.all()
    bands = Band.objects.all()
    # return http response with all users in parameters
    return render(request, "read.html", {'users': users, 'bands': bands})


def editUser(request, id):
    # get the user with its id
    user = User.objects.get(id=id)
    bands = Band.objects.all()
    # return http response with all users in parameters
    return render(request, 'editUser.html', {'user': user, 'bands': bands})

def editBand(request, id):
    # get the band with its id
    band = Band.objects.get(id=id)
    # return http response with all users in parameters
    return render(request, 'editBand.html', {'band': band})


def updateUser(request, id):
    # get the user with its id
    user = User.objects.get(id=id)
    # get the form filled
    form = UserForm(request.POST, instance=user)
    # if the form is valid
    if form.is_valid():
        # save the answers
        form.save()
        # get back the read page
        return redirect("/read")
    # otherwise get back to the edit page with
    return render(request, 'editUser.html', {'user': user})

def updateBand(request, id):
    # get the band with its id
    band = Band.objects.get(id=id)
    # get the form filled
    form = BandForm(request.POST, instance=band)
    # if the form is valid
    if form.is_valid():
        # save the answers
        form.save()
        # get back the read page
        return redirect("/read")
    # otherwise get back to the edit page with
    return render(request, 'editBand.html', {'band': band})


def destroyUser(request, id):
    # get the user with its id
    user = User.objects.get(id=id)
    # delete the object
    user.delete()
    # get back to the read page
    return redirect("/read")

def destroyBand(request, id):
    # get the band with its id
    band = Band.objects.get(id=id)
    # delete the object
    band.delete()
    # get back to the read page
    return redirect("/read")