from django.shortcuts import render
from django.views.generic.base import TemplateView
from college.models import Branch,Notice,Question,Profile
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.http.response import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.
class HomeView(TemplateView):
    template_name = "college/index.html"

@method_decorator(login_required, name="dispatch")
class NoticeListView(ListView):
    model = Notice

    def get_queryset(self):
        si = self.request.GET.get("si")  # serch ke liye logic hai
        if si == None:
            si = ""
        if self.request.user.is_superuser:  # agar user super user hai to sare notice show ho nhi to jis brach ka user hai wahi notice show ho
            return Notice.objects.filter(Q(subject__icontains=si) | Q(msg__icontains=si)).order_by("-id")
        else:
            return Notice.objects.filter(Q(branch=self.request.user.profile.branch) | Q(branch__isnull=True)).filter(
                Q(subject__icontains=si) | Q(msg__icontains=si)).order_by("-id")


@method_decorator(login_required, name="dispatch")
class NoticeDetailView(DetailView):
    model = Notice

@method_decorator(login_required, name="dispatch")
class MyList(TemplateView): # jab mylist pe click hoga tab notice table ka data or questions table ka data dikhayega
    template_name = "college/mylist.html"
    def get_context_data(self, **kwargs):
        context = TemplateView.get_context_data(self, **kwargs)
        context["notices"] = Notice.objects.order_by("-id")[:3]     # context["notices"] iska matlab ki mylist.html fle me jo notices wala part hai waha notice table ka data dikhao
        context["questions"] = Question.objects.order_by("-id")[:3]  # context["questionss"] iska matlab ki mylist.html fle me jo questionss wala part hai waha question table ka data dikhao
        return context;

@method_decorator(login_required, name="dispatch")
class QuestionCreate(CreateView):
    model = Question
    fields = ["subject", "msg", "user_name"]

@method_decorator(login_required, name="dispatch")
class NoticeUpdateView(UpdateView):
    model = Question
    fields = ["subject","msg","user_name"]

@method_decorator(login_required, name="dispatch")
class NoticeDeleteView(DeleteView):
    model = Question


@method_decorator(login_required, name="dispatch")
class ProfileUpdateView(UpdateView):# update karne ke liye par iska html page  banega profile table hai usko update karna hai to profile_form.html agar hamare pass notice name ke tale ko update karna hota to notice_form.html ke nam se bnate
    model = Profile
    fields = ["branch", "sem", "marks_10", "marks_12", "marks_aggr", "rn"]
