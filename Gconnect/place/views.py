from django.shortcuts import render, redirect, get_object_or_404
from .import forms
from .models import Place


def places(request):
    login_id = request.session['logid']
    model_object = Place.objects.filter(login_id=login_id)

    if request.method == 'POST':
        form = forms.PlaceForms(request.POST, request.FILES)
        if form.is_valid():
            placeobj=form.cleaned_data
            placename=placeobj['name']
            p = Place(name=placename, login_id=login_id)
            p.save()
            return redirect('place:PlaceForms')
    else:
        form = forms.PlaceForms

    return render(request, "places/place.html", {'form': form, 'data': model_object})


def edit_place(request, pk):
    template = 'places/place.html'
    post = get_object_or_404(Place, pk=pk)
    model_object = Place.objects.all()
    if request.method == 'POST':
        form = forms.PlaceForms(request.POST, instance=post)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('place:PlaceForms')
    else:
        form = forms.PlaceForms(instance=post)
        context = {
            'form': form,
            'post': post,
            'data': model_object,
        }
    return render(request, template, context)


def delete_place(request, pk):
    post = get_object_or_404(Place, pk=pk)
    post.delete()
    return redirect('place:PlaceForms')
