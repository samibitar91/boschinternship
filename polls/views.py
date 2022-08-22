from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Choice, Question
from django.utils import timezone


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
           ).order_by('-pub_date')[:5]

"""
displays a question text, with no results but with a form to vote.
"""
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

"""
displays results for a particular question
"""
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

"""
 handles voting for a particular choice in a particular question
"""
def vote(request, question_id):
    ... # same as above, no changes needed.