from django.shortcuts import render
from main_function import Test

# Create your views here.

def main(request):
    if request.method == "GET":
        word=(request.GET.get('search'))
        if str(word).strip() != '' and word != None:
            word= str(word).strip()
            content= Test().dummy(word)
            content['line'] = True
            print(word, len(word))
            return render(request,'home.html', content)
        
    return render(request,'home.html')