import os
import glob
import shutil

os.chdir(r'D:\\testpython\\testArchivos\\')

dicTipoArchivo= {
    "documentos":["*.pdf","*.docx","*.txt","*.csv"],
    "videos":["*.mp4","*.mkv","*.avi","*.flv"],
    "otros":[]
}

for tipoArchivo in dicTipoArchivo:
    if not os.path.exists(tipoArchivo):
        os.mkdir(tipoArchivo)
    for formato in dicTipoArchivo[tipoArchivo]:
        formatoGlobal=glob.glob(formato)
        for archivo in formatoGlobal:   
            shutil.move(archivo,tipoArchivo)