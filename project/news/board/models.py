from django.db import models


class News(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(default=0.0)

    def __str__(self):
        return self.name + "/" + str(self.price)


class Order(models.Model):
    time_in = models.DateTimeField(auto_now_add=True)
    time_out = models.DateTimeField(null=True)
    cost = models.FloatField(default=0.0)
    take_away = models.BooleanField(default=False)
    complete = models.BooleanField(default=False)

    news = models.ManyToManyField(News, through='NewsOrder')


class NewsOrder(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)