from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, Http404

from .models import Women

# Create your views here.

menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']


def index(request): #HttpRequest
    # return HttpResponse('Страница приложения women.')

    posts = Women.objects.all()

    return render(request, 'women/index.html', {'menu': menu, 'title': 'Главная страница',
                    'posts': posts}) # используем функцию render, чтобы загрузить шаблон


def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'О сайте'})


# Вторым аргументом в функцию передаем параметр catid, который отвечает за переход по категориям
# Этот параметр так же указываем в urls.py для данного приложения
def categories(request, catid):
    # Проверям, есть ли данные в GET запросе
    if request.GET:
        print(request.GET) # отлавливаем GET запрос

    return HttpResponse(f'<h1>Статьи по категориям</h1><p>{catid}</p>')


def archive(request, year):
    # Генерируем ошибку 404 в другой функции. Произойдет перенаправление на функцию pageNotFound
    # if int(year) > 2020:
    #     raise Http404()

    # Создаем редирект (перенаправление)
    if int(year) > 2020:
        return redirect('home', permanent=True) # по умолчанию генерится редирект с кодом 302, который говорит, что адрес страницы поменялся временно
        # постоянный редирект можно сгенерить с помощью доп. параметра permanent (тогда код ответа будет 301)

    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')


# Функция обработчик исключения для ошибки 404, должна принимать 2 аргумента
def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
