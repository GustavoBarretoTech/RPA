import pyautogui as ptg

imagem = "/home/user/Imagens/foto.png"

local_centro = ptg.locateCenterOnScreen(imagem, confidence=0.9, grayscale=True)

if local_centro:
    ptg.click(local_centro)
    print(f"Clique executado.")
else:
    print("Imagem não encontrada na tela.")
