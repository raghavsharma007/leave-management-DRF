from rest_framework import serializers
from .models import Employee, ExecLeaveRequest, LeaveBalance

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class ExecLeaveRequestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ExecLeaveRequest
        fields = '__all__'

class LeaveBalanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LeaveBalance
        fields = '__all__'