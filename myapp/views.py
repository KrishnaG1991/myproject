from django.shortcuts import render

# Create your views here.
import logging

from django.http import HttpResponse

logger = logging.getLogger(__name__)


def index(request):
    logger.info("Index page accessed")
    return HttpResponse("Hello, world!")


def about(request):
    try:
        result = 1 / 0
    except Exception as e:
        logger.exception(f'Error in about page: {e}')
        return HttpResponse("Oops, somthing went wrong.")
    else:
        logger.debug("About page accessed")
    return HttpResponse("This is the about page")
