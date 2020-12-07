from django.http import Http404
from django.core.paginator import Paginator
from django.views.generic import ListView, View, UpdateView, FormView
from django.shortcuts import render, redirect, reverse
from users import mixins as user_mixins
from django.contrib import messages
from . import models, forms


# from schedules import forms as schedule_forms


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
        return render(
            request,
            "curriculums/detail.html",
            {"curriculum": curriculum},
        )
    except models.Curriculum.DoesNotExist:
        raise Http404()


class SearchView(View):

    """ Searchview Definition """

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
                    filter_args["period__lte"] = period

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
        # "created_date",
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
        messages.success(self.request, "Curriculum Uploaded")
        return redirect(reverse("curriculums:detail", kwargs={"pk": curriculum.pk}))


class CreateDayView(user_mixins.LoggedInOnlyView, FormView):

    form_class = forms.CreateScheduleForm
    template_name = "curriculums/day_create.html"

    def form_valid(self, form):
        day = form.save()
        day.owner = self.request.user
        day.save()
        form.save_m2m()
        return redirect(reverse("curriculums:detail", kwargs={"pk": day.pk}))
