from django.shortcuts import render


def index(request):
    return render(request, 'projects/index.html', {})


# about
def about(request):
    return render(request, "projects/about.html", {})