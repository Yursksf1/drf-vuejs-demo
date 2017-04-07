from .models import Question, Choice
from rest_framework import serializers


class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'


class ChoiceIDSerializer(serializers.Serializer):
    id = serializers.IntegerField()

class NestedChoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Choice
        fields = ('choice_text', 'votes', 'id')


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    choices = NestedChoiceSerializer(many=True, read_only=True, source='choice_set')

    class Meta:
        model = Question
        fields = '__all__'