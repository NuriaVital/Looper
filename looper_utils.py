import random
from Bio import Entrez
from Bio import Medline
Entrez.email = "nuria.vital@looper.org.il"


def choose_random_subjects(current_area_of_reasearch, current_cancer_type, current_selected_subjects):
    n_random_subjects_per_category = 1
    chosen_reasearch_subjects = [current_area_of_reasearch]
    # if current_cancer_type != 'nan':
    #     chosen_reasearch_subjects += [current_area_of_reasearch]
    
    if len(current_cancer_type) > n_random_subjects_per_category:
        chosen_reasearch_subjects += random.sample(current_cancer_type, n_random_subjects_per_category)
    elif len(current_cancer_type) > 0:
        chosen_reasearch_subjects += current_cancer_type
    
    if len(current_selected_subjects) > n_random_subjects_per_category:
        chosen_reasearch_subjects += random.sample(current_selected_subjects, n_random_subjects_per_category)
    elif len(current_selected_subjects) > 0 :
        chosen_reasearch_subjects += current_selected_subjects
    
    return chosen_reasearch_subjects


def pubmed_search(search_term, n_requested_papers):

    # search articles
    handle = Entrez.esearch(db="pubmed", term=search_term, retmax=n_requested_papers)
    record = Entrez.read(handle)
    idlist = record["IdList"]

    # download articles
    handle = Entrez.efetch(db="pubmed", id=idlist, rettype="medline")
    records = Medline.parse(handle)
    records = list(records)

    return records


def generate_reading_list(article_records, header): 
    
    reading_list = header
    reading_list += '\n'
    reading_list += '-------------\n'

    for record in article_records:
        title = record.get("TI", "?")
        authors = record.get("AU", "?")[:10]
        authors = ", ".join(authors)
        source = record.get("SO", "?")
        
        reading_list += title + '\n'
        reading_list += authors + '\n'
        reading_list += source + '\n'
        reading_list += '\n'

    return reading_list



def assemble_message_text(reading_list, current_name):
    message_text = f"""Hi {current_name},
we are pleased to update you on the new exciting research from you ares of interesrt:

{reading_list}

Best regards,
the Looper team"""
    
    return message_text
