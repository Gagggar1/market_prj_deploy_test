from django.shortcuts import render
from .models import Accommodation
from django.shortcuts import get_object_or_404
from .models import ListOfCountries

# Create your views here.

# 1 обеспечить визуализацию стартовой страницы нашего веб-приложения


def main(request):
    return render(request, 'mainapp/index.html')


# 2 контроллер должен обеспечить нам отображение страницы со списком всех
# продуктов компании:


def accommodations(request):
    title = 'размещение'
    list_of_accommodations = Accommodation.objects.filter(is_active=True)
    content = {
        'title': title,
        'list_of_accommodations': list_of_accommodations}
    return render(request, 'mainapp/accommodations.html', content)

# контроллер, обеспечивающий визуализацию страницы с детальной информацией
# о каждом предложении нашего турагентства:


def accommodation(request, pk):
    title = 'продукты'
    content = {
        'title': title,
        'accommodation': get_object_or_404(
            Accommodation,
            pk=pk)}
    return render(request, 'mainapp/accommodation_details.html', content)
