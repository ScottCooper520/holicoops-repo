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
5. Push to GitHub.
   a. Go to https://github.com.
   b. Sign in (gmail, Pass: mygithub1)
   c. Create new repo. Call it 'holicoops-repo'
   => https://github.com/ScottCooper520/holicoops-repo.git
6. Hook laptop git repo to GitHub repo.
   type: git remote add origin https://github.com/ScottCooper520/holicoops-repo.git
   type: git push -u origin master
   Got fatal error, but asked for credentials anyway. Seemed to upload fine...
   Possibly because I logged in with gmail but have user name above?

Now add PythonAnywhere
1. Go to: https://www.pythonanywhere.com/
2. Clicked on a Sign up and try it out button.
3. Create a Beginner account. This is a limited, free account.
   - User: scottPy1
   - Pass: python_rsc
   - Email: gmail
   This takes you to theDashboard at: https://www.pythonanywhere.com/user/scottPy1/
   Following only needs to be done once:
   a. Select Account link at top-right of page.
   b. Select API Token.
   My token is: 03f958ffae71ddb7e8fcf7ffcd13a3f3337a4296
   Note: This appears to be a token used to access the PythonAnywhere api. 
   It should be included in the header for API calls. See PAToken.png.
4. Go back to PA Dashboard by clicking on the logo in UL corner.
   a. Choose option to start a bash console.
   Per the tutorial: "Deploying a web app on PythonAnywhere involves pulling down your 
   code from GitHub, and then configuring PythonAnywhere to recognise it and start 
   serving it as a web application. There are manual ways of doing it, 
   but PythonAnywhere provides a helper tool that will do it all for you. 
   Let's install it first:"
   Following are typed into the new bash terminal (has it's own browser tab):
5. type: pip3.6 install --user pythonanywhere
6. type: pa_autoconfigure_django.py https://github.com/ScottCooper520/holicoops-repo.git
   This took a few minutes to run.
   Got an error with my image field since pillow was not installed. So, I will install it via 
   PA bash window, then re-run previous command.
7. type: pip install Pillow
8. type: pa_autoconfigure_django.py https://github.com/ScottCooper520/holicoops-repo.git --nuke
   Added the --nuke option to replace the previous results (else already exists error).
   FYI - Creating virtualenv with Python3.6 (but I have 3.7 installed...)
   Still get image/Pillow error. Tried 'pip3.6 install --user Pillow'
   Result: Requirement already satisfied: Pillow in /usr/lib/python3.6/site-packages (5.2.0)
9. Re-tried above steps with Python3.7 (which I am using locally).
   type: pip3.7 install --user pythonanywhere
   pa_autoconfigure_django.py https://github.com/ScottCooper520/holicoops-repo.git --nuke
   Still fails. Will proceed and see if other fields are OK. [ans: cannot proceed]
At this point, I want to ensure a consistent version of python is used (3.7, 64-bit). have
seen some SO notes that perhaps Pillow is not yet supported for 3.7? But then why no errors
earlier? So, will generate a requirements.txt file that has my local (working) config, and then
repeat steps to push to GitHub and update PA.
Back in Code venv terminal:
10. type: pip freeze > requirements.txt


10. We now need to initialize the PA database (which is different than our previously init'd local DB).
   type: python manage.py createsuperuser
   Error: Can't find manage.py...
   When it does work, will just use same credentials as local admin.
   User: admin
   Pass: django_rsc











