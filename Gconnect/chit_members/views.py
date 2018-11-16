from django.shortcuts import render,get_object_or_404
from chit_details.models import ChitDetails


def chit_memb(request, pk):
    post = get_object_or_404(ChitDetails, pk=pk)
    model_object = ChitDetails.objects.filter(chit_name_id=pk)
    request.session['amount'] =pk

    return render(request, "chit_memb/memberlist.html", {'data': model_object})
