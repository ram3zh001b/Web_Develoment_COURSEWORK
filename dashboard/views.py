from django.shortcuts import render

from dashboard.models import LogisticsData

# Create your views here.

def dashboard(request):

    context = {}

    # userdaata
    current_user = request.user
    context['user'] = current_user.username
    context['email'] = current_user.email
    fname = current_user.first_name
    lname = current_user.last_name
    context['name'] = fname + " " + lname

    # logistics data
    logistics = LogisticsData.objects.all().filter(studentId = current_user.id)
    context['logistics'] = logistics

    print(logistics)
    
    return render(request, 'dashboard/dashboard.html', context)