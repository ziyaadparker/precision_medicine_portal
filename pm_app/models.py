from django.db import models

class gwas_catalogue_ancestory(models.Model):
    study_accession = models.CharField(max_length=50)
    pubmedid = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    initial_sample_description = models.CharField(max_length=500)
    stage = models.CharField(max_length=50)
    number_of_individuals = models.IntegerField(default=20)
    broad_acenstral_category = models.CharField(max_length=50)
    country_of_origin = models.CharField(max_length=50)
    country_of_recruitment = models.CharField(max_length=500)
    additional_ancestry_description = models.CharField(max_length=500)

    class Meta:
        db_table = "gwas_catalogue_ancestory"