from django.shortcuts import render
from django.http import FileResponse, Http404

# Create your views here.


def index(request):

    return render(request, 'index.html')


def pdf_view(request):
    try:
        return FileResponse(open('file.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()
