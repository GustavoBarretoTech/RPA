import os
import shutil


home = os.path.expanduser("~")
downloadsPasta = os.path.join(home, "Downloads")

for arq in os.listdir(downloadsPasta):
    caminho_origem = os.path.join(downloadsPasta, arq)
    
    # Pula se for uma pasta (o robô só quer arquivos)
    if os.path.isdir(caminho_origem):
        continue

    ext = os.path.splitext(arq)[1].lower() 

    # Define o destino baseado na extensão
    destino = None
    if ext == ".pdf":
        destino = os.path.join(home, "Documentos")
    elif ext in [".jpg", ".png", ".jpeg"]:
        destino = os.path.join(home, "Imagens")
    elif ext in [".zip", ".rar", ".7z"]:
        destino = os.path.join(home, "Compactados")

    # Se a extensão for uma das filtradas
    if destino:
        #Se a pasta não existir, o robô cria na hora!
        if not os.path.exists(destino):
            os.makedirs(destino)
        
        shutil.move(caminho_origem, os.path.join(destino, arq))
        print(f"Movido: {arq} -> {destino}")
