# follow these instructions:
# Create a seed.sh file in your project directory
# Place the code below in the file.

#!/bin/bash
rm -rf memoryjournal/migrations
rm db.sqlite3
python3 manage.py migrate
python3 manage.py makemigrations memoryjournalapi
python3 manage.py migrate memoryjournalapi

python3 manage.py loaddata user
python3 manage.py loaddata category
python3 manage.py loaddata items
python3 manage.py loaddata lists
python3 manage.py loaddata list_items
python3 manage.py loaddata inspiration_articles


# Run chmod +x seed.sh in the terminal.
# run ./seed.sh in the terminal to run the commands
