from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Location
from .forms import LocationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def is_admin(user):
    return user.is_superuser




@login_required
def index(request):
    locations = Location.objects.all()
    form = LocationForm()

    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            location = form.save(commit=False)
            location.created_by = request.user
            location.save()
            return redirect('index')

    return render(request, 'locations/index.html', {
        'locations': locations,
        'form': form,
        'is_admin': request.user.is_superuser,
    })

@login_required
def edit_location(request, pk):
    location = get_object_or_404(Location, pk=pk)
    if request.method == 'POST':
        form = LocationForm(request.POST, instance=location)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = LocationForm(instance=location)
    return render(request, 'locations/edit_location.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def delete_location(request, pk):
    location = get_object_or_404(Location, pk=pk)
    location.delete()
    return redirect('index')

@user_passes_test(is_admin)
def user_list(request):
    users = User.objects.all().exclude(pk=request.user.pk)  # не показывать самого себя
    return render(request, 'locations/user_list.html', {'users': users})

@user_passes_test(is_admin)
def add_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserCreationForm()
    return render(request, 'locations/add_user.html', {'form': form})

@user_passes_test(is_admin)
def delete_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if user != request.user:
        user.delete()
    return redirect('user_list')
