from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record
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

def add_expense(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            expense_name = request.POST['expense_name']
            expense_amount = request.POST['expense_amount']
            expense_date = request.POST['expense_date']
            expense_category = request.POST['expense_category']
            new_expense = Record(expense_name=expense_name, expense_amount=expense_amount, expense_date=expense_date, expense_category=expense_category)
            new_expense.save()
            messages.success(request, 'Expense added successfully!')
            return redirect('home')
    else:
        messages.success(request, 'You must be logged in to add an expense!')
        return redirect('home')