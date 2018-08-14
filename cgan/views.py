from django.shortcuts import render
from django.http import HttpResponse
from .models import *


CGAN_PAGE = 'cgan/cgan.html'


def gan_load(req):
    wanna_label = 1  # will be replaced with custom input

    if CGANInference(input_label=wanna_label).success:
        return render(req, CGAN_PAGE, {})
    else:
        return HttpResponse('<h1> CGAN Generation Failed... </h1>')


def about(req):
    return HttpResponse('<h1> GAN Benchmark! </h1>')
