from django.shortcuts import render,redirect
from showdata.models import applyleave
from .forms import leaveformvarify
from .forms import detailForm
from managementsystem.models import extendemp
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .import sms_send

@login_required(login_url='login')
def logadmin(request):
    data_fatch = applyleave.objects.all()
    return render(request,'admin_home.html',{'datavalue':data_fatch})

@login_required(login_url='login')
def datail(request,id):
    data_fatch = applyleave.objects.get(pk=id)
    users = data_fatch.user
    more_detail = extendemp.objects.get(user=users)
    return render(request,'detail.html',{'value1':data_fatch,'value2':more_detail})

@login_required(login_url='login')
def verified(request,id):
    verified_data = applyleave.objects.get(pk=id)
    verified_data.varify = True
    verified_data.save()
    username = verified_data.user
    user = User.objects.get(username=username)
    email = user.email
    first_name = user.first_name
    last_name = user.last_name
    send_mail(
                'subject- Leave Applications', 
                'Respected ADMINISTRATOR'+'\n'+first_name + last_name +'\n'+'applied for a leave.Your Application to be varified.','pawankrmandal121@gmail.com'
               , 
                [
                    email
                ],
                fail_silently=True
            )
    sms_send.sendPostRequest(URL, 'FTONPEX5ZD1RBT2GG1DF7SGRWWMKSJWM', '95BEYU97I3HSFJPL', 'stage', '8603587194', 'RIZVI', 'Applied for a leave' )
    
    return  redirect('logadmin')

@login_required(login_url='login')
def emp_list(request):
    employee = User.objects.all()
    return render(request,'all_emp.html',{'users':employee})

@login_required(login_url='login')
def pending_leave(request):
    data_fatch = applyleave.objects.all()
    return render(request,'admin_pending.html',{'datavalue':data_fatch})

@login_required(login_url='login')
def approve_leave(request):
    data_fatch = applyleave.objects.all()
    return render(request,'admin_approved.html',{'datavalue':data_fatch})

