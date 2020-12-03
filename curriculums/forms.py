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


class CreateCurriculumForm(forms.ModelForm):
    class Meta:
        model = models.Curriculum
        fields = (
            "title",
            "description",
            "created_date",
            "period",
            "budget",
            "related_skill",
            "education_background",
            "owner",
        )

    def save(self, *args, **kwargs):
        curriculum = super().save(commit=False)
        return curriculum


# from django import forms
# from . import models


# class CreateScheduleForm(forms.ModelForm):
#     class Meta:
#         model = models.Day
#         fields = ("title",)

#         def save(self):
#             review = super().save(commit=false)
#             return review