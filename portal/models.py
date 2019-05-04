from django.db import models
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.db.models.signals import pre_save


ANSWER_TYPE_CHOICES = (('TX', 'Text'), ('MC', 'Multiple Choice'), ('MO', 'Multiple Options'))


class SurveyManager(models.Manager):

    def active(self):
        return super().filter(active=True)


class Survey(models.Model):
    name = models.CharField(max_length=32, unique=True)
    slug = models.SlugField(max_length=300, blank=True)
    headline = models.CharField(max_length=128)
    purpose = models.TextField()
    instructions = models.TextField()
    active = models.BooleanField(default=False)

    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('survey_detail', kwargs={'slug': self.slug})

    objects = SurveyManager()


def add_slug(sender, instance, *args, **kwargs):
    if instance.slug != slugify(instance.name):
        instance.slug = slugify(instance.name)
        instance.save()


pre_save.connect(add_slug, sender=Survey)


class Question(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=64)
    # answer_type = models.CharField(max_length=2, choices=ANSWER_TYPE_CHOICES)
    serial_number = models.PositiveSmallIntegerField(default=30)

    def __str__(self):
        return self.question_text

    @property
    def display_link(self):
        return "View"


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=32)

    def __str__(self):
        return "{} - {}".format(self.question.question_text, self.choice_text)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    choice = models.ForeignKey(Choice, on_delete=models.PROTECT)
    unique_id = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return "{} - {}".format(self.choice, self.unique_id)




