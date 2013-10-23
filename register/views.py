from forms import RegisterForm
from models import BetaTester

from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

def join(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            bt = BetaTester()

            bt.load_from_form(form)
            bt.save()

            return render(request, 'thanks.html', {})

    return render(request, 'index.html', {})