from django.shortcuts import render
from django.http import HttpResponse
from .models import Enquiry, Events, Options

def index(request):
    events = Events.objects.all()
    message=""
    status="none"
    if request.method == 'POST':
        email = request.POST['email']
        message = request.POST['message']   
        e = Enquiry(email=email, message=message)
        e.save()
        status="success"
        message="Message Sent Successfully"
    return render(request, 'voting_app/index.html', {'message': message, 'status': status, 'events': events})

def host_event_page(request):
    return render(request, 'voting_app/host_event_page.html')

def participate_to_vote(request):
    return render(request, 'voting_app/participate_to_vote.html')

def event_page(request, event_code):
    event = Events.objects.get(event_code=event_code)
    options = Options.objects.filter(event_code=event)
    total_count = 0
    percs = []
    for option in options:
        total_count += option.count
    for option in options:
        per = (option.count*100) / total_count
        percs.append(per)
    max_vote = 0
    winner = ''
    for option in options:
        if option.count > max_vote:
            max_vote = option.count
            winner = option.option_name
    return render(request, 'voting_app/event_page.html', {'event_code': event_code, 'event': event, 'total_count': total_count, 'options': options, 'percs': percs, 'winner': winner})

def dashboard(request):
    return render(request, 'voting_app/dashboard.html')
