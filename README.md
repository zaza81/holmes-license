-Per iniziare questo progetto si installa la libreria django di python in un ambiente virtuale da terminale Windows con il seguente comando: 
pip install django
-Poi si esegue il comando da terminale: 
django-admin startproject myproject
-Poi ci si sposta nella cartella myproject con il comando da terminale:
cd myproject.
-Poi si esegue il comando da terminale: 
python manage.py startapp myapp.
-Poi si apre l'editor dal terminale Visual Studio Code.
-Poi si creano i file come visualizzato nell' immagine per inserire il codice fornito in Visual Studio Code.
-Poi si instsallano le libreria necessarie con il comando da terminale:
pip install -r requirements.txt. 
-Poi si eseguono questi due comandi da terminale nella cartella myproject :
python manage.py makemigrations
python manage.py migrate
-Infine si esegue il comando da terminale:
python manage.py runserver 8000
![visual studio](https://github.com/user-attachments/assets/18304d98-88d3-4514-8644-ba7f1b3244fe)
