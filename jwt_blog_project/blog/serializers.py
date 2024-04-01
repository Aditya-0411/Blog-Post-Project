#
# from rest_framework import serializers
# from .models import BlogPost
# #UserDetails, Profile
#
# class BlogPostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BlogPost
#         fields = '__all__'
#
# # class UserDetailsSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = UserDetails
# #         fields = '__all__'
# #
# # class ProfileSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = Profile
# #         fields = '__all__'

# serializers.py

from rest_framework import serializers
from .models import Blog, Author, Entry

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'name', 'tagline']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'email']

class EntrySerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)

    class Meta:
        model = Entry
        fields = ['id', 'blog', 'headline', 'body_text', 'pub_date', 'mod_date', 'authors', 'number_of_comments', 'number_of_pingbacks', 'rating']
