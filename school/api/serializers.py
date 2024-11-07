from rest_framework import serializers
from school.models import Subject, Course, Module

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'title', 'slug']

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Module
        fields = ['orders', 'title', 'description']

class CourseSerializer(serializers.ModelSerializer):
    modules = ModuleSerializer(many=True,read_only=True)
    class Meta:
        model = Course
        fields = [
            'id', 'subject','title', 'slug', 'overview', 'created', 'owner', 
            'module'
        ]