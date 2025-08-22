#i have created this file shary

from django.http import HttpResponse

from django.shortcuts import render

def index(request):
    #render have three parameters 1.request,2. templatename,3.dictionaray pass
    dict={"Name":"Shary","City":"Peshawer"}
    return render(request,"temp.html")

# def About(request):
#     return HttpResponse("About Shahriyar khan")

# def personal_n(request):
#     print(request.GET.get("text","default"))
#     return HttpResponse("Personal_n")


def analyzed(request):
    #get the text
    djtext=request.POST.get('Input_text','default')
    removepunc=request.POST.get("removpunc",'Off')
    capitals=request.POST.get("capitalyze",'Off')
    remove_n_l=request.POST.get("removenewline",'Off')
    remove_E_S=request.POST.get("rms",'Off')

    puncuations=(""" .,?!:;'"()[]{}-–.../\&*#%$€£@ """)

    if removepunc=="on":
        analyzed_text=""
        for char in djtext:
            if char not in puncuations:
                analyzed_text+=char
        parameter={"purpose":"Remove Punctuation","analyzed_text":analyzed_text}
        djtext=analyzed_text
    
    if capitals=="on":
        analyzed_text=""
        for char in djtext:         
                analyzed_text=analyzed_text+char.upper()
        parameter={"purpose":"Uppercase","analyzed_text":analyzed_text}
        djtext=analyzed_text
    
    if remove_E_S == "on":
        analyzed_text = ""
        index=len(djtext)
        for idx, char in enumerate(djtext):
           if not(djtext[idx] == " " and djtext[index+1]==" "):
                analyzed_text += char

        parameter = {"purpose": "Remove Extra Spaces", "analyzed_text": analyzed_text}
        djtext=analyzed_text
    
    if remove_n_l=="on":
        analyzed_text=""
        for char in djtext:
                if char !="\n" and char!="\r":         
                    analyzed_text=analyzed_text+char
        parameter={"purpose":"Remove new line","analyzed_text":analyzed_text}
    
    if(removepunc != "on" and remove_n_l!="on" and remove_E_S!="on" and capitals!="on"):
        return HttpResponse("please select any operation and try again")
    return render(request,"analyz.html",parameter)

        
