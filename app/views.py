from django.shortcuts import render
import datetime

# Create your views here.

def index(request):
    context = {
        'number': 9,
        'string': 'software development practice day',
        'empty_string': '',
        'list': [
            {'name': 'zed', 'age': 19},
            {'name': 'amy', 'age': 22},
            {'name': 'joe', 'age': 31},
        ],
        'large_number': 123456789,
        'another_list': ['a', 'b', 'c'],
        'multilinestext': '''one
                            two
                            three''',
        
        'another_string': 'Software Development Practice Day',
        'time': datetime.datetime.now()
    }
    return render(request, 'app/index.html', context)