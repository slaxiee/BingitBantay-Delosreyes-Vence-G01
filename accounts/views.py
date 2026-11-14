from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, UserProfileForm
from .models import User


def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            if user.role in ['tanod', 'official']:
                user.is_approved = False
                messages.info(request, "Registration submitted. Please wait for a Barangay Official to approve your account.")
            else:
                user.is_approved = True
                messages.success(request, "Account created successfully! You can now log in.")
            user.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard_redirect')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        for field in form.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
        if form.is_valid():
            user = form.get_user()
            if not getattr(user, 'is_approved', True) and not user.is_superuser:
                messages.warning(request, "Your staff account is still pending approval by a Barangay Official.")
                return redirect('login')
            login(request, user)
            return redirect('dashboard_redirect')
    else:
        form = AuthenticationForm()
        for field in form.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('login')


@login_required
def dashboard_redirect(request):
    user = request.user
    if user.is_superuser or getattr(user, 'role', '') == 'official':
        return redirect('official_dashboard')
    elif getattr(user, 'role', '') == 'tanod':
        return redirect('tanod_dashboard')
    elif getattr(user, 'role', '') == 'resident':
        return redirect('resident_dashboard')
    return render(request, 'accounts/resident_dashboard.html')


@login_required
def resident_dashboard(request):
    return render(request, 'accounts/resident_dashboard.html')


@login_required
def tanod_dashboard(request):
    return render(request, 'accounts/tanod_dashboard.html')


@login_required
def official_dashboard(request):
    pending_staff = User.objects.filter(role__in=['tanod', 'official'], is_approved=False)
    return render(request, 'accounts/official_dashboard.html', {'pending_staff': pending_staff})


@login_required
def approve_staff(request, user_id):
    if getattr(request.user, 'role', '') != 'official' and not request.user.is_superuser:
        return redirect('dashboard_redirect')
    staff_user = get_object_or_404(User, id=user_id)
    staff_user.is_approved = True
    staff_user.save()
    messages.success(request, f"{staff_user.get_full_name() or staff_user.username} has been approved.")
    return redirect('official_dashboard')


@login_required
def profile_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect('profile')
        else:
            messages.error(request, "Please fill out all required fields before saving.")
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'accounts/profile.html', {'form': form})