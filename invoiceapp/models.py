from django.db import models

class AgentDetails(models.Model):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=60)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.full_name

class InvoiceDetails(models.Model):
    agent_name = models.CharField(max_length=50, blank=True)
    invoice_number = models.IntegerField(blank=True, null=True)
    vender_name = models.CharField(max_length=50, blank=True)
    invoice_date = models.CharField(blank = True, max_length=20)
    pdf = models.FileField(upload_to= 'pdf/',blank=True)
    upload_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.agent_name

class ItemDetails(models.Model):
    agent_name = models.CharField(max_length=50, blank=True)
    invoice_number = models.IntegerField(blank=True, null=True)
    item_description = models.CharField(max_length= 50, blank=True)
    item_quantity = models.IntegerField(blank=True, null=True)
    item_rate = models.IntegerField(blank=True , null=True)

    def __str__(self):
        return self.item_description

