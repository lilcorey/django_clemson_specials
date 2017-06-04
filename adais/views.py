from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import ensure_csrf_cookie
from django.template import loader, RequestContext
from django.template.context_processors import csrf
from datetime import datetime as date
import calendar

from .models import Deal, Restaurant
from .forms import *

DAYS_OF_WEEK = (
    (7, 'All Week'),
    (0, 'Sunday'),
    (1, 'Monday'),
    (2, 'Tuesday'),
    (3, 'Wednesday'),
    (4, 'Thursday'),
    (5, 'Friday'),
    (6, 'Saturday'),
)
def dis_day(x):
  return '%s' % x

def index(request):
    #query based on request
    #today = date.today().strftime("%A")
    today = calendar.day_name[datetime.now(pytz.timezone('America/New_York')).weekday()]
    todayId = 0
    for item in DAYS_OF_WEEK:
      if item[1] == today:
        todayId = item[0]
    p = Deal.objects.filter(day=todayId).order_by('restaurantId')
    #p = Deal.objects.all().order_by('restaurantId')
    if p.exists():
      if p.count() >= 2:
        half = p.count()/2
        return render( request, "adais/dashboard.html",
                       {'username': request.user.username,
                        'deals1' : p[0:half], 'deals2' : p[half:],
                        'dealTitle': "Today's"} )
      else:
        return render( request, "adais/dashboard.html",
                       {'username': request.user.username,
                        'deals1' : p, 'deals2' : {},
                        'dealTitle': "Today's"} )
    else:
      return render(request, "adais/dashboard.html",
                  {'username': request.user.username, 'deals1': {}, 'deals2': {}, 'dealTitle' : "Today's" })

  # return HttpResponseRedirect('dashboard/')
  #else:
   # return HttpResponseRedirect('login/')


def signup(request):
  if request.POST:
    form = UserCreateForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/adais/signup/complete/')
  else:
    form = UserCreateForm()

  token = {}
  token.update(csrf(request))
  token['form'] = form
  return render_to_response('adais/signup_form.html', token)


def signup_complete(request):
  return render_to_response('adais/signup_complete.html')


@ensure_csrf_cookie
def user_login(request):
  # template_name = 'adais/login.html'
  if request.POST:
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)
    if user is not None:
      login(request, user)
      return HttpResponseRedirect('/')
    else:
      messages.error(request, 'Invalid login credentials')
      return render(request, 'adais/login.html')
    # return HttpResponse("invalid login info")
  return render(request, 'adais/login.html')


def logout(request):
  redirect('/login/')


def page_not_found(request):
  # response = HttpResponseNotFound('404.html', {},
  #                              context_instance=RequestContext(request))
  response.status_code = 404
  return response

def restaurant(request, url_id):
  p = Deal.objects.filter(restaurantId_id=url_id)
  if p.exists():
    if p.count() >= 2:
      half = p.count() / 2
      return render(request, "adais/dashboard.html",
                    {'username': request.user.username,
                     'deals1': p[0:half], 'deals2': p[half:],
                     'dealTitle' : Restaurant.objects.only('name').get(restaurantId=url_id)})
    else:
      return render(request, "adais/dashboard.html",
                    {'username': request.user.username,
                     'deals1': p, 'deals2': {},
                     'dealTitle' : Restaurant.objects.only('name').get(restaurantId=url_id)})
  else:
    return render(request, "adais/dashboard.html",
                  {'username': request.user.username,
                   'deals1': {}, 'deals2': {},
                   'dealTitle' : Restaurant.objects.only('name').get(restaurantId=url_id)})


def day(request, url_id):
  p = Deal.objects.filter(day=url_id)
  titleName = ""
  for item in DAYS_OF_WEEK:
    if item[0] == int(url_id):
      titleName = dis_day(item[1])
  if p.exists():
    if p.count() >= 2:
      half = p.count() / 2
      return render(request, "adais/dashboard.html",
                    {'username': request.user.username,
                     'deals1': p[0:half], 'deals2': p[half:],
                     'dealTitle': titleName })
    else:
      return render(request, "adais/dashboard.html",
                    {'username': request.user.username,
                     'deals1': p, 'deals2': {},
                     'dealTitle': titleName})
  else:
    return render(request, "adais/dashboard.html",
                  {'username': request.user.username,
                   'deals1': {}, 'deals2': {},
                   'dealTitle': titleName })


def dashboard(request):
  return HttpResponseRedirect('/adais/')
  # return render(request, "adais/dashboard.html", {'username':request.user.username})

def addDeal(request):
  if request.user.is_authenticated():
    if request.POST:
      daysOfDeal = request.POST.getlist('daysList')
      form = addDealForm(request.POST)
      if form.is_valid():
        aDeal = form.save(commit=False)
        print("VALID")
        print(daysOfDeal)
        if aDeal.startTime is None:
          aDeal.startTime = "00:00"
        if aDeal.endTime is None:
          aDeal.endTime = "00:00"

        for i in daysOfDeal:
          aDeal.pk = None
          aDeal.day = int(i)
          #print(aDeal.encode(sys.stdout.encoding, 'replace'))
          #print(aDeal.day)
          aDeal.save()
        return HttpResponseRedirect('/')

    else:
      form = addDealForm()

    token = {}
    token.update(csrf(request))
    token['form'] = form
    return render_to_response('adais/addDeal.html', token)
  else:
    return HttpResponseRedirect('/login/')
