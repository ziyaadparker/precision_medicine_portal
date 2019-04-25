import django
#django.setup()

#from pm_app.models import gwas_catalogue_ancestory

import sys
print(sys.path)

with open('data/gwas_catalog-ancestry_r2019-03-22.tsv', 'r') as f:

    for line in f.readlines()[1:]: #ignores the first line
        line = line.replace("\n", "")

        full_name = line.split('\t')

        study_accession = full_name(0)
        pubmedid = full_name(1)
        author = full_name(2)
        date = full_name(3)
        initial_sample_description = full_name(4)
        stage = full_name(5)
        number_of_individuals = full_name(6)
        broad_acenstral_category = full_name(7)
        country_of_origin = full_name(8)
        country_of_recruitment = full_name(9)
        additional_ancestry_description = full_name(10)

        p = gwas_catalogue_ancestory(country=study_accession, continent=pubmedid,
                                     author=author, date=date, initial_sample_description=initial_sample_description,
                                     stage=stage, number_of_individuals=number_of_individuals, broad_acenstral_category=broad_acenstral_category,
                                     country_of_origin=country_of_origin, country_of_recruitment=country_of_recruitment, additional_ancestry_description=additional_ancestry_description)
        p.save()
        #print(full_name[0])
