import customtkinter as ctk
import shutil
import subprocess

# Configuração visual básica
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Abrir Site no Chrome")
        self.geometry("900x900")

        # Localiza o Chrome
        self.chrome_caminho = shutil.which("google-chrome") or shutil.which("chrome")

        # Rótulo de instrução
        self.label = ctk.CTkLabel(self, text="Digite o site (ex: google):")
        self.label.pack(pady=10)

        # Campo de entrada
        self.entry = ctk.CTkEntry(self, placeholder_text="nome do site", width=250)
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", lambda event: self.abrir_site()) # Permite dar Enter

        # Botão
        self.button = ctk.CTkButton(self, text="Abrir no Chrome", command=self.abrir_site)
        self.button.pack(pady=20)

    def abrir_site(self):
        site = self.entry.get()
        if site:
            # Limpa o input como você fez no original
            site = site.replace("https://", "").replace(".com", "")
            
            if self.chrome_caminho:
                subprocess.Popen([self.chrome_caminho, f"https://{site}.com"])
            else:
                print("Chrome não encontrado.")

if __name__ == "__main__":
    app = App()
    app.mainloop()
