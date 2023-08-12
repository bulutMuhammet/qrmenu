from django.shortcuts import render

# Create your views here.
from home.models import Category


def index(request):
    categories = Category.objects.all()
    lang = request.GET.get('lang')
    if not lang:
        lang = request.session.get('lang')
    if lang == "en":
        request.session['lang'] = "en"
    else:
        request.session['lang'] = "tr"
    return render(request, "index.html", {'categories': categories, 'lang': lang})

def category(request, id):
    category = Category.objects.get(id=id)
    lang = request.GET.get('lang')
    if not lang:
        lang = request.session.get('lang')
    if lang == "en":
        request.session['lang'] = "en"
    else:
        request.session['lang'] = "tr"
    return render(request, "category.html", {'category': category, 'lang': lang})