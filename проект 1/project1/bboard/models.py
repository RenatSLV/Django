from django.db import models

class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True)
    class Meta:
        verbose_name = "Rubric"
        verbose_name_plural = "Rubrics"
        ordering = ['name']

    def __str__(self):
        return self.name

class Bb(models.Model):
    rubric = models.ForeignKey(Rubric, on_delete=models.PROTECT, null=True)
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    published = models.DateTimeField(auto_now_add=True, db_index=True)
    def title_and_price(self):
        if self.title and self.price:
            return f"Title = {self.title} and Price = {self.price}"

    title_and_price.short_description = 'Данная функция объеденяет цену и заголовок'

    def model_func(self):
        if self.title == "Sport" and self.price < 1000:
            return True

    class Meta:
        verbose_name = "Publication"
        verbose_name_plural = "Publications"
        ordering = ['-published']
        # order_with_respect_to = 'rubric'

    def __str__(self):
        return self.title

class Spare(models.Model):
    name = models.CharField(max_length=20)

class Car(models.Model):
    name = models.CharField(max_length=20)
    spares = models.ManyToManyField(Spare, null=True)

class Crypto(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    id = models.IntegerField(primary_key=True, )
    comment = models.TextField(null=True, blank=True)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.comment

# class Human(models.Model):
#     name = models.CharField(max_length=100, null=True, blank=True)
#     age = models.IntegerField(null=True, blank=True)
#     has_children = models.BooleanField(default=0)
#
# class Children(models.Model):
#     name = models.CharField(max_length=100, null=True, blank=True)
#     age = models.IntegerField(null=True, blank=True)
#     parent = models.ForeignKey(Human, on_delete=models.SET_NULL, null=True)
#
# class SupermarketIceCream(models.Model):
#     name = models.CharField(max_length=100, null=True, blank=True, unique=True)
#     place = models.TextField(null=True, blank=True)
#
# class Icecream(models.Model):
#     name = models.CharField(max_length=100, null=True, blank=True, unique=True)
#     price = models.DecimalField(null=True, blank=True, max_digits=3, decimal_places=2)
#     datetimeCreate = models.DateTimeField(auto_now_add=True, db_index=True)
#     place = models.ForeignKey(SupermarketIceCream, on_delete=models.SET_NULL, null=True)

        # unique_together = (
        #     ('title', 'published'),
        #     ('price', 'title'),
        # )
        # get_latest_by = 'published'
        # indexes = [
        #     models.Index(field=['title', 'published']),
        #     models.Index(field=['price', 'published'],
        #                  condition=models.Q(price_lte=1000, price_gt=500),
        #                  ),
        # ]

    # KINDS = (
    #     (None, 'Выберите рубрику'),
    #     ('Техника', ('c', 'Car')),
    #     ('Недвижемость', ('h', 'Home'))
    # )
    #
    # class KINDS(models.IntegerChoices):
    #     BUY = 1, "Car"
    #     SELL = 2, "House"
    #     RENT = 3, "Car"
    #     __empty__ = 'Выберите рубрику'
    #
    # kinds = models.CharField(max_length=1, default=KINDS.SELL, choices=KINDS.choices, blank=True, null=True)

    # class FLOATCHOICES(float, models.Choices):
    #     METERS = 1.2, "Metr"
    #     FEET = 1.3, "Feet"
    #     YARD = 1.4, "Yard"

    # floatChoices = models.FloatField(choices=FLOATCHOICES.choices, default=FLOATCHOICES.METERS)
    # test = models.BooleanField(null=True, blank=True)
    # test2 = models.URLField(null=True, blank=True)
    # test3 = models.IntegerField(null=True, blank=True)
    # test4 = models.SmallIntegerField(null=True, blank=True)
    # test5 = models.BigIntegerField(null=True, blank=True)
    # test6 = models.DecimalField(null=True, blank=True, max_digits=10, decimal_place=2)
    # test7 = models.DateField(null=True, blank=True)
    # test8 = models.TimeField(null=True, blank=True, auto_created=True)
    # test9 = models.SlugField(null=True, blank=True)
    # test5 = models.AutoField(null=True, blank=True)

#     rubric = models.ForeignKey(Rubric, on_delete=models.PROTECT, null=True)
#     rubric = models.ForeignKey(Rubric, on_delete=models.CASCADE, null=True)
#     rubric = models.ForeignKey(Rubric, on_delete=models.SET, null=True)
#
# class User(models.Model):
#     username = models.CharField(max_length=20, unique=True)
#     password = models.CharField(max_length=20)
#
# class Passport(models.Model):
#     iin = models.IntegerField()
#     name = models.CharField(max_length=20)
#     surname = models.CharField(max_length=20)
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#
# class Spare(models.Model):
#     name = models.CharField(max_length=20)
#
# class Car(models.Model):
#     name = models.CharField(max_length=20)
#     spares = models.ManyToManyField(Spare, on_delete=models.SET_NULL, null=True)