from django.db import models


class Comment(models.Model):
    user = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    photo = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.title


class User(models.Model):
    username = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='users/')
    designation = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class Post(models.Model):
    photo = models.ImageField(upload_to='posts/')
    title = models.CharField(max_length=100)
    text = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    comments = models.ForeignKey(Comment, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Client(models.Model):
    full_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='clients/')
    profession = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.full_name


class PostDetail(models.Model):
    photo = models.ImageField(upload_to='posts/')
    title = models.CharField(max_length=100)
    text = models.TextField()
    comments = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.name


