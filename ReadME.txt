Open the project in your IDE
change directory to venv
chnage directory to scripts
activate the virtual environment using activate.bat
go back to the Real_Estate_Portal using cd../..
check if all the required pip installations are present using pip freeze
if all the required pip installation are not present, run command pip install -r requirements.txt
install postgresSQL in your system
create database Real_Estate_Portal_DB from pgadmin
make the required changes in the database section in the settings.py
Run command pyhton manage.py makemigrations
Run command pyhton manage.py migrate
Run command pyhton manage.py runserver
Ctrl + Click on the link and the application is up and running


