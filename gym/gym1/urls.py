from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.index,name='index'),
    path('member_list/',views.member_list,name="member_list"),
    path('add_member/',views.add_member,name="add_member"),
    path('edit_member/<int:id>',views.edit_member,name="edit_member"),
    path('delete_member/<int:id>',views.delete_member,name="delete_member"),
    path('membership_plans/',views.membership_plans,name="membership_plans"),
    path('payments_history/',views.payments_history,name="payments_history"),
    path('gym_schedule/',views.gym_schedule,name="gym_schedule"),
    path('trainers_list/',views.trainers_list,name="trainers_list"),
    path('add_trainer/',views.add_trainer,name="add_trainer"),
    path('edit_trainer/<int:id>',views.edit_trainer,name="edit_trainer"),
    path('add_equipment/',views.add_equipment,name="add_equipment"),
    path('edit_equipment/<int:id>',views.edit_equipment,name="edit_equipment"),
    path('equipment-list/', views.equipment_list, name='equipment_list'),
    path('signup/', views.signup, name='signup'),
     path('login/', views.user_login, name='login'),
]
