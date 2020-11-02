from django.urls import path
from .views import (
    AllgroupsListView,
    AllgroupsUpdateView,
    AllgroupsDetailView,
    AllgroupsDeleteView,
    AllgroupsCreateView,
    AllgroupsTestView,
    )

urlpatterns = [
    path('<int:pk>/edit/', AllgroupsUpdateView.as_view(), name='allgroups_edit'),
    path('<int:pk>/', AllgroupsDetailView.as_view(), name='allgroups_detail'),
    path('<int:pk>/delete/', AllgroupsDeleteView.as_view(), name='allgroups_delete'),
    path('new/', AllgroupsCreateView.as_view(), name='allgroups_new'),
    path('test/', AllgroupsTestView.as_view(), name='allgroups_test'),
    path('', AllgroupsListView.as_view(), name='allgroups_list'),
    ]
