from django.urls import path
from . import views
from django.views.generic import TemplateView
urlpatterns = [
    path('tienda', views.tienda, name='tienda'),
    #path('login', views.login, name='login'),
    path('registroUsuarios', views.registroUsuarios, name='registroUsuarios'),
    path('carrito', views.carrito, name='carrito'),
    path('producto', views.producto, name='producto'),
    path('adminProductos', views.admin_productos, name='adminProductos'),
    path('test', views.test, name='test'),

	path('sucursalAjax', views.sucursalAjax, name='sucursalAjax'),
	path('sucursalAjaxResponse', views.sucursalAjaxResponse, name='sucursalAjaxResponse'),

	path('', views.sucursalApiFetch, name='sucursalApiFetch'),
	path('sucursalApiFetch', views.sucursalApiFetch, name='sucursalApiFetch'),
    path('sw.js',TemplateView.as_view(template_name='sw.js', content_type='application/javascript'),name='sw.js'),

]