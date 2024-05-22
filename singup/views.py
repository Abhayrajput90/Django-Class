from django.shortcuts import render
from django.http import HttpResponse
def index(req):
     return HttpResponse('<h1>This Is Index Page</h1>')
    #  return render(req,"index.html",context={"users": usersData, "tittle":"Django Project"})