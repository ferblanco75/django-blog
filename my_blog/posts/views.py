from django.views.generic.base import View
from django.shortcuts import render
from django.http import HttpResponse

class HelloWorld(View):
    def get(self, request):
        data = {
            'name': 'Fernando Blanco',
            'years': 48,
            'codes': ['Python', 'Php', 'React', 'Haskell']
        }
        return render(request, 'hello_world.html', context=data)