Pet App

Start by creating python virtual environment: 

python -m venv env

This will create an env folder in the current directory. To activate the environment: 

source env/Scripts/avtivate

It should look like this: 

![image](https://github.com/pineapplepeachypie/pet_app/assets/126367511/750f38d2-f98c-4985-bfe5-cfcd3d87f21e)

To run the app, type this in the command line: python app.py
Structure of the files:

app.py handles the server and all the route randlers. 
the templates folder contains: base.html, index.html, new.html, and show.html

index.html - '/' main page. 
register.html - '/tasks/register' contains the form to register a new user. 
