from django.db import models

# Create your models here.
class CustLogin(models.Model):
    """customer login table """
    loginName = models.CharField(max_length=20)
    pwd = models.CharField(max_length=20)
    user_stats = models.IntegerField(default=0)

    def __str__(self):
        return self.loginName


class CustInfo(models.Model):
    """customer info table """
    custID = models.ForeignKey(CustLogin, on_delete=models.CASCADE)
    customer_last_name = models.CharField(max_length=20)
    customer_first_name = models.CharField(max_length=20)
    phone = models.IntegerField(unique=True)
    email = models.EmailField()
    gender = models.IntegerField()
    register_time = models.DateTimeField(auto_now_add=True)
    account = models.DecimalField(max_digits=5,decimal_places=2)
    modify = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.customer_first_name+' '+self.customer_last_name


class CustBalance(models.Model):
    custID = models.ForeignKey(CustLogin, on_delete=models.CASCADE)
    source = models.IntegerField()
    sn = models.IntegerField()
    create_time = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=5,decimal_places=2)

class Product(models.Model):
    code = models.CharField(max_length=16,unique=True)
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    status = models.IntegerField()
    descript =models.TextField()
    modify = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name


class Result(models.Model):

    def user_directory_path(self, filename):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return 'user_{0}/{1}'.format(self.id, filename)

    prodID = models.ForeignKey(Product, on_delete=models.CASCADE)
    data = models.FileField(upload_to=user_directory_path)
    result = models.FileField(upload_to=user_directory_path)
    status = models.IntegerField()
    modify = models.DateTimeField(auto_now=True)


class Order(models.Model):
    custID = models.ForeignKey(CustLogin, on_delete=models.CASCADE)
    sn = models.IntegerField()
    PayMethod = models.IntegerField()
    create_time = models.DateTimeField(auto_now_add=True)
    paytime = models.DateTimeField()
    modify = models.DateTimeField(auto_now=True)
    finnish_time = models.DateTimeField()
    cost = models.DecimalField(max_digits=5,decimal_places=2)


class Detail(models.Model):
    orderID = models.ForeignKey(Order, on_delete=models.CASCADE)
    prodID = models.ForeignKey(Product, on_delete=models.CASCADE)
    resultID =models.ForeignKey(Result, on_delete=models.CASCADE)
    modify = models.DateTimeField(auto_now=True)