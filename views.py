# i created this - Prathamesh R. Pawar

from django.http import HttpResponse
from django.shortcuts import render

def index (request):
    dict1 = {'name':'ruturaj','relation':'brother'}
    return render(request,'index.html',dict1)

def analyze(request):
    # get the text and analyze text
    global analyzeupper
    djtext = request.POST.get('text', 'default')     #TEXT INPUTTED BY USER WILL GO TO DJTEXT

    # check box functions
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    newlineremover = request.POST.get('newlineremover','off')
    charcounter = request.POST.get('charcounter','off')
    readaloud = request.POST.get('readaloud','off')
    numdetails = request.POST.get('numdetails','off')
    #essayproject = request.POST.get('essayproject','off')

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Changed To UPPERCASE','analyzed_text':analyzed}
        djtext = analyzed
        #return render(request,'analyze.html ',params)


    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            # here you can use (if not arguments ) to make it more simple
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char

        params = {'purpose':'Extra Space Removed','analyzed_text':analyzed}
        djtext = analyzed
        #return render(request,'analyze.html',params)

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char !="\r":
                analyzed = analyzed + char
            else:print("no")
        print("pre",analyzed)
        params = {'purpose':'New Lines Removed','analyzed_text':analyzed}
        djtext = analyzed
        #return render(request,'analyze.html',params)

    if charcounter == "on":
        analyzedchar = len(djtext)
        word_list = djtext.split()
        analyzedword = len(word_list)
        analyzed = f"Total Characters = {analyzedchar} And Total Words Count = {analyzedword}"
        params = {'purpose':'Charcounter','analyzed_text': analyzed}
        djtext = analyzed
        #return render(request,'analyze.html',params)

    if removepunc == "on" and fullcaps == "on":
        punctuations =  '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations :
                analyzed = analyzed + char.upper()
        params =  {'purpose':'Remove Punctuations And Uppercase All','analyzed_text':analyzed.upper()}
        djtext = analyzed
        #return render(request,'analyze.html',params)

    if readaloud == "on":
        import pyttsx3
        user = pyttsx3.init()
        user.say(djtext)
        user.runAndWait()
        params = {'purpose':'Read Text','analyzed_text':(djtext)}
        djtext = analyzed
        #return  render(request,'analyze.html',params)

    if numdetails == "on":
        import phonenumbers
        from phonenumbers import timezone
        from phonenumbers import geocoder,carrier
        number = phonenumbers.parse(djtext)
        zone = timezone.time_zones_for_number(number)
        provider = carrier.name_for_number(number, 'en')
        region = geocoder.description_for_number(number, 'en')
        analyzed = {"Initial Timezone":zone,"Network Provider":provider,"Country or Region":region}
        params = {'purpose':'Phone Number Details','analyzed_text':analyzed}
    if (numdetails != "on" and readaloud != "on" and removepunc != "on" and charcounter !="on" and extraspaceremover != "on" and newlineremover != "on" and fullcaps != "on"):
        return render(request,'error.html')

    return render(request, 'analyze.html', params)






    # elif essayproject == "on":
    # import pywhatkit
    # analyzed = pywhatkit.info(f"{djtext}",10)# fstrings
    # params = {'purpose':'Text Project Information ','analyzed_text':analyzed}
    # return  render(request,'analyze.html',params)










    #return HttpResponse("analyze <a href = '/'>  <br>Back to home</a>")








#def capitalizefirst(request):
#    return HttpResponse("Capitalizefirst <a href = '/'> <br>Back to home</a>")
#def newlineremove(request):
#    return HttpResponse("Newlineremove  <a href = '/'> <br>Back to home</a>")
#def spaceremover(request):
#    return HttpResponse("ok")
#d#ef charcount(request):
#    return HttpResponse()
#def about(request):
#    return HttpResponse("about world ")


