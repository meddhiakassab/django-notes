from django.db import models
    
class User(models.Model):
    id = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=255, blank=True)
    
    def __str__(self):
        return self.userName

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    owner = models.ForeignKey('User', related_name='snippets', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"title: {self.title}, owner: {self.owner.userName}"
    
    class Meta:
        ordering = ['created']

# u1 = User(...)
# s1 = Snippet(... , owner = u1)
# s2 = Snippet(... , owner = u1)
# s3 = Snippet(... , owner = u1)
# u1.save()
# s1 ... s3     ...      .save()
# e = u1.snippets.all()
# e : list of all snippets of a specific u1 user