from django.http import Http404
from django.views.generic import ListView

# from django.urls import reverse
from . import models
from django.shortcuts import render

# from django.http import HttpResponse
# from math import ceil
# from django.core.paginator import Paginator, EmptyPage


class HomeView(ListView):
    """ Homeview Definition """

    model = models.Curriculum
    paginate_by = 10
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
