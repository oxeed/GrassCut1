from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ClientForm

# Create your views here.


def index(request):
   # if request.method == "POST":
        form = ClientForm(request.POST or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/#/')
        else:
            form = ClientForm()
        return render(request, 'index.html', {'form': form})






