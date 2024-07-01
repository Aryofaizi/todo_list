from django.db import models
from django.shortcuts import reverse

class Task(models.Model):
    STATUS_COMPLETED = "c"
    STATUS_HAS_DUE_DATE = "h"
    STATUS_EXPIRED = "e"
    STATUS = (
        ("c", "compeleted"),
        ("e", "expired"),
        ("h", "has due date")
    )
    title = models.CharField(max_length=50)
    due_date = models.DateField()
    status = models.CharField(max_length=1, choices=STATUS, default=STATUS_HAS_DUE_DATE)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)


    def mark_task(self):
        if self.status == self.STATUS_COMPLETED : 
            self.status = self.STATUS_HAS_DUE_DATE
            self.save()
        else:
            self.status = self.STATUS_COMPLETED
            self.save()
            
    def delete_task(self):
        del self
        
    