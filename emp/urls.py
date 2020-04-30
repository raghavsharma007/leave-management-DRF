from rest_framework import routers
from .views import EmployeeViewSet, ExecLeaveRequestViewSet, LeaveBalanceViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register('employee', EmployeeViewSet)
router.register('execleave', ExecLeaveRequestViewSet)
router.register('leavebalance', LeaveBalanceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
