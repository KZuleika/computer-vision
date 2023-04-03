from gtts import gTTS
from playsound import playsound
NOMBRE_ARCHIVO = "sonido_generado.mp3"
tts = gTTS('Hola mundo. Este Es un Ejemplo de Conversion de Texto a Voz.', lang='es-us')
# Nota: podríamos llamar directamente a save
with open(NOMBRE_ARCHIVO, "wb") as archivo:
    tts.write_to_fp(archivo)

playsound(NOMBRE_ARCHIVO)
