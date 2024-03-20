# Looper
By [Nuria Vital](https://nuriavital.github.io/)

Looper is a script that keeps you in the loop of your area of research. 
The script will assist your lab members to keep track on recent updates in your field of research, by sending them a weekly e-mail with relevant new articles, based on thier pre-defiend preferences keywords. 

The program is build out of two companents:
  - A GUI app for generating a database of usernames and their research subjects of interset.
  - A script based on Entrez that searches the Pubmed database and collects articles to fulfil the users' reading wishlist. 

Do the following to run the script:
1. Set the enviroment by installing biopython - 'pip install biopython' or 'pip install -r requirments.txt'
2. Running GUI - run the script by running  'python .\GUI_db_updater.py' at the root directory. 
3. Generate the input file database by- inviting you peers to fill their subjects of interest using the GUI script, this will create a csv file with their names and reading preferences.
4. Running Looper - run the script by running  'python .\looper.py' at the root directory.
5. Running tests - by typing 'pytest' at the root dierctory.
6. The output result of Looper is designed as an E-mail body text and reading list that was intended to be sent by e-mmail, however, it was too combersome to convience gmail to cooporate with python.  
