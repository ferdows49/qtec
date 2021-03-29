from datetime import datetime, timedelta, date
from django.shortcuts import render
from .models import S_history


def is_valid_queryparam(param):
    return param != '' and param is not None


def home(request):
    qs = S_history.objects.all().order_by("-time")

    keyword = request.GET.get('keyword')
    user = request.GET.get('user')
    for_today = request.GET.get('for_today')
    from_yesterday = request.GET.get('from_yesterday')
    from_last_week = request.GET.get('from_last_week')
    from_last_month = request.GET.get('from_last_month')
    date_min = request.GET.get('date_min')
    date_max = request.GET.get('date_max')

    if is_valid_queryparam(keyword):
        qs = qs.filter(keyword__contains=keyword)

    if is_valid_queryparam(user):
        qs = qs.filter(user__iexact=user)

    if is_valid_queryparam(for_today):
        today = date.today()
        qs = qs.filter(time__year=today.year, time__month=today.month, time__day=today.day)

    if is_valid_queryparam(from_yesterday):
        yesterday = datetime.today() - timedelta(days=1)
        qs = qs.filter(time__gte=yesterday)

    if is_valid_queryparam(from_last_week):
        last_week = datetime.today() - timedelta(days=7)
        qs = qs.filter(time__gte=last_week)

    if is_valid_queryparam(from_last_month):
        last_month = datetime.today() - timedelta(days=30)
        qs = qs.filter(time__gte=last_month)

    if is_valid_queryparam(date_min):
        qs = qs.filter(time__gte=date_min)

    if is_valid_queryparam(date_max):
        qs = qs.filter(time__lte=date_max)
        
    return render(request, 'base_generic.html', {'qs': qs})

