from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField

from sections.models import Section, Content
from sections.serializers.content_serializers import ContentSectionSerializer


class SectionSerializer(ModelSerializer):
    class Meta:
        model = Content
        field = '__all__'


class SectionListSerializer(ModelSerializer):
    section_content_title = SerializerMethodField()

    def get_section_content_title(self, section):
        return ContentSectionSerializer(Content.objects.filter(section=section), many=True).data

    class Mete:
        model = Section
        field = ('id', 'title', 'section_content_title')
