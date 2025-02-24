from rest_framework import serializers
from django.db.models import Avg

from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def get_rate(self, obj):
        # reviews = obj.reviews.all()    # -----> Método de cálculo da média das reviews escrito na mão

        # if reviews:
        #     sum_reviews = 0

        #     for review in reviews:
        #         sum_reviews += review.stars

        #     reviews_count = reviews.count()

        #     return round(sum_reviews / reviews_count, 1)

        # return None

        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']     # -----> Função acima reescrita utilizando métodos Aggregate e Avg

        if rate:
            return round(rate, 1)
        return None

    def validate_resume_date(self, value):
        if value.year < 1900:
            raise serializers.ValidationError('A data não pode ser anterior à 1900')
        return value

    def validate_resume(self, value):
        if len(value) > 250:
            raise serializers.ValidationError('Resumo não pode ter mais de 250 caracteres')
        return value
