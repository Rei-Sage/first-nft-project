from django.urls import path

from workspace import views

urlpatterns = [
    path('workspace/', views.workspace, name='workspace'),
    path('create',views.create,name='create'),
    path('update/<int:nft_id>/', views.update, name='update'),
    path('<int:nft_id>/',views.delete,name='delete'),

]