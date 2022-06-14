from django.urls import path, re_path

from .views import index, categories, archive, about  # импортируем функции представления


urlpatterns = [
    path('', index, name='home'), # для каждого адреса будет добавляться префикс women, так как мы указали его в главном url.py проекта
    #path('cats/<int:catid>/', categories), # добавляем числовой параметр для перехода по категориям по шаблону <тип данных: имя>
    #re_path(r'^archive/(?P<year>[0-9]{4})/', archive), # формируем url-адрес с помощью регулярного выражения
    path('about/', about, name='about'),
]
