import taglib
import eyed3
import PyPDF2
import docx
import piexif
import piexif.helper
from PIL import Image
import PIL
import PIL.Image
def inserimento_metadati(filename,commento):
  #immagini
  immagini_estensioni = (".jpg", ".jpeg", ".png")
  if filename.endswith(immagini_estensioni):
    img=PIL.Image.open(filename)
    exif_dict = piexif.load(img.info['exif']) if 'exif' in img.info else {'0th': {}, 'Exif': {}, 'GPS': {}, '1st': {}, 'thumbnail': None}
    user_comment = piexif.helper.UserComment.dump(str(commento))
    exif_dict["Exif"][piexif.ExifIFD.UserComment] = user_comment
    exif_bytes = piexif.dump(exif_dict)
    img.save(filename,exif=exif_bytes)
  # documenti docx
  if filename.endswith(".docx"):
    doc = docx.Document(filename)
    core_properties = doc.core_properties
    core_properties.identifier=str(commento)
    doc.save(filename)
  #documenti pdf
  if filename.endswith(".pdf"):
    reader = PyPDF2.PdfReader(filename)
    metadata = reader.metadata
    writer = PyPDF2.PdfWriter()
    new_metadata = {**metadata}
    new_metadata.update({'/Comment': str(commento) })
    writer.add_metadata(new_metadata)
    writer.write(filename)
  # mp3
  if filename.endswith(".mp3"):
    audio = eyed3.load(filename)
    if audio.tag is None:
       audio.initTag()
       audio.tag.comments.set(str(commento))
    audio.tag.save()
   # mp4
  if filename.endswith(".mp4"):
    file = taglib.File(filename)
    file.tags["COMMENT"] = [str(commento)]
    file.save()

def mostra_metadati(filename):
  #immagini
  immagini_estensioni = (".jpg", ".jpeg", ".png")
    
  if filename.lower().endswith(immagini_estensioni):
     img = Image.open(filename)
     if 'exif' in img.info:
        exif_dict = piexif.load(img.info['exif'])
        if piexif.ExifIFD.UserComment in exif_dict['Exif']:
              commento_binario = exif_dict['Exif'][piexif.ExifIFD.UserComment]
              commento = commento_binario[8:].decode('utf-8', errors='replace')
                
              return commento
        else:
                return "Nessun commento EXIF trovato."
     else:
            return "Nessun metadato EXIF trovato."
  
  # documenti docx
  if filename.endswith(".docx"):
    doc = docx.Document(filename)
    core_properties = doc.core_properties
    return core_properties.identifier
  #documenti pdf
  if filename.endswith(".pdf"):
    reader = PyPDF2.PdfReader(filename)
    metadata = reader.metadata
    return metadata
   # mp4
  if filename.endswith(".mp4"):
    
    file = taglib.File(filename)
    if "COMMENT" in file.tags:
        return file.tags["COMMENT"]
    else:
        return "nessun commento"
    
   
  # mp3
  if filename.endswith(".mp3"):
    audio = eyed3.load(filename)
    if audio.tag is not None and audio.tag.comments:
      commenti = []
      for comment in audio.tag.comments:
        commenti.append(comment.text)
    return commenti
  else:
    return "Nessun commento trovato nel file MP3."
  
  


