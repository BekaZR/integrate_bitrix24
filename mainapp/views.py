from django.shortcuts import render

from mainapp.forms import LinkForm


def linkview(request):
    if request.method == "POST":
        form = LinkForm(request.POST)
        form.is_valid()
    else:
        form = LinkForm()
    return render(request, "mainapp/index.html", {"form": form})
