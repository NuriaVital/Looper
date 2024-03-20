import pandas as pd
import looper_utils

n_requested_papers = 7

def main(db_table_location = 'data/looper_db.csv'):
    
    # read looper database file (csv of people + interest topics)
    db = pd.read_csv(db_table_location)

    # go over each line in the db
    for line in db.index:

    #   read the subjects
        current_name = db.loc[line,'Name']
        current_email = db.loc[line,'Email']
        current_area_of_reasearch = str(db.loc[line,'Area of research'])
        current_cancer_type = db.loc[line,'Cancer type'].split(',')
        current_selected_subjects = db.loc[line,'Selected subjects'].split(',')

        print('Personal details: ', current_name, current_email)
        print('Research preferences: ', current_area_of_reasearch, current_cancer_type, current_selected_subjects)

    #   choose randomly of research terms
        chosen_reasearch_subjects = looper_utils.choose_random_subjects(current_area_of_reasearch, current_cancer_type, current_selected_subjects)
        chosen_reasearch_subjects = " ".join(chosen_reasearch_subjects)
        print('Chosen research preferences: ', chosen_reasearch_subjects)

    #   search in pubmed for the kywords and take the first N requested articles
        article_records = looper_utils.pubmed_search(chosen_reasearch_subjects, n_requested_papers)
        print('Number of found articles: ', len(article_records))

    #   generate a reading list
        reading_list = looper_utils.generate_reading_list(article_records, chosen_reasearch_subjects)

        message_text = looper_utils.assemble_message_text(reading_list, current_name)
        print(message_text)

    #   send user an e-mail with the publication list and some text.
        # mail_sender.send_mail(message_text, current_email)

    return message_text

if __name__ == "__main__":
    main()