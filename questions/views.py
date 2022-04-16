"""
views for home app
"""
# pylint: disable=no-member
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import generic, View
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Question
from .forms import QuestionForm


class QuestionsList(generic.ListView):
    """
    view to display all questions paginated
    """
    model = Question
    queryset = Question.objects.filter(status=1).order_by('-created_on')
    template_name = 'questions/questions.html'
    paginate_by = 3


@login_required
def questions_manager(request):
    """
    view to display all unpublished questions
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only the store owners can do that.')
        return redirect(reverse('questions'))

    question_list = Question.objects.filter(status=0).order_by('-created_on')
    template = 'questions/questions.html'

    context = {
        'question_list': question_list,
    }

    return render(request, template, context)


@login_required
def add_question(request):
    """
    Add questions to FAQ page
    """

    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES)

        if form.is_valid():
            question = form.save()
            messages.success(request, 'Successfully added your question!\
                            Response will be published within 2 working days')
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


