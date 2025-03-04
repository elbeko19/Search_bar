from django.shortcuts import render
from .models import Data
from django.db.models import Q


def index(request):
    if 'q' in request.GET:
        q = request.GET['q']

        # data = Data.objects.filter(first_name__icontains=q)
        multiple = Q(Q(first_name__icontains=q) | Q(last_name__icontains=q) | Q(age__icontains=q))
        data = Data.objects.filter(multiple)
    else:
        data = Data.objects.all()
    context = {
        'data': data
    }
    return render(request, 'dashboard/index.html', context)