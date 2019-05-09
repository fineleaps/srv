from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, DetailView
from .models import Survey, Question, Choice, Answer
from django.http import Http404
from django.forms import formset_factory, modelformset_factory


def home(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    print(ip)
    context = {'surveys': Survey.objects.active()}
    return render(request, 'portal/home.html', context)

# class HomeView(TemplateView):
#     template_name = 'portal/home.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data()
#         context['surveys'] = Survey.objects.active()
#         return context


# def survey_start(request):
#     AnswerModelFormset = modelformset_factory(Answer, fields=('choice', ), extra=4)
#     formset = AnswerModelFormset(request.POST or None)
#     if formset.is_valid():
#         formset.save()
#     context = {'formset': formset}
#     return render(request, 'portal/survey_start.html', context)


class SurveyDetailView(DetailView):
    template_name = 'portal/survey_detail.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'survey'

    model = Survey

    def get_object(self, queryset=None):
        survey = super().get_object(queryset=queryset)
        if not survey.active:
            raise Http404('Invalid Request')
        return survey


def survey_start(request, slug):
    survey = get_object_or_404(Survey, slug=slug, active=True)
    if request.method == "POST":
        pass
    else:
        questions = survey.question_set.all()
        return render(request, 'portal/survey_start.html', {'questions': questions, 'survey': survey})


    #
    # AnswerModelFormset = modelformset_factory(Answer, fields=('choice', ), extra=4)
    # formset = AnswerModelFormset(request.POST or None)
    # if formset.is_valid():
    #     formset.save()
    # context = {'formset': formset}
    # return render(request, 'portal/survey_start.html', context)
