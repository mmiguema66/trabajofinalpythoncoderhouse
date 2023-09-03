from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name="home" ),
    path('clientes/', clientes, name="clientes"),
    path('marcas/', marcas, name="marcas"),
    
    path('cliente_form/', clienteForm, name="cliente_form"),
    path('cliente_form2/', clienteForm2, name="cliente_form2" ),

    path('update_cliente/<id_cliente>/', updateCliente, name="update_cliente" ),
    path('delete_cliente/<id_cliente>/', deleteCliente, name="delete_cliente" ),
    path('create_cliente/', createCliente, name="create_cliente" ),

    path('update_marca/<id_marca>/', updateMarca, name="update_marca" ),
    path('delete_marca/<id_marca>/', deleteMarca, name="delete_marca" ),
    path('create_marca/', createMarca, name="create_marca" ),

    path('patentes/', PatenteList.as_view(), name="patentes" ),
    path('create_patente/', PatenteCreate.as_view(), name="create_patente" ),    
    path('update_patente/<int:pk>/', PatenteUpdate.as_view(), name="update_patente" ),
    path('delete_patente/<int:pk>/', PatenteDelete.as_view(), name="delete_patente" ),

    path('problemas/', ProblemaList.as_view(), name="problemas" ),
    path('create_problema/', ProblemaCreate.as_view(), name="create_problema" ),    
    path('update_problema/<int:pk>/', ProblemaUpdate.as_view(), name="update_problema" ),
    path('delete_problema/<int:pk>/', ProblemaDelete.as_view(), name="delete_problema" ),

    path('login/', login_request, name="login" ),
    path('logout/', LogoutView.as_view(template_name="aplicacion/logout.html"), name="logout" ),
    path('registro/', register, name="registro" ),
     path('registro/', register, name="registro" ),
    path('editar_perfil/', editarPerfil, name="editar_perfil" ),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar" ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



