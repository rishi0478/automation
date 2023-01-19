from django.urls import path
from . import views

urlpatterns = [
    path('',views.func,name='search'),
    path('table1',views.Table_NoOpener,name='noopener'),
    path('table2',views.Table,name='without_noopener'),
    path('delete_t',views.Delete_table,name='delete_table'),
    path('delete_t2',views.Delete_table2,name='delete_table2')
]
