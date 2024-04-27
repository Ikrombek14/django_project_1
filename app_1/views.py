from django.shortcuts import render
from django.http import HttpResponse


def first(request):
    html="""
        <h1>First Page</h1>
        <a href="second/">Second Page</a>
    
    """
    return HttpResponse(html)

def second(request):
    html="""
        <h1>Second Page</h1>
        <a href="../">First Page</a>
    
    """
    return HttpResponse(html)

def pages(request, page):
    html=f"""
        <h1>Page {page}</h1>
        <a href="../">First Page</a>
    """
    return HttpResponse(html)