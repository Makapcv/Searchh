from django.shortcuts import render
from .models import Info


def InfoView(request):
    info = Info.objects
    print(info.all().values_list()[0])
    return render(request, 'base.html', {'students': info})
