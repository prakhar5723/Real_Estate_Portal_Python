Application Overview (Real Estate Portal) –
The Real Estate Portal would simplify the current manual method using computerized equipment and full-fledged computer applications to meet their needs. The essential information can be retained for a more extended period with convenient storage and management. 
Problem Statement - 
No other scenario like right now will explain the need of the digitally operating real estate companies in the country most of the real estate company works on an offline basis with limited resources and customers to buy and sell their properties.
Problem Solution - 
To increase the scope for a real estate company the company can use a real estate portal operated by the company admin who get the details of the properties from the owners and add them to their portal. So, people from all over the country can have a look at the properties virtually and connect the seller and buyer for a property.

**************************Steps to run the application in Windows*****************************************
Open the project in your IDE
Create Virtual environment
Activate the virtual environment using activate.bat
Go back to the Real_Estate_Portal using cd../..
Run command pip install -r requirements.txt
Install postgresSQL in your system
Create database Real_Estate_Portal_DB from pgadmin
Make the required changes in the database section in the settings.py
Run command pyhton manage.py makemigrations
Run command pyhton manage.py migrate
Run command pyhton manage.py runserver
Ctrl + Click on the link and the application is up and running