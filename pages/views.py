from django.shortcuts import render
from django.utils.datetime_safe import datetime
#from django.http import HttpResponse

# Create your views here.


def home_view(request):
    # def home_view(request, *args, **kwargs):
    #print(args, kwargs)
    # print(request.user)
    return render(request, "index.html")


def template_tags_filters_view(request):
    data = {
        1: {
            'id': 1,
            'slug': 'test-slug-1',
            'name': 'Test Name 1'
        },
        2: {
            'id': 2,
            'slug': 'test-slug-2',
            'name': 'Test Name 2'
        }
    }
    values = ['Python','Python','Python','Ruby','Java','JavaScript','JavaScript','C','C++','C++','C++','C#']
    dict_values=[{'name':'Milon', 'language': 'Python'},
                {'name':'alim', 'language': 'Ruby'},
                {'name':'Mily', 'language': 'Ruby'},
                {'name':'Asha', 'language': 'Python'},
                {'name':'Munmun', 'language': 'JavaScript'}]
    
    cities = [
    {'name': 'Dhaka', 'population': '19,000,000', 'country': 'Bangladesh'},
    {'name': 'Rajshahi', 'population': '15,000,000', 'country': 'Bangladesh'},
    {'name': 'New York', 'population': '20,000,000', 'country': 'USA'},
    {'name': 'Chicago', 'population': '7,000,000', 'country': 'USA'},
    {'name': 'Tokyo', 'population': '33,000,000', 'country': 'Japan'},
    ]
    books=[
    {'title': '1984', 'author': {'name': 'George', 'age': 45}},
    {'title': 'Timequake', 'author': {'name': 'Kurt', 'age': 75}},
    {'title': 'Alice', 'author': {'name': 'Lewis', 'age': 33}},
    ]

    context = {
        'title': 'title title',
        'my_text': 'this is about page.',
        'this_is_true': True,
        'my_number': 123.456789,
        'my_list': [456, 789, 159, 357, "ABC"],
        'my_html': "<h1>Hello world</h1>",
        'points': [(1, 2, 3), (4, 5, 6)],
        'data': data,
        'empty_list': [],
        'filters_list':[1,2,3,"abc",4,5,6,"def",7,8,9,"ghi",10,11,12,"jkl"],
        'values':values,
        'dict_values':dict_values,
        'cities':cities,
        'first':[1,2,3],
        'second':[4,5,6],
        'addslashes':"I'm using Django.",
        'capfirst1':'capfirst capitalizes the charecter of the value.',
        'capfirst2':' 0 capfirst capitalizes the charecter of the value.',
        'center':"Django",
        'datetime': datetime.now(),
        'books':books,
        'url':"https://www.facebook.com/abdulalim.milon.71/",
        'email':"alim.abdul.5915@gmail.com",
        'yes':True,
        'no':False,
        'none':None
    }
    return render(request, "template_tags_filters.html", context)
