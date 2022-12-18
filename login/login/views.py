from django.contrib.auth import authenticate, login
from .models import FormData
from django.shortcuts import render, redirect
from forms import FormDataForm
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from login.models import FormData


def index(request):
    template = loader.get_template('login/index.html')
    context = {}
    return HttpResponse(template.render(context, request))


def index(request):

    account_number = request.POST.get('Account Number')

    account_name = request.POST.get('Account Name')

    interest_rate = request.POST.get('Interest Rate')

    overdue_limit = request.POST.get('Overdue Limit')

    savebutton = request.POST.get('Submit')

    context = {'Account Number': account_number, 'Account Name': account_name,
               'Interest Rate': interest_rate, 'Overdue Limit': overdue_limit,
               'Save': savebutton}

    return render(request, 'base.html', context)


def dashboard(request):
    return render(request, 'dashboard.html')


def base(request):
    if request.method == "POST":
        form = FormData(request.POST)
    if form.is_valid():
        form.save()
        account_number = request.POST.get('Account Number')

        account_name = request.POST.get('Account Name')

        interest_rate = request.POST.get('Interest Rate')

        overdue_limit = request.POST.get('Overdue Limit')

        savebutton = request.POST.get('Submit')
        print(account_number, account_name,
              interest_rate, overdue_limit, savebutton)
        ins = FormData(Account_Number=account_number, Account_Name=account_name,
                       Interest_Rate=interest_rate, Overdue_Limit=overdue_limit)
        ins.save()
        print("The data has been processed successfully")

        context = {'Account Number': account_number, 'Account Name': account_name,
                   'Interest Rate': interest_rate, 'Overdue Limit': overdue_limit,
                   'Save': savebutton}

    if form.is_valid():
        form.save()
        # do something with the saved data
        ...
    else:
        form = FormData()
        return render(request, 'base.html', {'form': form})

        account_number = request.POST.get('Account Number')

        account_name = request.POST.get('Account Name')

        interest_rate = request.POST.get('Interest Rate')

        overdue_limit = request.POST.get('Overdue Limit')

        savebutton = request.POST.get('Submit')

        context = {'Account Number': account_number, 'Account Name': account_name,
                   'Interest Rate': interest_rate, 'Overdue Limit': overdue_limit,
                   'Save': savebutton}

    return render(request, 'base.html', {'form': form})
    return render(request, 'dashboard.html')


def due(request):
    return render(request, 'due_loans.html')


def help(request):
    return render(request, 'help.html')


def logout(request):
    return render(request, 'logout.html')


def principal(request):
    return render(request, 'principal.html')


def payments(request):
    return render(request, 'payments.html')


def profile(request):
    return render(request, 'profile.html')


def purchase(request):
    return render(request, 'purchase.html')


def login(request):
    return render(request, 'login.html')


def search_view(request):
    elements = login.objects.all()
    search_term = request.GET.get('search')
    if search_term:
        elements = elements.filter(name__contains=search_term)
        context = {'elements': elements}
        return render(request, 'base.html', context)


def form_view(request):
    if request.method == 'POST':
        form = FormDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('form_success')
    else:
        form = FormDataForm()
    return render(request, 'base.html', {'form': form})


def view_form_data(request):
  form_data = FormData.objects.all()
  context = {'form_data': form_data}
  return render(request, 'base.html', context)


def login_view(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      return redirect('home')
    else:
      return render(request, 'logout.html', {'form': form})
  else:
    return render(request, 'logout.html')


def login_view(request):
  correct_username = 'lynnakinyi2003@gmail.com'
  correct_password = '208oAL##'
  if request.method == 'POST':
    username = request.POST['lynnakinyi2003@gmail.com']
    password = request.POST['208oAL##']
    if username == correct_username and password == correct_password:
      user = authenticate(request, username=username, password=password)
      logout(request, user)
      return redirect('dashboard/')
    else:
      return render(request, 'logout.html', {'form': form, 'error': 'Invalid username or password'})
  else:
    return render(request, 'logout.html')

