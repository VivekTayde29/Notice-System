from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator,\
    RegexValidator

# Create your models here.
class Branch(models.Model):
    name = models.CharField(max_length = 100)
    hod = models.CharField(max_length = 100)
    def __str__(self):
        return "%s (%s)" % (self.name, self.hod) # multipale  string sow karane ke liye database me  brach,hod dono show karega

class Notice(models.Model):
    subject = models.CharField(max_length = 100)
    msg = models.TextField()
    cr_date = models.DateTimeField(auto_now_add=True)
    branch = models.ForeignKey(to=Branch, on_delete=CASCADE, null=True, blank=True)

    def __str__(self):
        return self.subject

class Question(models.Model): # user question bhi puch sakta hai
    subject = models.CharField(max_length = 100)
    msg = models.TextField()
    cr_date = models.DateTimeField(auto_now_add=True)
    user_name=models.CharField(max_length=100)
    def __str__(self):
        return self.subject


class Profile(models.Model):
    user = models.OneToOneField(to=User,on_delete=CASCADE)  # OneTOOneField iska matlab hai ki ak user ka ak hi profile hoga ak nam ka user 2 profile nhi bana sakta
    # to=user, iska matlab hai ki ye add hoga user se jo login rahega, on_delete=cascade, means jab user ko delete kiya jayega tab profile ko bhi delete kar dena

    branch = models.ForeignKey(to=Branch, on_delete=CASCADE, null=True,blank=True)  # profile table me bhi ak fild hoga brach name se jisme student apni brach fild karega
    sem = models.IntegerField(default=1, choices=((1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8,8)))  # default=1 iska matlab ki 1 default show hoga field me or choice=(1,1)...(8,8) isme ak field me show ke liye or ak database me show ke liye hai
    marks_10 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(
        100)])  # o se kam or 100 se jyada number nhi lega
    marks_12 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    marks_aggr = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    rn = models.IntegerField(validators=[MinValueValidator(1)], null=True, blank=True,unique=True)  # unique=True iska matlab hai ki ak rol number ke do student nhi lega rn sabhi ka unique hona chahiye , aise hi ham email ko bhi unique bana sakte hai
    pn = models.CharField(validators=[RegexValidator("^0?[5-9]{1}\d{9}$")], max_length=15, null=True, blank=True)

    def __str__(self):
        return "%s" % self.user  # yaha data base me sirf user ka nam dikhayega
