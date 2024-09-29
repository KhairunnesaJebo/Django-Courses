from django.shortcuts import render
import datetime

# Create your views here.

def home(request):
    abc = {
        'name': 'jebo', 'age': 26, 'num': 121, 'str': "This isn't my Home",
        'lstNum': [3, 1, 8, 6], 'lstStr': ['Django', 'is', 'exciting'], 'timeNow': datetime.datetime.now(), 'val': "", 'lst': [
            {'name': 'tushi', 'age': 21}, 
            {'name': 'himi', 'age': 17}, 
            {'name': 'koli', 'age': 25},], 
        'title': 'You &lt;i>are&lt;/i&gt Good &amp Beautiful!',
        'intro': 'Hey, my name is janna.\nI am a programmar.\nNice to meet you!',
        'var': ['States', ['Kansas', ['Lawrence', 'Topeka'], 'Illinois']],
         'birthdate': datetime.datetime(1998, 7, 10),
         'btn': '<b>He</b> is <em>my</em> <button>husband</button>',
         'num_message': 4,
    }
    return render(request, 'home.html', abc)