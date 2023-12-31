from django.db import models
from django.utils.translation import gettext_lazy as _               ## For translations
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.




class Product(models.Model):
    PRDName =  models.CharField(max_length=50, verbose_name=_("Book Title"))
    PRDAuthor =  models.CharField(max_length=50, verbose_name=_("Author"))
    PRDCategory = models.ForeignKey('Category', on_delete=models.CASCADE,blank=True, null=True ,verbose_name=_("Category"))
    # PRDBrand = models.ForeignKey('settings.Brand', on_delete=models.CASCADE ,blank=True, null=True ,verbose_name=_("Brand"))
    PRDDesc = models.TextField(verbose_name=_("Book Description"))
    PRDImage = models.ImageField(upload_to='book_image/',verbose_name=_("Image") , blank=True , null=True)
    PRDPrice = models.DecimalField(max_digits=8 , decimal_places=2 , verbose_name=_("Price"))
    PRDDiscountPrice = models.DecimalField(max_digits=8 , decimal_places=2 , blank=True, null=True,verbose_name=_("Discount Price"))
    PRDCost = models.DecimalField(max_digits=8 , decimal_places=2 , verbose_name=_("Cost"))
    PRDCreated = models.DateTimeField(auto_now=True , verbose_name=_("Created at"))
    
    PRDSlug = models.SlugField(blank=True, null=True, verbose_name=_("Book URL"))
    PRDISNew = models.BooleanField(default=True ,verbose_name=_("New Book"))
    PRDISBestSeller = models.BooleanField(default=False, verbose_name=_("Best Seller"))


    def save(self, *args, **kwargs):
        if not self.PRDSlug:
            self.PRDSlug =slugify(self.PRDName)

        super(Product , self).save(*args , **kwargs)
    


    class Meta:
            verbose_name = _("Book")
            verbose_name_plural = _("Books")



    def get_absolute_url(self):
        return reverse("store:product_detail", kwargs={"slug": self.PRDSlug})
        


    def __str__(self):
        return self.PRDName
    




class Category(models.Model):
    CATName = models.CharField(max_length=50 , verbose_name=_('Name'))
    CATParent = models.ForeignKey('self' ,limit_choices_to={'CATParent__isnull':True} , verbose_name=_('MAin Category'),on_delete= models.CASCADE , blank=True, null=True) 
    CATDesc = models.TextField(verbose_name=_('Description'))
    CATImg = models.ImageField(upload_to='category/' ,verbose_name=_('Image'),blank=True, null=True)
    CATSlug = models.SlugField(blank=True, null=True, verbose_name=_("Category URL"))


    def save(self, *args, **kwargs):
        if not self.CATSlug:
            self.CATSlug =slugify(self.CATName)

        super(Category , self).save(*args , **kwargs)
    

    class Meta:
            verbose_name = _("Category")
            verbose_name_plural = _("Categories")


    def get_absolute_url(self):
        return reverse("store:category_detail", kwargs={"slug": self.CATSlug})
    


    def __str__(self):
        return self.CATName