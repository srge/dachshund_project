from django.shortcuts import render, redirect
from comparisons.models import Comparison

def home_page(request):
    if request.method == 'POST':
        comparison = Comparison()
        comparison.doc_a = request.POST.get('doc_a', '')
        comparison.doc_b = request.POST.get('doc_b', '')

        if comparison.doc_a and comparison.doc_b:
            comparison.save()
            context = {'test':'test',}

            return redirect('/results/')
        else:
            return redirect('/')

    return render(request, 'base.html')
