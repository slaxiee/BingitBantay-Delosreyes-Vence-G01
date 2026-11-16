from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .forms import ComplaintForm
from .models import Complaint


@login_required
def my_complaints(request):
    if getattr(request.user, 'role', '') != 'resident':
        messages.error(request, "Only residents can access the resident complaint list.")
        return redirect('dashboard_redirect')

    complaints = Complaint.objects.filter(resident=request.user)
    return render(request, 'complaints/my_complaints.html', {'complaints': complaints})


@login_required
def file_complaint(request):
    if getattr(request.user, 'role', '') != 'resident':
        messages.error(request, "Only residents can file noise complaints.")
        return redirect('dashboard_redirect')

    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.resident = request.user
            complaint.save()
            messages.success(request, "Noise complaint submitted successfully.")
            return redirect('my_complaints')
        else:
            messages.error(request, "Please correct the errors below before submitting.")
    else:
        form = ComplaintForm()

    return render(request, 'complaints/complaint_form.html', {
        'form': form,
        'page_title': 'File a Noise Complaint',
        'submit_label': 'Submit Complaint'
    })


@login_required
def edit_complaint(request, pk):
    complaint = get_object_or_404(Complaint, pk=pk, resident=request.user)

    if complaint.status != 'filed':
        messages.error(request, "You can only edit complaints that are still in 'Filed' status.")
        return redirect('my_complaints')

    if request.method == 'POST':
        form = ComplaintForm(request.POST, instance=complaint)
        if form.is_valid():
            form.save()
            messages.success(request, f"Complaint #{complaint.id} updated successfully.")
            return redirect('my_complaints')
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        form = ComplaintForm(instance=complaint)

    return render(request, 'complaints/complaint_form.html', {
        'form': form,
        'page_title': f'Edit Complaint #{complaint.id}',
        'submit_label': 'Save Changes'
    })


@login_required
def delete_complaint(request, pk):
    complaint = get_object_or_404(Complaint, pk=pk, resident=request.user)

    if complaint.status != 'filed':
        messages.error(request, "Cannot delete a complaint that is already under review or resolved.")
        return redirect('my_complaints')

    if request.method == 'POST':
        complaint_id = complaint.id
        complaint.delete()
        messages.success(request, f"Complaint #{complaint_id} has been deleted.")
        return redirect('my_complaints')

    return render(request, 'complaints/complaint_confirm_delete.html', {'complaint': complaint})