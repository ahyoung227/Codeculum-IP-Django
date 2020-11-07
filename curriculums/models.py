from django.db import models
from core import models as core_models
from users import models as user_models
from django.urls import reverse


class AbstractItem(core_models.TimeStampedModel):

    title = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Skill(AbstractItem):

    pass


class Curriculum(core_models.TimeStampedModel):

    """ Curriculum Model definition """

    EDUCATION_COMPUTERSCIENCE = "computer science"
    EDUCATION_STEMFIELD = "STEM field"
    EDUCATION_NONSTEM = "Non STEM field"

    EDUCATION_CHOICES = (
        (EDUCATION_COMPUTERSCIENCE, "computer science"),
        (EDUCATION_STEMFIELD, "STEM field"),
        (EDUCATION_NONSTEM, "Non STEM field"),
    )

    title = models.CharField(max_length=140)
    description = models.TextField()
    created_date = models.DateField()
    period = models.IntegerField()
    budget = models.IntegerField()
    related_skill = models.ManyToManyField(Skill, related_name="skill", blank=True)
    education_background = models.CharField(
        choices=EDUCATION_CHOICES, max_length=30, null=True
    )
    owner = models.ForeignKey(
        user_models.User,
        related_name="curriculums",
        on_delete=models.CASCADE,
        null=True,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("curriculums:detail", kwargs={"pk": self.pk})

    # def save(self, *args, **kwargs):
    #     self.city = str.capitalize(self.title)
    #     super().save(*args, **kwargs)
