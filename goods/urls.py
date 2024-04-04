from django.urls import path

from goods import views

# необходимо указать имя приложения для пространства имён (namespace), чтобы не было ошибки
app_name = 'goods'

# первый аргумент в path - это адрес конкретной страницы,
# второй аргумент - регистрация представления, которое будет закреплено за этим адресом
# третий аргумент - для тегов в html-документах, чтобы можно было обращаться к этим ссылкам по имени
urlpatterns = [
    # путь для страницы с каталогом товаров
    path('', views.catalog, name='index'),
    # путь для страницы конкректного товара
    path('product/', views.product, name='product'),
]