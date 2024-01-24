from django.db import models

# Create your models here.


class Scarp_Material(models.Model):
    date=models.DateField()
    doc_no=models.IntegerField()
    department=models.CharField(max_length=50)
    category=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    identified_by=models.CharField(max_length=50)
    item_warehouse=models.CharField(max_length=50)
    item_code=models.CharField(max_length=50)
    quantity=models.IntegerField()
    unit=models.CharField(max_length=50)
    reason=models.TextField()
    man_img=models.ImageField(upload_to="pics")
    superviser_name=models.CharField(max_length=50)
    approved_by=models.CharField(max_length=50)
    planner_name=models.CharField(max_length=50)
    order_no=models.CharField(max_length=50)
    pos_no=models.CharField(max_length=50)
    material_received=models.CharField(max_length=50)
    store1_name=models.CharField(max_length=50)
    store1_img=models.ImageField(upload_to="pics")
    erp_person=models.CharField(max_length=50)
    qa_remark=models.TextField()
    qa_diposition=models.CharField(max_length=50)
    qa_classification=models.CharField(max_length=50)
    qa_name=models.CharField(max_length=50)
    qa_engineer=models.CharField(max_length=50)
    store2_disposition=models.CharField(max_length=50)
    store2_ordernumber=models.CharField(max_length=50)
    store2_name=models.CharField(max_length=50)
    supplier_name=models.CharField(max_length=50)
    store2_orderno=models.CharField(max_length=50)
    rejection_reason=models.TextField()
    rejection_name=models.CharField(max_length=50)
    rejection_department=models.CharField(max_length=50)
    pending_with=models.CharField(max_length=50)



   




