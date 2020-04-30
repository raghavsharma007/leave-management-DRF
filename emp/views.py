from django.shortcuts import render
from .serializers import EmployeeSerializer, ExecLeaveRequestSerializer, LeaveBalanceSerializer
from rest_framework import viewsets, permissions
from .models import Employee, ExecLeaveRequest, LeaveBalance

class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    # permission_classes = (permissions.IsAuthenticated,)

class ExecLeaveRequestViewSet(viewsets.ModelViewSet):
    serializer_class = ExecLeaveRequestSerializer
    queryset = ExecLeaveRequest.objects.all()
    # permission_classes = (permissions.IsAuthenticated,)

class LeaveBalanceViewSet(viewsets.ModelViewSet):
    serializer_class = LeaveBalanceSerializer
    queryset = LeaveBalance.objects.all()
    # permission_classes = (permissions.IsAuthenticated,)