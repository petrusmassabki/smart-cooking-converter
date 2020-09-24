from django.shortcuts import render, get_object_or_404
from .models import Ingredient
from .conversion import mass_to_utensils


def index(request):

    ingredients = Ingredient.objects.all().order_by('ingredient_name')

    data = {
        'ingredients': ingredients,
    }

    return render(request, 'cooking_converter_app/index.html', data)


def result(request):

    request1 = request.GET.get('ingredient')
    request2 = request.GET.get('grams')
    request3 = request.GET.get('utensils')

    if request1 and request2 and request3:
        utensils = request.GET.getlist('utensils')
        ingredient = get_object_or_404(Ingredient, pk=request.GET['ingredient'])
        conversion_result = mass_to_utensils(float(request.GET['grams']),
                                             float(ingredient.bulk_density),
                                             utensils)
        utensils_result, grams_result, error_msg = conversion_result
    else:
        utensils_result = ''
        ingredient = ''
        grams_result = ''
        error_msg = ''

    data = {
        'ingredient': ingredient,
        'grams': request.GET['grams'],
        'grams_result': grams_result,
        'utensils_result': utensils_result,
        'error_msg': error_msg,
    }

    return render(request, 'cooking_converter_app/result.html', data)


def data(request):

    ingredients = Ingredient.objects.all().order_by('ingredient_name')

    data = {
        'ingredients': ingredients,
    }

    return render(request, 'cooking_converter_app/data.html', data)
