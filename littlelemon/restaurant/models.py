from django.db import models

# Create your models here.

class Menu(models.Model):
    Title = models.CharField(max_length = 255)
    Price = models.DecimalField(max_digits = 10, decimal_places = 2)
    Inventory = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.Title

class Booking(models.Model):
    Name = models.CharField(max_length = 255)
    No_of_guests = models.PositiveSmallIntegerField()
    BookingDate = models.DateTimeField()

    def __str__(self):
        return self.Name + "_" + str(self.BookingDate.date()) + "_" + str(self.BookingDate.time())