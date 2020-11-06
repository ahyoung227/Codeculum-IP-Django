from django.shortcuts import render
from django.http import HttpResponse
from . import models


def all_curriculums(request):
    all_curriculums = models.Curriculum.objects.all()
    return render(
        request,
        "/Users/ahyoungkim/coding/IP_project/templates/curriculums/all_curriculums.html",
        context={"curriculums": all_curriculums},
    )
