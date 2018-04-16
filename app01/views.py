from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from app01.models import Area


def index(request):
    print('index')
    # print('aa'+ Null)
    return HttpResponse('hello')


def show_static(request):
    return None


def add_user(request):

    return render(request, 'app01/add_user.html')


def show_page(request, page_num):
    areas = Area.objects.filter(parent_id=1)
    paginator = Paginator(areas,10)
    page = paginator.page(page_num)
    datas = {
        'page':page,
    }
    return render(request, 'app01/show_page.html', datas)


def show_areas(request):
    # 查询所有省份的数据
    areas = Area.objects.filter(parent_id=1)
    # print(areas)
    context = {
        'areas':areas
    }
    return render(request, 'app01/show_areas.html', context)


def get_children(request, children_id):
    city = Area.objects.filter(parent_id=children_id)
    print(city)
    context = {
        'city':city
    }
    return JsonResponse(context)