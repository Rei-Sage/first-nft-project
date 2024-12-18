
from django.urls import path, include
from .views import *

urlpatterns = [
    path('detail/<int:id>',detail,name='detail'),
    path('wallet/',wallet,name='wallet'),
    path('ranking/',ranking,name='ranking'),
    path('marketplace',market,name='market'),
    path('',creator,name='creator'),
]