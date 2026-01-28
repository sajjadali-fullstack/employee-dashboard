from django.urls import path
from . import views
urlpatterns = [
    path('<int:id>/',views.employee_detail_view, name='employee_details'),
    path('add/', views.add_employee_view, name='add_employee'),
    path('edit/<int:pk>/', views.edit_employee_view, name='edit_employee'),
    path('delete/<int:pk>/', views.delete_employee, name='delete_employee'),

]