from django.urls import path
from django.conf.urls import url
from . import views

app_name = "firstapp" 

urlpatterns = [
    path('',views.vista,name='vista'),
    path('dogs',views.dogs,name='dogs'),
    path('dog/add',views.dogsAdd,name='dogsAdd'),
    path('dog/delete',views.dogsDelete,name='dogsdelete'),
    path('dog/get',views.dogsGet,name='dogsGet'),
    path('dog/get/<int:dogid>',views.dogsGetId,name='dogsGetId'),
    path('dog/update/<int:dogid>',views.dogsUpdate,name='dogsUpdate'),
    path('types',views.types,name='types'),
    #############################################
    # path('teams',views.teams,name='teams'),
    # path('teams/add',views.teamsAdd,name='teamsAdd'),
    # #path('teams/delete/<int:idteam>',views.teamsDelete,name='teamsdelete'),
    # #url(r'^teams/delete/(?P<iddelete>\d+)/$',views.teamsDelete, name='teamsdelete'),
    # path('teams/delete/<int:iddelete>', views.teamsDelete, name='teamsdelete'),
    # path('teams/get',views.teamsGet,name='teamsGet'),
    # path('teams/get/<int:teamid>',views.teamsGetId,name='teamsGetId'),
    # path('confederation',views.confederation,name='confederation'),
    # path('editar/<int:idedit>',views.editar,name='editar'),
    # #url(r'^teams/editar/(?P<idedit>\d+)/$',views.editar, name='editar'),
    # path('add',views.add,name='add'),
    # path('eliminar/<int:iddelete>/<str:nameteam>',views.eliminar,name='eliminar'),

    ###############################################

    path('gpus',views.gpus,name='gpus'),
    path('gpu/add',views.gpusAdd,name='gpusAdd'),
    path('gpu/delete/<int:id>',views.gpusDelete,name='gpusDelete'),
    path('agregar',views.agregar,name='agregar'),
    path('eliminar/<int:id>/<str:gpu>',views.eliminar,name='eliminar'),
    path('editar/<int:id>',views.editar,name='editar')
    
    # path('gpu/get',views.gpusGet,name='gpusGet'),
    # path('gpu/get/<int:gpuid>',views.gpusGetId,name='gpusGetId')
    
]
