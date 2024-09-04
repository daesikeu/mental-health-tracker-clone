from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306165793',
        'name': 'Naila Zakiyyah Effendy',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)