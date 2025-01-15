from django.db import models

from django.db import models


# Model for Room types
class RoomType(models.Model):
    ROOM_TYPES = [
        ("SINGLE", "Single"),
        ("DOUBLE", "Double"),
        ("SUITE", "Suite"),
        ("PENTHOUSE", "Penthouse"),
    ]
    name = models.CharField(max_length=20, choices=ROOM_TYPES)
    description = models.TextField()

    def __str__(self):
        return self.name


# Model for Room
class Room(models.Model):
    room_number = models.CharField(max_length=10, unique=True)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    price_per_night = models.DecimalField(max_digits=7, decimal_places=2)
    availability = models.BooleanField(default=True)
    description = models.TextField(blank=True, null=True)
    amenities = models.TextField(blank=True, null=True)  # e.g., Wi-Fi, AC, etc.

    def __str__(self):
        return f"Room {self.room_number} ({self.room_type})"


# Model for Customer
class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField()
    gender = models.CharField(
        max_length=10,
        choices=[("MALE", "Male"), ("FEMALE", "Female"), ("OTHER", "Other")],
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# Model for Booking
class Booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    number_of_guests = models.PositiveIntegerField()
    special_requests = models.TextField(
        blank=True, null=True
    )  # Special requests from customers

    STATUS_CHOICES = [
        ("BOOKED", "Booked"),
        ("CHECKED_IN", "Checked In"),
        ("CHECKED_OUT", "Checked Out"),
        ("CANCELLED", "Cancelled"),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="BOOKED")

    def __str__(self):
        return f"Booking: {self.customer} - {self.room.room_number} ({self.status})"


# Model for Payment
class Payment(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    payment_date = models.DateTimeField(auto_now_add=True)
    amount_paid = models.DecimalField(max_digits=8, decimal_places=2)
    payment_method = models.CharField(
        max_length=20,
        choices=[
            ("CREDIT_CARD", "Credit Card"),
            ("DEBIT_CARD", "Debit Card"),
            ("CASH", "Cash"),
            ("ONLINE", "Online"),
        ],
    )
    payment_status = models.CharField(
        max_length=20,
        choices=[("PAID", "Paid"), ("PENDING", "Pending"), ("FAILED", "Failed")],
        default="PAID",
    )

    def __str__(self):
        return f"Payment for Booking {self.booking.id} - {self.amount_paid}"
