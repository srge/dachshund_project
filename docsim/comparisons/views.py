from django.shortcuts import render, redirect

def get_results(request):
    if not 'HTTP_REFERER' in request.META:
        return redirect('/')

    return render(request, 'results.html')
