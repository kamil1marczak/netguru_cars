from django.db import models

RATING_CHOICES = [(i, i) for i in range(6)]


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    make = models.CharField(max_length=512)
    model = models.CharField(max_length=512)

    @property
    def avg_rating(self) -> float:
        if self.ratings.first():
            result = self.ratings.all().aggregate(models.Avg("rating_value"))
            return round(result["rating_value__avg"], 1)
        else:
            pass

    @property
    def rates_number(self) -> int:
        if self.ratings.first():
            return self.ratings.count()
        else:
            return 0

    def __str__(self) -> str:
        return f"make: {self.make} model: {self.model}"

    class Meta:
        unique_together = (
            "make",
            "model",
        )


class Rating(models.Model):
    id = models.AutoField(primary_key=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="ratings")
    rating_value = models.IntegerField(choices=RATING_CHOICES, default=0)

    def __str__(self) -> str:
        return f"id: {str(self.id)} rating: {self.rating_value}"
