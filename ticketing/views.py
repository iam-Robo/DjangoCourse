from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from ticketing.models import Movie, Cinema


def movie_list(request):
    movies = Movie.objects.all()
    context = {
        'movie_list1' : movies
    }
    return render(request,'movie_list.html',context)

def cinema_list(request):
    cinemas = Cinema.objects.all()
    response_text = """
    <!DOCTYPE html>
        <html dir=rtl>
        <head>
        <title>لیست سینماها</title>
        </head>
        <body style="background-color:#4d79ff;">
        <h1 ><span style="color:#9400D3">فهرست سینماهای</span><span style="color: transparent;text-shadow: none;">&nbsp;</span><span style="color:#4B0082">کشور</span></h1>
        <ul style="font-family:tahoma;color:#000099"> {} </ul>
        </body>
        </html>
        """.format(''.join('<h4><li>{}</li></h4>'.format(item) for item in cinemas))
    return HttpResponse(response_text)