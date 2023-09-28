import emoji

print(emoji.emojize("¡Yo :red_heart: Pyhon!"))

# Cuando intentes correr este ejemplo saldrá un mensaje de error porque no está instalado en el SO la librería "emoji"
# Instalar librerías consume muchos recursos, sobre todo si estamos probando cosas
# Para probar cosas es conveniente usar un "entorno virtual" (o entorno conda).

# Para crear un entorno virtual: python -m venv .env
# Para activar el entorno virtual: .env\Scripts\activate.bat (seleccionar previamente una terminal cmd en vez de bash)
# Para instalar la librería emoji en el entorno virtual: pip install emoji
# Ahora sí puedo ejecutar el programa: python emoji.py (o bien el botón Play. Se tiene que ejecutar en una terminal Python o cmd)
# Por último, para desactivar el entorno virtual tipear en la terminal (cmd): deactivate
