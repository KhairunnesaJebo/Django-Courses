from django.shortcuts import render
import datetime

# Create your views here.

def home(request):
    d = {'author' : 'Tushar', 'age': 18, 'birthday': datetime.datetime.now(), 'value': '12', 'str': 'dear ing peu', 'lst': ['python','is','Language'], 'courses': [
        {
            'id': 1,
            'name': 'Python',
            'fee': 5000
        },
        {
            'id': 2,
            'name': 'Django',
            'fee': 8000
        },
        {
            'id': 1,
            'name': 'C',
            'fee': 3000
        }
    ]}
    return render(request, 'home.html', d)