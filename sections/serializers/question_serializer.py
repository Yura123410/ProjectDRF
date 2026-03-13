from rest_framework.serializers import ModelSerializer
from rest_framework.relations import SlugRelatedField
from rest_framework.fields import CharField, SerializerMethodField

from sections.models import Question, Section

class QuestionSerilizer(ModelSerializer):
    section = SlugRelatedField(slug_field='title', queryset=Section.objects.all())

    class Meta:
        model = Question
        fields = ('id', 'section', 'question')

class QuestionSectionSerilizer(ModelSerializer):
    section = SlugRelatedField(slug_field='title', queryset=Section.objects.all())
    member_answer = CharField()

    class Meta:
        model = Question
        fields = ('id', 'section', 'question', 'member_answer')


