from datetime import date

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, add_record_form
from .models import Record, monthly_record
from celery import shared_task
from datetime import date, timedelta
def home(request):
    # check to see if logging in
    records = Record.objects.all()
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in')
            return redirect('home')
        else:
            messages.success(request, 'There was an error logging in, please try again...')
            return redirect('home')
    else:
        return render(request, 'home.html', {'records':records})

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out...')
    return redirect('home')

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})



def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, 'Record deleted successfully...')
        return redirect('home')
    else:
        messages.success(request, 'You must be logged in to delete a record!')
        return redirect('home')


def add_record(request):
    form = add_record_form(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                new_record = form.save(commit=False)
                new_record.userid = request.user.id
                new_record.save()
                messages.success(request, 'Record added successfully...')
                return redirect('home')
        return render(request, 'add_record.html', {'form':form})
    else:
        messages.success(request, 'You must be logged in to add a record!')
        return redirect('home')

def report(request):
    records = Record.objects.all()
    month_report = monthly_record.objects.all()
    if request.user.is_authenticated:
        outcome, expense = 0, 0
        for record in records:
            if record.income == "Expense":
                expense += record.amount
            else:
                outcome += record.amount
        return render(request, 'report.html', {'records':records, 'outcome':outcome, 'expense':expense})
    return render(request, 'report.html', {'records':records})

def view_recurring_records(request):
    recurring_record = Records.objects.filter(recurrance =['Weekly', 'Biweekly', 'Monthly'] )

#def delete_recurring_record(request, pk):


