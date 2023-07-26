from django.db import models
from django.conf import settings

class doc_controller(models.Model):
    doc_controller_id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class jhpl_ims_masterlist(models.Model):
    STATUS_SELECT = [
        ("Active", "Active"),
        ("Obsolete", "Obsolete"),
        ("InProcess", "InProcess"),
        ]
    ims_masterlist_id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    doc_num = models.CharField(max_length=200, null = False, blank= False)
    doc_title = models.CharField(max_length=200, null=True, blank=True)
    rev_num = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    issue_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=9, choices=STATUS_SELECT)
    reviewed_by = models.ForeignKey("doc_controller", on_delete=models.CASCADE, related_name="jhpl_reviewed_by",null= True,blank = True)
    reviewed_date = models.DateField(null=True, blank=True)
    approved_by = models.ForeignKey("doc_controller", on_delete=models.CASCADE, related_name="jhpl_approved_by",null= True,blank= True)
    approved_date = models.DateField(null=True, blank=True)
    control_copy_num = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.doc_title


class notes(models.Model):
    notes_id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    large_text_body = models.TextField()
    jhpl_ims_masterlist_key = models.ForeignKey("jhpl_ims_masterlist", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.large_text_body


class incident(models.Model):
    incident_id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    incident_datetime = models.DateTimeField()
    people_involved = models.TextField()
    incident_location = models.CharField(
        max_length=200, null=False, blank=False)
    incident_description = models.TextField()
    incident_witness = models.CharField(max_length=200, null=True, blank=True)
    incident_outcome = models.BooleanField(default=False)
    picture = models.BinaryField(null=True, blank=True, editable=True)
    content_type = models.CharField(
        max_length=256, null=True, blank=True, help_text='The MIMEType of the file')

    def __str__(self):
        return str(self.incident_id)