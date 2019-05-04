from django.conf.urls import url
from . import views

urlpatterns = [

    # url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^$', views.home, name='home'),
    url('survey/details/(?P<slug>[\w-]+)/$', views.SurveyDetailView.as_view(), name='survey_detail'),
    url('survey/start/$', views.survey_start, name='survey_start'),

]
