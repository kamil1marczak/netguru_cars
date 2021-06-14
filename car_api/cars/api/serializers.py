from rest_framework import serializers
from car_api.cars.models import Car, Rating
import requests


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ["id", "make", "model", "avg_rating"]

    def create(self, validated_data):
        make = validated_data.get("make")
        model = validated_data.get("model")
        url = f"https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/{make}?format=json"
        response = requests.get(url)
        data_set = response.json()

        if not data_set["Message"] == "Response returned successfully":
            raise serializers.ValidationError(
                {"error": "Could not connect to 'https://vpic.nhtsa.dot.gov/api/'"}
            )

        if not data_set["Results"]:
            raise serializers.ValidationError(
                {"error": "dataset from 'https://vpic.nhtsa.dot.gov/api/' i empty"}
            )

        data_set_clean = data_set["Results"]

        if model not in [i["Model_Name"] for i in data_set_clean]:
            raise serializers.ValidationError(
                {"error": "data for provided credentials not found"}
            )

        car = Car.objects.create(**validated_data)

        return car


class RatingSerializer(serializers.ModelSerializer):
    car_id = serializers.PrimaryKeyRelatedField(
        source="car", queryset=Car.objects.all()
    )

    class Meta:
        model = Rating
        fields = ["car_id", "rating_value"]


class PopularCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ["id", "make", "model", "rates_number"]
