from django.shortcuts import render,redirect
from .models import employee
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import leaveform
from .forms import extendForm
from .forms import userForm
from .models import applyleave
from managementsystem.models import extendemp
from django.core.mail import send_mail
from .import sms_send


# Create your views here.
@login_required(login_url='login')
def show(request):
    form = leaveform()
    data_fatch = applyleave.objects.all()
    user = User.objects.filter(username=request.user)

    if request.method == 'POST':
        form = leaveform(request.POST)
        data = form.save(commit=False)
        new_user = request.user
        data.user = new_user
        user = User.objects.get(username=new_user)
        email = user.email
        first_name = user.first_name
        last_name = user.last_name
        URL = 'https://www.sms4india.com/api/v1/sendCampaign'
        send_mail(
                'subject- Leave Applications', 
                'Respected ADMINISTRATOR'+'\n'+first_name + last_name +'\n'+'applied for a leave.You can interact with the particular request on the application!', email
               , 
                [
                    'pawankrmandal121@gmail.com'
                ],
                fail_silently=True
            )
        #print(email)        
        sms_send.sendPostRequest(URL, 'FTONPEX5ZD1RBT2GG1DF7SGRWWMKSJWM', '95BEYU97I3HSFJPL', 'stage', '8603587194', 'RIZVI', 'Applied for a leave' )
        data.save()
        return redirect(emp_all_leave)

    return render(request,'employee_home.html',{'rows':form,'datavalue':data_fatch})



@login_required(login_url='login')
def profile(request):
    if request.method == 'GET':
        user = request.user
        employee = extendemp.objects.get(user=user)
        form = extendForm(instance=employee)
        employee_name = User.objects.get(username=user)
        form_name =  userForm(instance=employee_name)
        return render(request,'empprofile.html',{'form':form,'form1':form_name})
    else:
        user = request.user
        employee = extendemp.objects.get(user=user)
        form = extendForm(request.POST, instance=employee)
        form.save()
        employee_name = User.objects.get(username=user)
        form_name =  userForm(request.POST, instance=employee_name)
        form_name.save()

        return redirect('show')   
    
    
##======================================
@login_required(login_url='login')
def emp_all_leave(request):
    log_user = request.user
    data_fatch = applyleave.objects.filter(user=log_user)
    return render(request,'emp_all_leave.html',{'datavalue':data_fatch})


@login_required(login_url='login')
def pendingleave(request):
    log_user = request.user
    data_fatch = applyleave.objects.filter(user=log_user)
    return render(request,'pending_leave.html',{'datavalue':data_fatch})


@login_required(login_url='login')
def confirmleave(request):
    log_user = request.user
    data_fatch = applyleave.objects.filter(user=log_user)
    return render(request,'approved.html',{'datavalue':data_fatch})
    