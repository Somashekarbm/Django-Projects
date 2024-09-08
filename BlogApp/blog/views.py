from django.shortcuts import render


posts=[
    {
        'author':'somu',
        'title':'Blog post 1',
        'content':'first post',
        'date_posted':'August 27'
    },
    {
        'author':'shrey',
        'title':'Blog post 2',
        'content':'first post',
        'date_posted':'august 28'
    }
]

def home(request):
    context={
        'posts':posts,
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'About'})



