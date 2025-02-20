from django.shortcuts import render

# Create your views here.
def login(request):
    if request.method ==  'Post':
        username = request.Post['username']
        password = request.Post['password'] 