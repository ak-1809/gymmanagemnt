from django.shortcuts import render
from django.http import HttpResponse
from .models import Subscriber
from .forms import MemberForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Subscriber
from django.shortcuts import render
from .models import MembershipPlan
from django.shortcuts import render
from .models import Payment
from django.shortcuts import render
from .models import Member, Attendance
from .models import Trainer
from .forms import TrainerForm
from .models import GymEquipment
from .forms import EquipmentForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login


# Create your views here.



def index(request):
    return render(request, 'gym1/index.html')


def member_list(request):
    members = Member.objects.all()
    return render(request, 'gym1/member_list.html', {'members': members})



def add_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('member_list')
    else:
        form = MemberForm()

    return render(request, 'gym1/add_member.html', {'form': form})


def edit_member(request, id):
    member = get_object_or_404(Member, id=id)

    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('member_list')
    else:
        form = MemberForm(instance=member)

    return render(request, 'gym1/edit_member.html', {'form': form})



def delete_member(request, id):
    member = get_object_or_404(Member, id=id)

    if request.method == 'POST':
        member.delete()
        return redirect('member_list')

    return render(request, 'gym1/delete_member.html', {'member': member})


def membership_plans(request):
    plans = MembershipPlan.objects.all()
    return render(request, 'gym1/membership_plans.html', {'plans': plans})



def payments_history(request):
    payments = Payment.objects.all()
    return render(request, 'gym1/payments_history.html', {'payments': payments})


def attendance(request):
    members = Member.objects.all()
    if request.method == 'POST':
        date = request.POST.get('attendance_date')
        for member in members:
            attendance_status = request.POST.get(str(member.id), False)
            attendance_obj, created = Attendance.objects.get_or_create(member=member, date=date)
            attendance_obj.attendance_status = attendance_status
            attendance_obj.save()

    return render(request, 'gym1/attendance.html', {'members': members})



def gym_schedule(request):
    # Add code to fetch the gym schedule from the database or any other data source
    schedule = [
        {'day': 'Monday', 'time': '9:00 AM - 11:00 AM', 'activity': 'Yoga'},
        {'day': 'Tuesday', 'time': '6:00 PM - 7:30 PM', 'activity': 'Zumba'},
        # Add more schedule items as needed
    ]

    return render(request, 'gym1/gym_schedule.html', {'schedule': schedule})




def trainers_list(request):
    trainers = Trainer.objects.all()
    return render(request, 'gym1/trainers_list.html', {'trainers': trainers})




def add_trainer(request):
    if request.method == 'POST':
        form = TrainerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trainers_list')
    else:
        form = TrainerForm()

    return render(request, 'gym1/add_trainer.html', {'form': form})


def edit_trainer(request, id):
    trainer = get_object_or_404(Trainer, id=id)

    if request.method == 'POST':
        form = TrainerForm(request.POST, instance=trainer)
        if form.is_valid():
            form.save()
            return redirect('trainers_list')
    else:
        form = TrainerForm(instance=trainer)

    return render(request, 'gym1/edit_trainer.html', {'form': form})



def equipment_list(request):
    equipment = GymEquipment.objects.all()
    return render(request, 'gym1/equipment_list.html', {'equipment': equipment})



def add_equipment(request):
    if request.method == 'POST':
        form = EquipmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipment_list')
    else:
        form = EquipmentForm()

    return render(request, 'gym1/add_equipment.html', {'form': form})



def edit_equipment(request, id):
    equipment = get_object_or_404(GymEquipment, id=id)

    if request.method == 'POST':
        form = EquipmentForm(request.POST, instance=equipment)
        if form.is_valid():
            form.save()
            return redirect('equipment_list')
    else:
        form = EquipmentForm(instance=equipment)

    return render(request, 'gym1/edit_equipment.html', {'form': form})

def equipment_list(request):
    equipment = GymEquipment.objects.all()
    return render(request, 'gym1/eipment_list.html', {'equipment': equipment})



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect or handle successful signup
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'gym1/signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Redirect or handle successful login
            return redirect('index')  # Redirect to home page or any other page
    else:
        form = AuthenticationForm()

    return render(request, 'gym1/login.html', {'form': form})
