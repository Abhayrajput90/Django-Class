from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def login(req):
    # return HttpResponse('<h1>This Is Index Page</h1>')
    usersData = [
        {
            "name" : "Chirag",
            "age" : 15,
            "city" : "Ratlam",
            "phone" : 9876543210
        },
        {
            "name" : "Abhay",
            "age" : 19,
            "city" : "Sehore",
            "phone" : 9876543210
        },
        {
            "name" : "Vinod",
            "age" : 20,
            "city" : "Indore",
            "phone" : 987654388210
        },
        {
            "name" : "Subham",
            "age" : 18,
            "city" : "Bhopal",
            "phone" : 98763783210
        },
    ]
    # return render(req,"index.html",context={"users": usersData, "tittle":"Django Project"})
    tems = loader.get_template("login.html")
    return HttpResponse(tems.render({'users':usersData}))

def About(req):
    return HttpResponse('<h1>This Is About Page</h1>')