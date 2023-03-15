from django.shortcuts import render
from django.http import HttpResponse
from googletrans import Translator

def tools(request):
    return render(request, 'tools.html')

def translator(request):
    return render(request, 'translator.html')

def translated(request):
    text= request.GET.get('text')
    lang= request.GET.get('lang')
    print('text:',text,'lang:', lang)
    translator= Translator()
    dt= translator.detect(text)
    dt2=dt.lang
    translated=translator.translate(text, lang)
    tr=translated.text
    return render(request, 'translated.html', {'translated':tr, 'u_lang':dt2, 't_lang':lang})

def analyze(request):
    djtext = request.GET.get('text', 'default')
    fullcaps = request.GET.get('fullcaps', 'off')
    if(fullcaps=="off"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
       
        return render(request, 'analyze.html', params)
def counter(request):
     mess=request.GET['message']
     w1=mess.split()
     return render(request,'counter.html',{'msg':mess,"length": len(w1)})