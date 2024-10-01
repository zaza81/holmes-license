from django.urls import reverse
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
import os
import urllib.parse
from django.conf import settings
from .models import Documento
from .forms import UploadFileForm
from .utils import inserimento_metadati, mostra_metadati

def home(request):
    return render(request, 'home.html')

# Upload, download automatico e cancellazione
def upload_file_1(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            add_comment1 = form.cleaned_data.get('add_comment1', False)
            add_comment2 = form.cleaned_data.get('add_comment2', False)

            documento = Documento.objects.create(
                titolo=uploaded_file.name,
                file=uploaded_file
            )
            documento.save()

            # Inserimento dei metadati
            commenti_da_aggiungere = []
            if add_comment1:
                commenti_da_aggiungere.append("diritto d'autore:copia negata")
            if add_comment2:
                commenti_da_aggiungere.append("diritto d'autore:trasformazione negata")

            if commenti_da_aggiungere:
                inserimento_metadati(documento.file.path, commenti_da_aggiungere)

            # Download automatico del file
            file_path = documento.file.path
            try:
                with open(file_path, 'rb') as f:
                    response = HttpResponse(f.read(), content_type='application/force-download')
                    response['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'

                # Rimuovi il file dopo il download
                os.remove(file_path)
                return response
            except IOError as e:
                return HttpResponse(f"Errore di I/O: {e}", status=500)
    else:
        form = UploadFileForm()

    return render(request, "upload1.html", {"form": form})

# Upload, visualizzazione dei metadati e cancellazione
def upload_file_2(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            documento = Documento.objects.create(
                titolo=uploaded_file.name,
                file=uploaded_file
            )
            documento.save()

            # Visualizza i metadati e rimuovi il file
            decoded_filename = urllib.parse.unquote(documento.file.name)
            file_path = os.path.join(settings.MEDIA_ROOT, decoded_filename)

            if os.path.exists(file_path):
                try:
                    metadati = mostra_metadati(file_path)
                    response = render(request, "metadati.html", {
                        "filename": decoded_filename,
                        "metadati": metadati
                    })
                    os.remove(file_path)
                    return response
                except IOError as e:
                    return HttpResponse(f"Errore di I/O durante la visualizzazione dei metadati: {e}", status=500)
            else:
                raise Http404("File non trovato")
    else:
        form = UploadFileForm()

    return render(request, "upload2.html", {"form": form})
