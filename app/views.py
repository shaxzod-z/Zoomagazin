from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from app.models import Product, User, Client, Comment, Category, Post, PostDetail, Contact


class IndexView(ListView):
    template_name = 'index.html'
    model = Post
    context_object_name = 'posts'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        context['clients'] = Client.objects.all()
        context['products'] = Product.objects.all()
        context['comments'] = Comment.objects.all()
        context['categories'] = Category.objects.all()
        context['post_details'] = PostDetail.objects.all()

        return context


class PostDetailView(DetailView):
    template_name = 'detail.html'
    model = Post
    context_object_name = 'post1'


class AboutView(ListView):
    template_name = 'about.html'
    model = User
    context_object_name = 'users1'


class ServicesView(ListView):
    template_name = 'service.html'
    model = Client
    context_object_name = 'clients1'


class ProductView(ListView):
    template_name = 'product.html'
    model = Product
    context_object_name = 'products1'


class PriceView(ListView):
    template_name = 'price.html'
    model = User
    context_object_name = 'users2'


class TeamView(ListView):
    template_name = 'team.html'
    model = User
    context_object_name = 'users3'


class TestView(ListView):
    template_name = 'testimonial.html'
    model = Client
    context_object_name = 'clients2'


class PostView(ListView):
    template_name = 'blog.html'
    model = Post
    context_object_name = 'posts1'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = self.get_queryset()
        paginator = Paginator(products, self.paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['post_page'] = page_obj
        context['range'] = range(1, 6)
        return context

    def get_queryset(self):
        queryset = super().get_queryset().order_by('-created_at')
        query = self.request.GET.get("query")
        sort_by = self.request.GET.get('sort_by')
        if sort_by == 'created_at':
            queryset = queryset.order_by('-created_at')
        if sort_by == 'title':
            queryset = queryset.order_by('title')
        if sort_by == 'id':
            queryset = queryset.order_by('id')
        elif sort_by == 'text':
            queryset = queryset.order_by('text')
        elif sort_by == 'photo':
            queryset = queryset.order_by('photo')

        return queryset


class Post1View(ListView):
    template_name = 'blog.html'
    model = Post
    context_object_name = 'posts2'


class ContactView(CreateView):
    template_name = 'contact.html'
    model = Contact
    fields = "__all__"
    context_object_name = 'contacts'
    success_url = reverse_lazy('contact')
