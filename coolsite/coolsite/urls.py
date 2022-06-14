"""coolsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from cgitb import handler

from coolsite import settings
from django.urls import path, include # Функция include позволяет импрортировать url-адреса прямо из приложения,
# чтобы они были независимыми друг от друга

from women.views import pageNotFound

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('women.urls')), # Прописываем url-адрес для каждой функции
]

# Добавляем специальные настройки для подгрузки статических файлов на момент продакшена. Указываем URL подгрузки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Обработчик исключений для страницы 404 при выключенном DEBUG
handler404 = pageNotFound
