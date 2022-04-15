"""
views for home app
"""
# pylint: disable=no-member
from django.shortcuts import render
from django.views import generic, View
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
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


class AddNewQuestion(CreateView):
    '''
    class view in get - gets the traffic_msg_form and in post - posts the form
    and creates new traffic alert
    '''
    template_name = 'questions/add_question.html'
    form_class = QuestionForm
    success_url = 'questions'

    def get(self, request, *args, **kwargs):

        return render(
            request,
            'questions/add_question.html',
            {
                'form': QuestionForm()
            },
        )

    def post(self, request, *args, **kwargs):

        form = QuestionForm(data=request.POST)
        if form.is_valid():
            form.instance.author_id = request.user.id

            question = form.save(commit=False)
            question.save()

        else:
            form = QuestionForm(instance=form)

        return HttpResponseRedirect('questions')