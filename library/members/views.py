from django.shortcuts import render, redirect
from .forms import BookTakenForm, BookEditForm
from .models import Member
from book_store.models import Book
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.urls import reverse
# Create your views here.


def book_form(request):
    if request.method == "POST":
        form = BookTakenForm(request.POST)
        if form.is_valid():
            form.save()
            if form.cleaned_data['book_status'] == "Borrowed":
                book_name = form.cleaned_data.get('book_name')
                instance = Book.objects.get(name=book_name)
                instance.status = 'Not Available'
                instance.save()
            messages.success(request, "Record is Saved")
            return redirect('members:book_form')
        else:
            return render(request, 'book_taken_form.html', {'form': form})
    else:
        form = BookTakenForm()
        return render(request, 'book_taken_form.html', {'form': form})

def borrow_list(request):
    book_borrowers = Member.objects.filter(book_status='Borrowed')
    book_returned = Member.objects.filter(book_status='Returned')
    context = {'book_borrowers': book_borrowers, 'book_returned': book_returned}
    return render(request,'borrow_list.html', context)

def borrow_list_edit(request, id):
    profile = Member.objects.get(id=id)
    form = BookEditForm(request.POST or None, instance=profile)
    if form.is_valid():
        form.save()
        if form.cleaned_data.get('book_status') == 'Returned':
            book_name = form.cleaned_data.get('book_name')
            instance = Book.objects.get(name=book_name)
            instance.status = 'Available'
            instance.save()
        return redirect('book_store:book_details')
    return render(request, 'edit_profile.html', {'form': form, 'profile': profile})
# def update(request,id):
    # task=Task.objects.get(id=id)
    # form1=TodoForm(request.POST or None, instance=task)
    # if form1.is_valid():
    #     form1.save()
    #     return redirect('/')
    # return render(request,'edit.html',{'form1':form1,'task':task})

# class Member_update_view(UpdateView):
#     model = Member
#     template_name = 'edit_profile.html'
#     context_object_name = 'profile'
#     fields = ['name', 'book_name', 'return_date', 'book_status', 'phone_number', 'member_id']
#     def get_success_url(self):
#         if form.cleaned_data.get('book_status') == 'Returned':
#             book_name = form.cleaned_data.get('book_name')
#             instance = Book.objects.get(name=book_name)
#             instance.status = 'Available'
#             instance.save()
#         return reverse('members:cbvdetail', kwargs={'pk':self.object.id})
    
# class Task_details_view(DetailView):
#     model= Member
#     template_name = 'member_view.html'
#     context_object_name = 'profile'