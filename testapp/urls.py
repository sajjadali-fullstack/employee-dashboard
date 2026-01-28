from django.urls import path
from . import views
urlpatterns = [
    path('<int:id>/',views.employee_detail_view, name='employee_details'),
    path('add/', views.add_employee_view, name='add_employee')
]