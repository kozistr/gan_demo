from django.shortcuts import render
from django.http import HttpResponse
from .models import *


CGAN_PAGE = 'cgan/cgan.html'


def gan_load(req):
    wanna_label = 1  # will be replaced with custom input

    CGANInference(input_label=wanna_label)

    return render(req, CGAN_PAGE, {})


def about(req):
    return HttpResponse('<h1> GAN Benchmark! </h1>')
