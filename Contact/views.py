from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.generic import ListView

from .models import Contact
from .forms import ContactForm


def addContact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.instance.username = request.user
            form.save()
            messages.success(request, "Contact Created Successfully")
            return redirect('viewContact')
        else:
            messages.error(request, "Contact Not Created Successfully")
    else:
        form = ContactForm()
    return render(request, 'Contact/ContactFrom.html', {'form': form})


class viewContactList(ListView):
    model = Contact
    template_name = 'Contact/ContactView.html'
    context_object_name = 'object_list'
    # paginate_by = 2


def deleteContact(request, pk, template_name='Contact/Contact_Confirm_Delete.html'):
    training = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        training.delete()
        messages.success(request, "Contact Deleted Successfully")
        return redirect('viewContact')
    # else:
    #     messages.error(request, "Training Not Deleted Successfully")
    return render(request, template_name, {'object': training})


def updateContact(request,pk):
    training = get_object_or_404(Contact, pk=pk)
    form = ContactForm(request.POST or None, request.FILES or None, instance=training)
    if form.is_valid():
        form.save()
        messages.success(request, "Contact Updated Successfully")
        return redirect("viewContact")
    # else:
    #     messages.error(request, "Training Not Updated Successfully")
    return render(request, 'Contact/ContactFrom.html', {'form': form})


