from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306245844',
        'name': 'Ammara Fasha Zia',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)