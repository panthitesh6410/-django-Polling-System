
import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Enquiry, Events, Options, Transactions
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

def compare_dates(d1, d2):
    d1_y = d1.year
    d1_m = d1.month
    d1_d = d1.day
    d2_y = d2.year
    d2_m = d2.month
    d2_d = d2.day
    if d1_y > d2_y:
        return d1
    elif d1_y < d2_y:
        return d2
    else:
        if d1_m > d2_m:
            return d1
        elif d1_m < d2_m:
            return d2
        else:
            if d1_d > d2_d:
                return d1
            elif d1_d < d2_d:
                return d2

def host_event_page(request):
    msg_flag = -1
    if request.method == 'POST':
        msg_flag = 0
        event_name = request.POST['event_name']
        event_description = request.POST['event_description']
        event_code = request.POST['event_code']
        referal_code = request.POST['referal_code']
        starting_date = request.POST['starting_date']
        starting_date_processing = starting_date.replace('T', '-').replace(':', '-').split('-')
        starting_date_processing = [int(v) for v in starting_date_processing]
        starting_date_processing_out = datetime.datetime(*starting_date_processing)
        ending_date = request.POST['ending_date']
        ending_date_processing = ending_date.replace('T', '-').replace(':', '-').split('-')
        ending_date_processing = [int(v) for v in ending_date_processing]
        ending_date_processing_out = datetime.datetime(*ending_date_processing)
        # import current date
        curr_date = datetime.datetime.now()
        event_status = 0
        # compare current date with starting and ending date :
        # if curr_date > start_date && curr_date > end_date --> event_status=-1
        if compare_dates(curr_date, starting_date_processing_out)==curr_date and compare_dates(curr_date, ending_date_processing_out)==curr_date:
            event_status = -1 
        # if curr_date < start_date && curr_date < end_date --> event_status=1
        elif compare_dates(curr_date, starting_date_processing_out)==starting_date_processing_out and compare_dates(curr_date, ending_date_processing_out)==ending_date_processing_out:
            event_status = 1 
        # if curr_date > start_date && curr_date < end_date --> event_status=0
        elif compare_dates(curr_date, starting_date_processing_out)==curr_date and compare_dates(curr_date, ending_date_processing_out)==ending_date_processing_out:
            event_status = 0 
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
        # confirm_username = request.POST['confirm_username
        if User.objects.get(password=confirm_password, email=user_email):
            u = User.objects.get(password=confirm_password, email=user_email)
            e = Events(event_name=event_name, event_code=event_code, event_status=event_status, referal_code=referal_code, hosted_by=u, event_description=event_description, starting_date=starting_date, ending_date=ending_date)
            e.save()
            msg_flag = 1    
    return render(request, 'voting_app/host_event_page.html', {'msg_flag': msg_flag})

def participate_to_vote(request):
    flag = 0
    msg_flag = 0
    if request.method == 'POST':
        uname = request.POST['uname']
        password =  request.POST['password']
        event_code = request.POST['event_code']
        referal_code = request.POST['referal_code']
        u = User.objects.get(username=uname, password=password)
        e = Events.objects.get(event_code=event_code, referal_code=referal_code) 
        if e is None:
            msg_flag = -1
        else:
            trans = Transactions.objects.filter(voter=u, event_code=event_code, referal_code=referal_code) 
            if trans:
                flag = -1
            else:
                return redirect('event_page', event_code)
    return render(request, 'voting_app/participate_to_vote.html', {'msg_flag': msg_flag, 'flag': flag})

def event_page(request, event_code):
    event = Events.objects.get(event_code=event_code)
    starting_date_processing_out = event.starting_date
    ending_date_processing_out = event.ending_date
    curr_date = datetime.datetime.now()
    event_status = 0
    if compare_dates(curr_date, starting_date_processing_out)==curr_date and compare_dates(curr_date, ending_date_processing_out)==curr_date:
        event_status = -1 
    elif compare_dates(curr_date, starting_date_processing_out)==starting_date_processing_out and compare_dates(curr_date, ending_date_processing_out)==ending_date_processing_out:
        event_status = 1 
    elif compare_dates(curr_date, starting_date_processing_out)==curr_date and compare_dates(curr_date, ending_date_processing_out)==ending_date_processing_out:
        event_status = 0 
    event.event_status = event_status
    event.save()  
    options = Options.objects.filter(event_code=event_code)
    total_count = 0
    percs = []
    for option in options:
        total_count += option.count
    # for option in options:
    #     per = (option.count*100) / total_count
    #     percs.append(per)
    max_vote = 0
    winner = ''
    for option in options:
        if option.count > max_vote:
            max_vote = option.count
            winner = option.option_name
    msg_flag = 0
    if request.method == 'POST':
        option_name = request.POST['option']
        email = request.POST['email']
        password = request.POST['password']
        u = User.objects.get(email=email, password=password)
        t = Transactions.objects.filter(voter=u, event_code=event.event_code, referal_code=event.referal_code)
        if t.exists():
            msg_flag = -1
        else:
            tr = Transactions(voter=u, option_name=option_name, event_name=event.event_name, event_code=event.event_code, referal_code=event.referal_code)
            tr.save()
            # increment count by 1 :
            op = Options.objects.get(option_name=option_name, event_code=event_code)
            op.count = op.count + 1
            op.save()
            msg_flag = 1
    return render(request, 'voting_app/event_page.html', {'event_code': event_code, 'event': event, 'total_count': total_count, 'options': options, 'percs': percs, 'winner': winner, 'msg_flag': msg_flag})

def view_event(request, event_code):
    event = Events.objects.get(event_code=event_code)
    starting_date_processing_out = event.starting_date
    ending_date_processing_out = event.ending_date
    curr_date = datetime.datetime.now()
    event_status = 0
    if compare_dates(curr_date, starting_date_processing_out)==curr_date and compare_dates(curr_date, ending_date_processing_out)==curr_date:
        event_status = -1 
    elif compare_dates(curr_date, starting_date_processing_out)==starting_date_processing_out and compare_dates(curr_date, ending_date_processing_out)==ending_date_processing_out:
        event_status = 1 
    elif compare_dates(curr_date, starting_date_processing_out)==curr_date and compare_dates(curr_date, ending_date_processing_out)==ending_date_processing_out:
        event_status = 0 
    event.event_status = event_status
    event.save()  
    options = Options.objects.filter(event_code=event_code)
    total_count = 0
    percs = []
    for option in options:
        total_count += option.count
    # for option in options:
    #     per = (option.count*100) / total_count
    #     percs.append(per)
    max_vote = 0
    winner = ''
    for option in options:
        if option.count > max_vote:
            max_vote = option.count
            winner = option.option_name
    return render(request, 'voting_app/view_event.html', {'event_code': event_code, 'event': event, 'total_count': total_count, 'options': options, 'percs': percs, 'winner': winner})


def dashboard(request):
    events = Events.objects.all()
    transactions = Transactions.objects.all()
    return render(request, 'voting_app/dashboard.html', {'events': events, 'transactions': transactions})
