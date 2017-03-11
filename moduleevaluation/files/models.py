import os

from django.db import models
from datetime import date, timedelta


BLOCK_CHOICES = (
    ('YR1', 'Year 1'),
    ('YR2', 'Year 2'),
    ('YR3', 'Year 3'),
    ('MSc', 'MSc')
)

SEMESTER_CHOICES = (
    ('A', 'Autumn Semester'),
    ('S', 'Spring Semester'),
    ('N', 'No-Semester')
)

def file_directory_path(instance, filename):
    filename, file_extension = os.path.splitext(filename)
    return os.path.join(instance.year, instance.block, instance.semester, 'data{0}'.format(file_extension))

class Document(models.Model):

    # Set up the year choices so that it includes every year
    YEAR_CHOICES = []

    today = date.today()
    year = timedelta(days=365)
    last_year = today - year

    while last_year.year > 2013:
        YEAR_CHOICES.append((
            '%s-%s' % (last_year.strftime('%y'), (last_year+year).strftime('%y')),
            '%s/%s' % (last_year.strftime('%Y'), (last_year+year).strftime('%Y'))
        ))
        last_year = last_year - year

    YEAR_CHOICES = tuple(YEAR_CHOICES)

    year = models.CharField(max_length=5, choices=YEAR_CHOICES)
    block = models.CharField(max_length=3, choices=BLOCK_CHOICES)
    semester = models.CharField(max_length=1, choices=SEMESTER_CHOICES)
    docfile = models.FileField(upload_to=file_directory_path)
