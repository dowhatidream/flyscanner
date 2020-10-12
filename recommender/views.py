from django.shortcuts import render
from .models import Country
import pandas as pd
import numpy as np
import glob
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import time
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
from scipy import spatial
import operator
import csv


def index(request):
    countries = Country.objects.all()
    return render(request, 'recommender/index.html', {
        'index': countries
    })


def detail(request, cID):
    country = Country.objects.get(pk=cID)
    get_file()
    return render(request, 'recommender/detail.html', {
        'detail': country
    })


def get_file():
    df_rating = pd.read_csv('recommend/jupyter/data/person_dataset.csv')
    df = pd.read_csv('recommend/jupyter/data/person_dataset2.csv')
    df_country = pd.read_csv('recommend/jupyter/data/country_dataset.csv')
    df_country = df_country.fillna(0)
    for a in df_country:
        print(a)

