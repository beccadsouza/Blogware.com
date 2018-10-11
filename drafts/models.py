from django.db import models

# Create your models here.
class drafts(models.Model):
    #doc_id = models.CharField(max_length = 20, primary_key = True)
    title = models.CharField(max_length = 100)
    body = models.TextField()
    date_of_update = models.DateField()
    date_of_publish = models.DateField()
    status = models.IntegerField()
    thumbnail = models.ImageField(upload_to = 'thumbs')
    author = models.CharField(max_length = 20)


    def __str__(self):
        return ' '.join(list([self.title, self.body, str(self.date_of_update), str(self.date_of_publish)]))
