# Looper
By [Nuria Vital](https://nuriavital.github.io/)

Looper is a script that keeps you in the loop of your area of research. 
The script will assist my lab members to keep track on recent updates in the cancer proteomics field, by sending them a weekly e-mail with relevant new articles, based on thier pre-defiend preferences keywords. 

The script will include the following elements:
1. Each user will define a set of keywords of interest (i.e 'Proteomics', 'Cancer', 'Ovarian Cancer', 'mass-spectrometry' ect.) 
2. The set of users and their interest keywords will be stored in an Excel file.
4. The script will use Entrez package to inquire the PubMed database and fetch relevant new articles per user.
5. The script will send an E-mail to every user with a thier own list of articles of interest.
6. The script will add all new articles to the Lab's shared excel file, in order to enable all other lab-memebrs to be up to date as well.
7. The script will be configured to run every thursday morning, in order to supply an interesting reading material for the weekend :)

additional optional features-
1. GUI for setting up the keywords preferances per user. 
2. Updates of top priorities articles sent to the lab Slack 'Jornal club' channel.
