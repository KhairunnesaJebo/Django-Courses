from django.shortcuts import render, redirect
from . import forms

# Create your views here.
def add_category(request):
    if request.method == 'POST': # user post request koreche
        category_form = forms.CategoryForm(request.POST) # user er post request data ekhane capture korlam
        if category_form.is_valid(): # post kora data gula amra valid kina check korechi
            category_form.save() # jodi data valid hoi tahole database e save korbo
            return redirect('add_category') # sob thik thakle etake add category ei url e pathiye dibo
    else: # user normally website e gele blank form pabe
        category_form = forms.CategoryForm()
    return render(request, 'add_category.html', {'form': category_form})
