# boschinternship
Internship application task at Bosch XC/ENA2 Team.
This project is a Django web application that produces customised polls where users can vote on questions.
	- It includes a home page with an overview about the subject (here Switzerland) with some general information.
	- Polls can be accessed from the home page for users.
	- App administrators can login securely to the platform and generate new polls with their respective choices.
The Django app which displays the homepage is called "swiss", while the app that produces polls is called "polls".

The app needs Python 3.8 and Django to run properly.

** Installation Instructions **

1. Download and install the latest version of Python from https://www.python.org/downloads/

2. Download the source folder of the application "boschintern" from Github and store it on the device/platform.

3. Open command terminal with admin rights and navigate to the directory of the source file, input the following to install pip:
	Unix/MacOS: python3 -m pip install --user --upgrade pip 
	Windows: py -m pip install --upgrade pip

4. Now install Django by inputting the following into the terminal: 
	Unix/MacOS:  python -m pip install Django
	Windows:     py -m pip install Django

6. (Windows only): make sure that running scripts is enabled in the system. Run "Windows Power Shell" as administrator and type "Set-ExecutionPolicy unrestricted". If prompted to agree type in "Y". Check that it is changed to unrestricted by running "Get-ExecutionPolicy"

5. By default, Django is setup with Sqlite3 database. For installing and using other databese types, please refer to "https://docs.djangoproject.com/en/4.1/topics/db/"

6. If the database is not installed. Run the following command from main directory: >> py manage.py migrate

7. Create superuser by running the following command from the main directory:  
	7.1 Windows: py manage.py createsuperuser >> Username: sami. Email: (can be left blank). Password: sami1359


** Runnig the application **

1. In the command terminal, navigate to directory of the source folder "boschintern"

2. Launch the application with the following command: 
	Unix/MacOS:  python manage.py runserver
	Windows:     py manage.py runserver

3. The output should be as follows:
	Watching for file changes with StatReloader
	System check identified no issues (0 silenced).
	Current Date - Time
	Django version 4.1, using settings 'boschintern.settings'
	Starting development server at http://*localhost*:8000/

4. Run any web browser an go to the URL in the last line of the output http://*localhost*:8000/

5. Now the HOME page of the application should appear.

6. To stop the server, press cmd/ctrl + break. The server can be run again with the ">> py manage.py runserver" command.



** Editing polls and user credentials **

1. In the browser go the administrator webpage URL: "http://127.0.0.1:8000/admin"

2. Input the username and password: sami, sami1359. A "Django administration" page should open.

3. In the POLLS menu, clicking on Questions/Choices will display all the current Polls/Choices stored in the database.

4. In the POLLS menu, the admin can ADD/Change polls and choices from the respective icons on the right of the menu.

5. Under AUTHENTICATION AND AUTHORIZATION, the admin can add user credentials for access to the admin page.



** Viewing polls **

Through the navigation menu in the black box at the top of the HOME page, click on POLLS to view all polls available in the application.

** Editing Contact Us address **


1. With any text editor, open the file "index.html" located in the directory "..\boschintern\polls\templates".

2. Navigate to line 55    <a href="mailto:m@gmail.com">Contact Us</a>

3. Replace the "m@gmail.com" with desired contact email.
