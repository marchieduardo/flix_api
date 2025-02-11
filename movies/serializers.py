from rest_framework import serializers

from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

    def validate_resume_date(self, value):
        if value.year < 1900:
            raise serializers.ValidationError('A data não pode ser anterior à 1900')
        return value
    
    def validate_resume(self, value):
        if len(value) > 250:
            raise serializers.ValidationError('Resumo não pode ter mais de 250 caracteres')
        return value