from django.shortcuts import render

# Create your views here.
def noninjas(request):
    return render(request, 'ninjas/noninjas.html')


def noninjas(request):
    return render(request, 'ninjas/show_all.html')


def showaninja(request, color):
    ninja_color = {
        'blue' : 'Leonardo',
        'orange' : 'Michelangelo',
        'red' : 'Raphael',
        'purple' : 'Donatello'
    }
    if color in ninja_color:
        filename = ninja_color[color]
    else:
        filename = 'megan_fox'
    return render(request, 'ninjas/showaninja.html', {'filename': filename})
