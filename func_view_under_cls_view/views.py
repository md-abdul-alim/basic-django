from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
# Create your views here.
from .forms import CourseModelForm
from .models import Course


class CourseCreateView(View):
    template_name = "coursese/course_create.html"
    # GET method

    def get(self, request, *args, **kwargs):
        form = CourseModelForm()
        context = {"form": form}
        return render(request, self.template_name, context)

    # POST method
    def post(self, request, *args, **kwargs):
        form = CourseModelForm(request.POST)
        if form.is_valid():
            form.save()
            form = CourseModelForm()  # after submiting form this will bring to the blank form again
        context = {"form": form}
        return render(request, self.template_name, context)


class CourseListView(View):
    template_name = "coursese/course_list.html"
    queryset = Course.objects.all()

    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwargs):
        context = {'object_list': self.get_queryset()}  # or self.queryset
        return render(request, self.template_name, context)

# # perticular ekta fixed id ke CourseListView teke nia asbe search kore dia show kora jabe
# class MyListView(CourseListView):
#     queryset = Course.objects.filter(id=1)


class CourseObjectMixin(object):
    model = Course
    #lookup = 'id'

    def get_object(self):
        id = self.kwargs.get('id')#id = self.kwargs.get(lookup)
        obj = None
        if id is not None:
            obj = get_object_or_404(self.model, id=id)#obj = get_object_or_404(Course, id=id)
        return obj


class CourseView(CourseObjectMixin, View):
    template_name = "coursese/course_detail.html"

    def get(self, request, id=None, *args, **kwargs):
        # context er vitor object dite hobe.build in
        context = {'object': self.get_object()}
        return render(request, self.template_name, context)


class CourseUpdateView(CourseObjectMixin, View):
    template_name = "coursese/course_update.html"

    def get(self, request, id=None, *args, **kwargs):
        # GET method
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(instance=obj)
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)

    def post(self, request, id=None,  *args, **kwargs):
        # POST method
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)


class CourseDeleteView(CourseObjectMixin, View):
    template_name = "coursese/course_delete.html"  # DetailView

    def get(self, request, id=None, *args, **kwargs):
        # GET method
        context = {}
        obj = self.get_object()
        if obj is not None:
            context['object'] = obj
        return render(request, self.template_name, context)

    def post(self, request, id=None,  *args, **kwargs):
        # POST method
        context = {}
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            context['object'] = None
            return redirect('/mycourses/')
        return render(request, self.template_name, context)
