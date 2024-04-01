#
# from rest_framework import generics, status
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from django.http import Http404
#
# from . import models
# from .models import BlogPost
#     #, UserDetails, Profile
# from .serializers import BlogPostSerializer
# #UserDetailsSerializer, ProfileSerializer
# from rest_framework.views import APIView
# from django.contrib.auth.models import User
#
#
# class BlogPostListView(APIView):
#      permission_classes = [IsAuthenticated]
#
#      def get(self, request):
#         posts = BlogPost.objects.all()
#         serializer = BlogPostSerializer(posts, many=True)
#         return Response(status=status.HTTP_200_OK, data=serializer.data)
#
#      def post(self, request, format=None):
#          serializer = BlogPostSerializer(data=request.data)
#          print(request.data)
#          if serializer.is_valid():
#              serializer.save()
#              return Response(serializer.data, status=status.HTTP_201_CREATED)
#          else:
#              return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#      def delete(self, request):
#         try:
#             post = BlogPost.objects.get(id=request.data['id'])
#             post.delete()
#             return Response({"status": "success", "data": "Item Deleted"})
#         except BlogPost.DoesNotExist:
#             return Response({"status": "error", "data": "Blog post not found"}, status=status.HTTP_404_NOT_FOUND)
#         except Exception as e:
#             return Response({"status": "error", "data": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#
#      def put(self, request):
#          post = BlogPost.objects.get(id=request.data['id'])
#          serializer = BlogPostSerializer(post, data=request.data)
#          if serializer.is_valid():
#              serializer.save()
#              return Response(serializer.data)
#
#          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#


# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Blog, Author, Entry
from .serializers import BlogSerializer, AuthorSerializer, EntrySerializer

class BlogCrudView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AuthorCrudView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        author = get_object_or_404(Author, pk=pk)
        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        author = get_object_or_404(Author, pk=pk)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class EntryCrudView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        entries = Entry.objects.all()
        serializer = EntrySerializer(entries, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        entry = get_object_or_404(Entry, pk=pk)
        serializer = EntrySerializer(entry, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        entry = get_object_or_404(Entry, pk=pk)
        entry.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
