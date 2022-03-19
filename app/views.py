from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView, ListView
from .forms import ContactForm
from .models import Profile, Work, Experience, Education, Software, Technical
from django.conf import Settings
from django.views.generic.edit import FormView
from .forms import ContactForm
from django.urls import reverse_lazy

class IndexView(TemplateView):
    template_name = 'app/index.html'

    #1つのテンプレートに2つ以上のModelを使うためのメソッド
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #idを降順に並べ替え、最新のプロフィールデータを取得
        if Profile.objects.all().exists():
            context['profile_data'] = Profile.objects.all().order_by('-id')[0]
        #作成日を降順に並べ替え、最新の作品から取得していく(4個分)
        context['work_data'] = Work.objects.all().order_by('-created')[:4]
        return context


class DetailPageView(DetailView):
    template_name = 'app/detail.html'
    model = Work
    # context_object_nameはテンプレートで表示する際のモデルの参照名。
    context_object_name = 'work_data'


class AboutView(TemplateView):
    template_name = 'app/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if Profile.objects.all().exists():
            context['profile_data'] = Profile.objects.all().order_by('-id')[0]
        context['experience_data'] = Experience.objects.all().order_by('-id')
        context['education_data'] = Education.objects.all().order_by('-id')
        context['software_data'] = Software.objects.all().order_by('-id')
        context['technical_data'] = Technical.objects.all().order_by('-id')
        return context

class WorksView(ListView):
    template_name = 'app/works.html'
    model = Work
    context_object_name = 'work_data'
    #作品を作成日の新しい順に並び替える
    ordering = ['-created']




class ContactView(FormView):
    template_name = 'app/contact.html'
    form_class = ContactForm
    #送信が成功したらurls.pyからname='contact_result'のurlにリダイレクトする
    success_url = reverse_lazy('contact_result')

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)


class ContactResultView(TemplateView):
    template_name = 'app/contact_result.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['success'] = "お問い合わせは正常に送信されました。"
        return context