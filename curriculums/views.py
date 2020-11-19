from django.http import Http404
from django.core.paginator import Paginator
from django.views.generic import ListView, View, UpdateView, FormView
from django.shortcuts import render, redirect, reverse
from users import mixins as user_mixins
from django.contrib import messages
from . import models, forms

# from django.urls import reverse
# from django.http import HttpResponse
# from math import ceil
# from django.core.paginator import Paginator, EmptyPage


# class LoginView():
#     """ """


class HomeView(ListView):
    """ Homeview Definition """

    model = models.Curriculum
    paginate_by = 12
    ordering = "created"
    paginate_orphans = 5
    page_kwarg = "page"
    context_object_name = "curriculums"


def curriculum_detail(request, pk):
    try:
        curriculum = models.Curriculum.objects.get(pk=pk)
        return render(request, "curriculums/detail.html", {"curriculum": curriculum})
    except models.Curriculum.DoesNotExist:
        raise Http404()


class SearchView(View):
    def get(self, request):

        title = request.GET.get("title")

        if title:

            form = forms.SearchForm(request.GET)

            if form.is_valid():

                title = form.cleaned_data.get("title")
                period = form.cleaned_data.get("period")
                budget = form.cleaned_data.get("budget")
                related_skill = form.cleaned_data.get("related_skill")
                education_background = form.cleaned_data.get("education_background")

                filter_args = {}

                filter_args["title__startswith"] = title

                if budget is not None:
                    filter_args["budget__lte"] = budget

                if period is not None:
                    filter_args["period__gte"] = period

                for s in related_skill:
                    filter_args["related_skill"] = s

                if education_background is not None:
                    filter_args["education_background"] = education_background

                qs = models.Curriculum.objects.filter(**filter_args).order_by(
                    "-created"
                )

                #  = models.Curriculum.objects.filter(**filter_args).order_by(
                #     "-created"
                # )
            else:
                paginator = Paginator(qs, 10, orphans=5)
                page = request.GET.get("page", 1)
                curriculums = paginator.get_page(page)

                return render(
                    request,
                    "curriculums/search.html",
                    {"form": form, "curriculums": curriculums},
                )

        else:
            form = forms.SearchForm()

        return render(
            request,
            "curriculums/search.html",
            {"form": form},
        )


class EditCurriculumView(user_mixins.LoggedInOnlyView, UpdateView):

    model = models.Curriculum
    template_name = "curriculums/curriculum_edit.html"
    fields = {
        "title",
        "description",
        "created_date",
        "period",
        "budget",
        "related_skill",
        "education_background",
        "owner",
    }

    def get_object(self, queryset=None):
        curriculum = super().get_object(queryset=queryset)
        if curriculum.owner.pk != self.request.user.pk:
            raise Http404()
        return curriculum


class CreateCurriculumView(user_mixins.LoggedInOnlyView, FormView):

    form_class = forms.CreateCurriculumForm
    template_name = "curriculums/curriculum_create.html"

    def form_valid(self, form):
        curriculum = form.save()
        curriculum.owner = self.request.user
        curriculum.save()
        form.save_m2m()
        messages.success(self.request, "Room Uploaded")
        return redirect(reverse("curriculums:detail", kwargs={"pk": curriculum.pk}))

    # # skill = request.GET.get("skill")
    # # skill = str.capitalize(skill)
    # budget = int(request.GET.get("budget", 0))
    # period = int(request.GET.get("period", 0))
    # s_related_skills = request.GET.getlist("related_skills")
    # form = {
    #     # "skill": skill,
    #     "budget": budget,
    #     "period": period,
    #     "s_related_skills": s_related_skills,
    # }

    # related_skills = models.Skill.objects.all()

    # choices = {"related_skills": related_skills}

    # filter_args = {}

    # if budget != 0:
    #     filter_args["budget__lte"] = budget

    # if period != 0:
    #     filter_args["period__gte"] = period

    # if len(s_related_skills) > 0:
    #     for s_related_skill in s_related_skills:
    #         filter_args["related_skill__pk"] = int(s_related_skill)

    # curriculums = models.Curriculum.objects.filter(**filter_args)


# def all_curriculums(request):
#     page = request.GET.get("page", 1)
#     curriculum_list = models.Curriculum.objects.all()
#     paginator = Paginator(curriculum_list, 10, orphans=5)
#     try:
#         curriculums = paginator.page(int(page))
#         return render(
#             request,
#             "/Users/ahyoungkim/coding/IP_project/templates/curriculums/all_curriculums.html",
#             {"curriculums": curriculums}
# context={
#     "curriculums": all_curriculums,
#     "page": page,
#     "page_count": page_count,
#     "page_range": range(1, page_count),
# },
#     )
# except EmptyPage:
#     curriculums = paginator.page(1)
#     return redirect("/")
# page = int(request.GET.get("page", 1))
# page = int(page or 1)
# page_size = 10
# limit = page_size * page
# offset = limit - page_size
# all_curriculums = models.Curriculum.objects.all()[offset:limit]
# page_count = ceil(models.Curriculum.objects.count() / page_size)
