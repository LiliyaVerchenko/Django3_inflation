from django.shortcuts import render
from django.conf import settings
import csv


def inflation_view(request):
    template_name = 'inflation.html'
    context = {}

    # чтение csv-файла и заполнение контекста
    with open(settings.INFLATION_RUSSIA_FILE, 'r', newline='', encoding='utf8') as file:
        reader = csv.DictReader(file, delimiter=";")
        data = list(reader)
        context = {'rows': data}

    return render(request, template_name, context)
