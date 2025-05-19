from django.shortcuts import render, redirect
from .models import contactform
from .forms import contact  

def submit(request):
    if request.method == 'POST':
        form = contact(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration_success')
        else:
            return render(request, 'a.html', {'form': form})
    else:
        return redirect('home')

def registration_success(request):
    return render(request, 'success.html')









def home(request):
    return render(request, "a.html")

def success(request):
    return render(request, 'success.html')



def index(request):
    return render(request, 'index.html')  # ← Ensure it's 'index.html'






