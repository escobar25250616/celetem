from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        # on ignore les identifiants, pas de vérification réelle
        return redirect('merci')
    return render(request, 'accounts/login.html')

def merci_view(request):
    return render(request, 'accounts/merci.html')
