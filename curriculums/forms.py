from django import forms
from . import models


class SearchForm(forms.Form):

    title = forms.CharField(initial="Any", required=False)
    budget = forms.IntegerField(initial="All", required=False)
    period = forms.IntegerField(required=False)
    education_background = forms.ChoiceField(
        choices=models.Curriculum.EDUCATION_CHOICES, required=False
    )
    related_skill = forms.ModelMultipleChoiceField(
        required=False,
        queryset=models.Skill.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
