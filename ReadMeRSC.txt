10/10/2018
==========
Using Django/Python/Heroku for Christmas app development.
Starting with https://tutorial.djangogirls.org/en/
To setup virtual environement (from Powershell):
1. cd to C:\Users\scott\OneDrive\Documents\CoopCraft\HoliCoops
2. type: python -m venv myvenv
3. type: myvenv\Scripts\activate
   Actually, opening the python terminal in Code activated it.
   From here on, type commands in Code terminal.
4. Upgraded pip to latest version 18.1 (from within Code terminal):
   type: python -m pip install --upgrade pip
5. Create requirements.txt (in main folder).
6. type: pip install -r requirements.txt
7. Create Django project called 'mysite' (automatically creates file structure):
   django-admin.exe startproject mysite .
   Allowed to install python linter (getting warning massage). It ran:
   c:/Users/scott/OneDrive/Documents/CoopCraft/HoliCoops/myvenv/Scripts/python.exe -m pip install -U pylint
8. Create database (by default it uses sqlite3).
   type: python manage.py migrate
9. Start the web server:
   type: python manage.py runserver
   Can view default page at http://127.0.0.1:8000

At this point, I am veering off of the tutorial to create my own api.
1. Create hss (holiday slideshow) application in project.
   type: python manage.py startapp hss
   This creates an hss folder containing several default files.
2. Tell Django to use our new app.
   type: 'hss', at the bottom of INSTALLED_APPS array in mysite/settings.py.
3. Create the hss model by over-writing the defaults in hss/models.py.
   Not recorded here, see the file for my changes.
4. Add the model to the database. Autogen a migration file.
   type: python manage.py makemigrations hss
   Was instructed to install Pillow to support image field. So I did this:
   type: pip install Pillow
5. Re-type: python manage.py makemigrations hss
   OK. It displayed as expected: 'Create model Slide'.
6. Apply the autogen'd migration file to our database.
   type: python manage.py migrate hss
7. Use Django admin to interact with the database.
   Replace contents of hss/admin.py. See file for results.
8. Look at the model.
   type: python manage.py runserver
   In browser, go to http://127.0.0.1:8000/admin
9. Create superuser so I can log in.
   Since I am using Code terminal to run server, I used PS for following. 
   a. In PS, go to HoliCoops folder. 
   b. Activate virtualenv (type: myvenv\Scripts\activate).
   type: python manage.py createsuperuser
   Username: admin
   Email: admin@admin.com
   Password: django_rsc
10. Now login with these new credentials on the site.
11. Add a couple of Slides (note that image file chooser shows up automatically!).
   Click on + Add button for HSS/Slides.

At this point, the (unfinished) project will be deployed, then finished later.
We are deploying with:
   a. PythonAnywhere (free for small projects).
   b. GitHub.
1. Create Git repository (do this from the HoliCoops folder - from PS venv).
   type:    git init
            git config --global user.name "ScottCooper520"
            git config --global user.email "scottc520@gmail.com"
2. Create .gitignore file (see conyents in file).
3. type: 'git status' regularly to see what has changed.
   This is like looking at DIFFs prior to committing in Tortoise.
4. Save current changes.
   type:    git add --all .
            git commit -m "My HoliCoops app, first commit"
            








