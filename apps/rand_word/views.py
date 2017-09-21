from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.

def index(request):

    print request

    if 'number' not in request.session:
        request.session['number'] = 0

    request.session['number'] += 1
    rand_word = {
        "word": get_random_string(14)
    }
    return render(request, 'rand_word/index.html', rand_word)

def reset(request):
    print request
    request.session.clear()
    return redirect('/')