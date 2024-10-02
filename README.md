![visual studio](https://github.com/user-attachments/assets/18304d98-88d3-4514-8644-ba7f1b3244fe)

-Per iniziare questo progetto si installa la libreria django di python in un ambiente virtuale, per esempio conda, da terminale Windows con il seguente comando:<br>
pip install django<br>
-Poi si esegue il comando da terminale: <br>
django-admin startproject myproject <br>
-Poi ci si sposta nella cartella myproject con il comando da terminale: <br>
cd myproject<br>
-Poi si esegue il comando da terminale: <br>
python manage.py startapp myapp<br>
-Poi si apre l'editor dal terminale Visual Studio Code.<br>
-Poi si creano i file come visualizzato nell' immagine per inserire il codice fornito in Visual Studio Code.<br>
-Poi si instsallano le libreria necessarie con il comando da terminale:<br>
pip install -r requirements.txt <br>
-Poi si eseguono questi due comandi da terminale nella cartella myproject : <br>
python manage.py makemigrations <br>
python manage.py migrate <br>
-Infine si esegue il comando da terminale: <br>
python manage.py runserver 8000 <br>

