from forms import RegisterForm
from models import BetaTester

from django.shortcuts import render
from django.db import IntegrityError

from django.http import HttpResponseRedirect

def index(request):
    return render(request, 'index.html', {})

def join(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            bt = BetaTester()

            bt.load_from_form(form)
            try:
                bt.save()
            except IntegrityError:
                pass

            return HttpResponseRedirect('/thanks')

    return HttpResponseRedirect('/')

def thanks(request):
    return render(request, 'thanks.html', {})