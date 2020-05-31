
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Enquiry, Events, Options
from django.contrib.auth.models import User

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
    msg_flag = -1
    if request.method == 'POST':
        msg_flag = 0
        event_name = request.POST['event_name']
        event_description = request.POST['event_description']
        event_code = request.POST['event_code']
        referal_code = request.POST['referal_code']
        starting_date = request.POST['starting_date']
        ending_date = request.POST['ending_date']
        # import current date and compare with end date 

        # if end date exceeds cureent date --> status = -1
        # if current date exceeds/grater than start date --> status = 1
        choice = request.POST['choice']
        if(choice == 'two'):
            o1_name = request.POST['field_one']
            o1_event = request.POST['event_code']
            o2_name = request.POST['field_two']
            o2_event = request.POST['event_code']
            o1 = Options(option_name=o1_name, event_code=o1_event)
            o2 = Options(option_name=o2_name, event_code=o2_event)
            o1.save()
            o2.save()
        if(choice == 'three'):
            o1_name = request.POST['field_one']
            o1_event = request.POST['event_code']
            o2_name = request.POST['field_two']
            o2_event = request.POST['event_code']
            o3_name = request.POST['field_three']
            o3_event = request.POST['event_code']
            o1 = Options(option_name=o1_name, event_code=o1_event)
            o2 = Options(option_name=o2_name, event_code=o2_event)
            o3 = Options(option_name=o3_name, event_code=o3_event)
            o1.save()
            o2.save()
            o3.save()
        if(choice == 'four'):
            o1_name = request.POST['field_one']
            o1_event = request.POST['event_code']
            o2_name = request.POST['field_two']
            o2_event = request.POST['event_code']
            o3_name = request.POST['field_three']
            o3_event = request.POST['event_code']
            o4_name = request.POST['field_four']
            o4_event = request.POST['event_code']
            o1 = Options(option_name=o1_name, event_code=o1_event)
            o2 = Options(option_name=o2_name, event_code=o2_event)
            o3 = Options(option_name=o3_name, event_code=o3_event)
            o4 = Options(option_name=o4_name, event_code=o4_event)
            o1.save()
            o2.save()
            o3.save()
            o4.save()
        if(choice == 'five'):
            o1_name = request.POST['field_one']
            o1_event = request.POST['event_code']
            o2_name = request.POST['field_two']
            o2_event = request.POST['event_code']
            o3_name = request.POST['field_three']
            o3_event = request.POST['event_code']
            o4_name = request.POST['field_four']
            o4_event = request.POST['event_code']
            o5_name = request.POST['field_five']
            o5_event = request.POST['event_code']
            o1 = Options(option_name=o1_name, event_code=o1_event)
            o2 = Options(option_name=o2_name, event_code=o2_event)
            o3 = Options(option_name=o3_name, event_code=o3_event)
            o4 = Options(option_name=o4_name, event_code=o4_event)
            o5 = Options(option_name=o5_name, event_code=o5_event)
            o1.save()
            o2.save()
            o3.save()
            o4.save()
            o5.save()
        if(choice == 'six'):
            o1_name = request.POST['field_one']
            o1_event = request.POST['event_code']
            o2_name = request.POST['field_two']
            o2_event = request.POST['event_code']
            o3_name = request.POST['field_three']
            o3_event = request.POST['event_code']
            o4_name = request.POST['field_four']
            o4_event = request.POST['event_code']
            o5_name = request.POST['field_five']
            o5_event = request.POST['event_code']
            o6_name = request.POST['field_six']
            o6_event = request.POST['event_code']
            o1 = Options(option_name=o1_name, event_code=o1_event)
            o2 = Options(option_name=o2_name, event_code=o2_event)
            o3 = Options(option_name=o3_name, event_code=o3_event)
            o4 = Options(option_name=o4_name, event_code=o4_event)
            o5 = Options(option_name=o5_name, event_code=o5_event)
            o6 = Options(option_name=o6_name, event_code=o6_event)
            o1.save()
            o2.save()
            o3.save()
            o4.save()
            o5.save()
            o6.save()
        user_email = request.POST['user_email']
        confirm_password = request.POST['confirm_password']
        # confirm_username = request.POST['confirm_username']
        if User.objects.get(password=confirm_password, email=user_email):
            u = User.objects.get(password=confirm_password, email=user_email)
            e = Events(event_name=event_name, event_code=event_code, referal_code=referal_code, hosted_by=u, event_description=event_description, starting_date=starting_date, ending_date=ending_date)
            e.save()
            msg_flag = 1    
    return render(request, 'voting_app/host_event_page.html', {'msg_flag': msg_flag})

def participate_to_vote(request):
    msg_flag = 0
    if request.method == 'POST':
        event_code = request.POST['event_code']
        referal_code = request.POST['referal_code']
        e = Events.objects.get(event_code=event_code, referal_code=referal_code)
        if e is not None:
            return redirect('event_page/'+e.event_code)
        else:
            msg_flag = -1
    return render(request, 'voting_app/participate_to_vote.html', {'msg_flag': msg_flag})

def event_page(request, event_code):
    event = Events.objects.get(event_code=event_code)
    options = Options.objects.filter(event_code=event_code)
    total_count = 1
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
    events = Events.objects.all()
    return render(request, 'voting_app/dashboard.html', {'events': events})
