from django.shortcuts import render, redirect, get_object_or_404
from comparisons.models import Comparison
from core.consensus import Consensus
import re


def home_page(request):
    msg=''

    if 'HTTP_REFERER' in request.META:
        referer = request.META['HTTP_REFERER']
        referer = re.sub('^https?:\/\/', '', referer).split('/')
        if len(referer) == 2:
            msg='Please submit both doc a and doc b'


    if request.method == 'POST':
        comparison = Comparison()
        comparison.doc_a = request.POST.get('doc_a', '')
        comparison.doc_b = request.POST.get('doc_b', '')

        if comparison.doc_a and comparison.doc_b:
            comparison.save()

            return redirect(get_results, id_c=comparison.id)

        else:
            notify = "You must submit both doc a and doc b"
            return redirect(home_page)

    return render(request, 'base.html', {'msg':msg})


def get_results(request, id_c=1):
    if not 'HTTP_REFERER' in request.META:
        return redirect('/')

    comparison = Comparison.objects.order_by('-id')[0]
    consensus = Consensus(comparison.doc_a, comparison.doc_b)
    results = consensus.get_consensus()

    return render(request, 'results.html', {
            'doc_a': comparison.doc_a,
            'doc_b': comparison.doc_b,
            'jac': results['jac'],
            'sor': results['sor'],
            'ham': results['ham'],
            'lev': results['lev'],
            'cos': results['cos'],
            'var': results['var']
        })
