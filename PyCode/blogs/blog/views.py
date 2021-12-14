from django.shortcuts import render
from blog.models import Blog
import markdown
# Create your views here.
def index(request):
    blog=Blog.objects.all().first()
    blog_content=markdown.markdown(blog.content)
    return render(request,"blog.html",{'blog':blog,"blog_content":blog_content})
