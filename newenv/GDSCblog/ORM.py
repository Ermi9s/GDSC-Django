import os
import django
from .Blog.models import Post
from .Comment.models import Comment

os.environ.setdefault("DJANGO_SETTINGS_MODULE" , "GDSCblog.settings")
django.setup()

#_______________________________________for Blog app ______________________________

#creating Posts 1 2 of em
post1 = Post(Title="C++ full course", Catagory="Programming language", Content="A very powerfull programming language")
post1.save()

post1_0 = Post(Title="Java", Catagory="Programming language", Content="System,Out.println(hello world)")
post1_0.save()

#creating Posts 2
post2 = Post(Title="FIkir Eskemekabir", Catagory="Books", Content="The Greatest Amharic Book")
post2.save()

#creating Posts 3
post3 = Post(Title="Doro wet", Catagory="Food", Content="The most common habesha fest food")
post3.save()


#Quering the posts by catagory
cata1 = Post.objects.filter(Catagory = "Programming language")

for obj in cata1:
    print(obj.Title)

#updating post 2
p2 = Post.objects.filter(Title = "Books")
p2.update(Content = "This is the updated content Of the Book")

#deleting the first post
toBeDeleted = Post.objects.get(Title = "Food")
toBeDeleted.delete()


#______________________________________________For Comment app______________________________

#create

comment1 = Comment(Content = "This course was very helpful" , Author = "Ermias" , post = post1)
comment1.save()
comment2 = Comment(Content = "This Book is amazing!" , Author = "Dagm" , post = post2)
comment2.save()
comment3 = Comment(Content = "I dont like this language" , Author = "Abe" , post = post1_0) 
comment3.save()

#update

toBeUodated = Comment.objects.filter(Author = "Ermias")
toBeUodated.update(Conttent = "The greatest pg ever made")

#delete
doomed = Comment.objects.get(post = post1_0)
doomed.delete()