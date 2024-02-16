from django.shortcuts import render
# Create your views here.


def home_view(request):
    return render(request, 'index.html')
    
def error_404(request, exception):
    return render(request, '404.html')