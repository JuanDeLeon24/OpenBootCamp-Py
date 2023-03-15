import os

# Función para convertir bytes a KB, MB o GB
def tamano_en_formato_humano(tamano_bytes):
    for unidad in ['', 'KB', 'MB', 'GB']:
        if tamano_bytes < 1024.0:
            return f"{tamano_bytes:.2f} {unidad}"
        tamano_bytes /= 1024.0

# Carpeta personal
ruta_base = os.path.join(os.path.expanduser('~'), 'Downloads')

# Iterar sobre todos los directorios y subdirectorios desde la carpeta personal
for ruta, subdirs, archivos in os.walk(ruta_base):
    # Iterar sobre los archivos en cada directorio
    for archivo in archivos:
        ruta_completa = os.path.join(ruta, archivo)
        tamano = os.path.getsize(ruta_completa)
        tamano_formateado = tamano_en_formato_humano(tamano)
        print(f"{ruta_completa} ({tamano_formateado})")

