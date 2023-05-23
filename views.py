# created by me

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # params = {'name':'sasidha', 'planet': 'Earth'}
    return render(request, 'index2.html')
    # return HttpResponse("HELLO FOLKS!!")


# def about(request):
#     return HttpResponse("about folks....")


def analyze(request):
    # get the text
    djtext = request.POST.get('text', 'default')
    #check checkbox values
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    lineremover = request.POST.get('lineremover','off')
    spaceremover = request.POST.get('spaceremover','off')
    # print(removepunc)
    # print(djtext)
    # analyze the text
    # return HttpResponse("remove punctuation")

    #checking the on checkbox
    if removepunc=='on':
        analyzed=""
        punctuations = '''!@#$%^&*()><:;?|\}{][`~'''
        for char in djtext:
            if char not in punctuations:
                analyzed+=char
        params={'purpose':'Removed punctuations','analyzed_text':analyzed}
        djtext=analyzed
        # return render(request,'analyze2.html',params)

    if fullcaps=='on':
        analyzed=""
        for char in djtext:
            analyzed+=char.upper()
        params={'purpose':'changed to upper case','analyzed_text':analyzed}
        djtext=analyzed
        # return render(request,'analyze2.html',params)

    if lineremover=='on':
        analyzed=""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed+=char
            else: print("no")
        print("pre",analyzed)
        params={'purpose':'Removed new lines','analyzed_text':analyzed}
        djtext=analyzed
        # return render(request,'analyze2.html',params)

    if spaceremover=='on':
        analyzed=""
        # for char in djtext:
        #     if char!='\t':
        #         analyzed+=char
        for index,char in enumerate(djtext):
            if not (djtext[index]=='' and djtext[index+1]==''):
                analyzed+=char
        params={'purpose':'Removed space between words','analyzed_text':analyzed}
        djtext = analyzed

    if(removepunc!='on' and fullcaps!='on' and lineremover!='on' and spaceremover!='on'):
        return HttpResponse("ERROR:( ENTER ANY FUNCTION & TRY AGAIN")

    return render(request,'analyze2.html',params)

    # else:
    #     return HttpResponse("ERROR!!")


# def exercise1(request):
#     ex='''<h1>CREATING THE PAGE</h1></br>
#        <h2>Links for pages</h2></br>
#        <a href="https://facebook.com/">FACEBOOK</a></br>
#        <a href="https://instagram.com/">INSTAGRAM</a></br>
#        <a href="https://youtube.com/">YOUTUBE</a></br>
#     '''
#     return HttpResponse(ex)

# def capfirst(request):
#     return HttpResponse("capitalize first")
# def newlineremove(request):
#     return HttpResponse("newline remove first")
# def spaceremove(request):
#     return HttpResponse("space remover <a href='/'>back</a>")
# def charcount(request):
#     return HttpResponse("charcount")