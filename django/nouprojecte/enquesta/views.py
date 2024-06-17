from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Opcio, Pregunta

class IndexView(generic.ListView):
    template_name = "enquesta/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Pregunta.objects.order_by("-data_publicacio")[:5]

class DetailView(generic.DetailView):
    model = Pregunta
    template_name = "enquesta/detail.html"

class ResultsView(generic.DetailView):
    model = Pregunta
    template_name = "enquesta/results.html"

def vote(request, question_id):
    question = get_object_or_404(Pregunta, pk=question_id)
    try:
        selected_choice = question.opcio_set.get(pk=request.POST["choice"])
    except (KeyError, Opcio.DoesNotExist):
        return render(
            request,
            "enquesta/detail.html",
            {
                "question": question,
                "error_message": "No ha selecció cap opció.",
            },
        )
    else:
        selected_choice.vots += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("enquesta:results", args=(question.id,)))
