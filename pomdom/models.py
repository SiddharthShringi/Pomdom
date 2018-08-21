from django.db import models


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True


class Task(BaseModel):
    Priority_Choices = (
        ('H', 'High'),
        ('M', 'Medium'),
        ('L', 'Low'),
    )

    Status_Choices = (
        ('D', 'Done'),
        ('P', 'Pending')
    )
    name = models.CharField(max_length=30)
    priority = models.CharField(max_length=1, choices=Priority_Choices, default='M')
    status = models.CharField(max_length=1, choices=Status_Choices, default='P')

    def __str__(self):
        return self.name
