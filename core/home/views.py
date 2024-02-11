from django.shortcuts import render

from django.http import HttpResponse

def practice(request):

    peoples = [
        {'name' : 'Faiz', 'age' : 28},
        {'name' : 'Rakshit', 'age' : 25},
        {'name' : 'Nikhil', 'age' : 12},
        {'name' : 'Himanshu', 'age' : 26},
        {'name' : 'Binay', 'age' : 16}

    ]
    text = """
        Lorem ipsum dolor sit amet consectetur adipisicing elit. 
        Qui, totam numquam id aperiam animi doloribus voluptates reprehenderit, 
        impedit, omnis quo maxime aut nesciunt minus molestias commodi magnam quod 
        aliquid distinctio nulla dolor! Maxime, animi eligendi. Amet ipsam necessitatibus 
        molestias, fugit quo excepturi libero labore quam quos sapiente, nulla atque tempore.
        """
    
    vegetables = ['Pumpkin', 'Tomato', 'Potato']
    return render(request, "home/practice.html", context={'peoples_data' : peoples, 'text_lorem':text, 'vegetables_data':vegetables, 'pageName': 'Practice'})

def about(request):
    
    return render(request, "home/about.html", context={'pageName':'about'})

def home(request):
    return render(request, "home/index.html", context={'pageName':'home'})

def contacts(request):
    return render(request, "home/contacts.html", context={'pageName':'contacts'})

def success_page(request):
    print("*" * 10) # as we are not returning it as httpresponse so it will get printed in terminal only
    return HttpResponse("<h1> Hey this is a success page</h1>")
