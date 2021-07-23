from django.db import models

# Create your models here.
country=(
('','-----Country Select -----'),
('Bangladesh','Bangladesh'),
('India','India'),
('Pakistan','Pakistan'),
('NewYork','NewYork'),
)
class registration(models.Model):
    user_name=models.CharField(max_length=20)
    frist_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email_address=models.EmailField()
    phone_no=models.CharField(max_length=11)
    road_no=models.CharField(max_length=10)
    country=models.CharField(max_length=50,choices=country)
    def __str__(self):
        return self.frist_name +" "+ self.last_name
class user_details(models.Model):
    user_id=models.ForeignKey(registration,on_delete=models.CASCADE)
    product=models.CharField(max_length=50)
    buydate=models.DateField()

    def __str__(self):
        return "Product id"+ str(self.user_id)
