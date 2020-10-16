from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from lorem_text import lorem

# Create your views here.
def index(request):
    return render(request,'creative/index.html')


def random(request,word):
    print(word)
    text=lorem.words(word)
    print(text)
    return HttpResponse(text)

def loremtext(request):
    text="nothing"
    if request.method=="POST":
        words=int(request.POST.get('words',''))
        text=lorem.words(words)
    return render(request,'creative/lorem.html',{'text':text})