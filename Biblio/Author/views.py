from django.shortcuts import render

# Create your views here.
def show_author(request):
    return render(request, 'Author/main.html')