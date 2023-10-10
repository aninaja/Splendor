from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    template_name = 'dashboard.html'
    context = {
        'transactions': 'test',
    }
    return render(request, template_name, context)
