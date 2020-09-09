from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
#from django.urls.base import reverse_lazy
from django.views.generic import (
    CreateView, DetailView, ListView, UpdateView, DeleteView
)
# Create your views here. ArticleModelForm
from .forms import ArticleModelForm
from .models import Article


class ArticleListView(ListView):
    # templates folder er vitor e je nam dia hobe sei nam age set kore
    template_name = 'articles_test/article_list.html'
    # dite hobe. chile direct template folder er vitoreo file raka jabe
    queryset = Article.objects.all()

# class ArticleDetailView(DetailView):
#     template_name_list ='articles/article_detail.html'
#     queryset=Article.objects.all()

# or


class ArticleDetailView(DetailView):
    template_name = 'articles_test/article_detail.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)


class ArticleCreateView(CreateView):
    template_name = 'articles_test/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()

    # one way: not tested
    # success_url='/'
    # ##or
    # def get_success_url(self):
    #     return '/'

    # two way : tested
    # def form_valid(self, form):
    # print(form.cleaned_data) #this will print all form data in console
    #     #(1 & 2 hide kore 3 on korle direct article model a chole jabe link.karon ekane super call kora ache)
    #     return super().form_valid(form) #3

    # three way
    def form_valid(self, form):
        form.save()  # 1
        return redirect('articles:article-list')  # 2


class ArticleUpdateView(UpdateView):
    template_name = 'articles_test/article_create.html'
    form_class = ArticleModelForm

    # this funtion to save the update form
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    # step 1
    # eta step follow korle update hoa direct main list e chole jabe
    # update hoa main list e na gia jodi update ta separetly dekte chai tar por main list e jete chai tahole nicher step follow korte hobe

    # def form_valid(self, form):
    #     form.save() #1
    #     return redirect('articles:article-list')#2

    # ##must read step 1
    # # step 2: this function to redirect after update the form
    def get_absolute_url(self):
        return reverse("articles:article-detail", kwargs={"id": self.id})


class ArticleDeleteView(DeleteView):
    template_name = 'articles_test/article_delete.html'
    #queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def get_success_url(self):
        return reverse('articles:article-list')

##Function base delete
# def deleteTask(request, pk):
#     item = Task.objects.get(id = pk)
#     if request.method == "POST":
#         item.delete()
#         return redirect("/")
#     context = {'item': item}
#     return render(request, 'tasks/delete.html', context)

# #login base delete
# class ArticleDeleteView(LoginRequiredMixin, DeleteView):
#     model = Article # or (queryset = Article.objects.all())
#     success_url = reverse_lazy("articles:article-list")