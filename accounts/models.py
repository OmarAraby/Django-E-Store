from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.urls import reverse
from django.utils.translation import gettext_lazy as _    
import datetime
from django_countries.fields import CountryField
from django.utils.text import slugify
from django.db.models.signals import post_save

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name=_("user"), on_delete=models.CASCADE)
    slug = models.SlugField(blank=True , null=True)
    phone_number = models.CharField(max_length=15 ,blank=True, null=True , verbose_name=_("Phone Number"))
    image = models.ImageField(_("Image"), upload_to="profile_image",blank=True, null=True)
    country = CountryField() 
    address = models.CharField(max_length=100)
    join_date = models.DateTimeField(_("join date"), default=datetime.datetime.now)
    

    def save(self, *args , **kwargs ):
        if not self.slug:
            self.slug = slugify(self.user.username)
        super(Profile,self).save( *args , **kwargs )



    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse("accounts:Profile_detail", kwargs={"slug": self.slug})
    




## create new user  -----> create new empty profile for this user

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


