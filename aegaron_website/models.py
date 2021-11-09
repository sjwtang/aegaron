from django.db import models

# Create your models here.

class Term(models.Model):
	id = models.AutoField(primary_key=True)
	name_eng = models.CharField(max_length=300)
	name_ger = models.CharField(max_length=300)
	name_ar = models.CharField(max_length=300)
	synonym_eng = models.CharField(max_length=300)
	synonym_ger = models.CharField(max_length=300)
	synonym_ar = models.CharField(max_length=300)
	broader_term = models.ManyToManyField(Term, blank=True)
	narrower_term = models.ManyToManyField(Term, blank=True)
	related_links = models.ManyToManyField(ExternalSource, blank=True)
	definition_eng = models.CharField(max_length=300)
	definition_ger = models.CharField(max_length=300)
	definition_ar = models.CharField(max_length=300)
	image = models.ManyToManyField(Image, blank=True)




class Image(models.Model):
	id = models.AutoField(primary_key=True)
	context = models.OneToOneField(
        Plan,
        on_delete=models.CASCADE,
        primary_key=True,
    )




class ExternalSource(models.Model):
	id = models.AutoField(primary_key=True)
	source = models.CharField(max_length=300)
	url = models.URLField(blank=True)
	name_eng = models.CharField(max_length=300)
	name_ger = models.CharField(max_length=300)
	name_at = models.CharField(max_length=300)
