from django.db import models


class Message(models.Model):
    sender = models.CharField(max_length=100)
    email = models.EmailField(max_length=65)
    subject = models.CharField(max_length=100)
    body = models.TextField(max_length=1000)
    date_send = models.DateTimeField(auto_now_add=True)
    new = models.BooleanField(default=True)
    replied = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.email}  =>  {self.body[:50]}'

    def __body__(self):
        return self.body[:50]


def projectDir(instance, filename):
    path = f'tec-project/{str(instance.id)}_{str(instance.project_instance.project_location)}/{str(filename)}'
    print(type(path))
    return path


class Project(models.Model):
    TYPE = {
        'solor': 'Solar Installation', 'electric': 'Electrical Wiring',
        'cctv': 'CCTV Installation', 'web': 'Web Development'
    }
    project_type = models.CharField(max_length=100)
    project_name = models.CharField(max_length=100, null=True, blank=True)
    project_location = models.CharField(max_length=100, null=True, blank=True)
    project_client = models.CharField(max_length=100, null=True, blank=True,)

    date_started = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.project_location} => {self.project_type}'


class ProjectImage(models.Model):

    project_instance = models.ForeignKey(
        Project, default=None, on_delete=models.CASCADE)
    project_pictures = models.FileField(upload_to=projectDir,)

    def __str__(self):
        return f'{self.project_instance.project_type} {self.project_instance.project_client}'
