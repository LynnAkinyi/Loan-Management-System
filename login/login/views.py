from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def index(request):
     template = loader.get_template('login/index.html')
     context = {}
     return HttpResponse(template.render(context, request))

def index(request):

    account_number= request.POST.get('Account Number')

    account_name= request.POST.get('Account Name')

    interest_rate= request.POST.get('Interest Rate')

    overdue_limit= request.POST.get('Overdue Limit')

    savebutton= request.POST.get('Submit')
    
    context= {'Account Number': account_number, 'Account Name':account_name,
              'Interest Rate': interest_rate, 'Overdue Limit': overdue_limit,
              'Save': savebutton}
        
    return render(request, 'login/base.html', context)

def dashboard(request):
    return render(request, 'dashboard.html')
def due(request):
    return render(request, 'due_loans.html')
def help(request):
    return render(request, 'help.html')
def logout(request):
    return render(request, 'logout.html')
def payments(request):
    return render(request, 'principal.html')
def profile(request):
    return render(request, 'profile.html')
def purchase(request):
    return render(request, 'purchase.html')


