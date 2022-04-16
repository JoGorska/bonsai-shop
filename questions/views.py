"""
views for home app
"""
# pylint: disable=no-member
from django.shortcuts import render, redirect, reverse
from django.views import generic, View
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Question
from .forms import QuestionForm


class QuestionsList(generic.ListView):
    """
    view to display all questions paginated
    """
    model = Question
    queryset = Question.objects.filter(status=1).order_by('-created_on')
    template_name = 'questions/questions.html'
    paginate_by = 10


def add_question(request):
    """
    Add questions to FAQ page
    """

    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES)

        print(f'form alone {form}')

        if form.is_valid():
            question = form.save()
            messages.success(request, 'Successfully added your question!')
            return redirect(reverse('questions'))
        else:
            messages.error(request, 'Failed to add question.\
                                     Please ensure the form is valid')
    else:
        form = QuestionForm()

    template = 'questions/add_question.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
