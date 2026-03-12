import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


class NotatnikApp:
    def __init__(self, master):
        self.master = master
        master.title("Prosty Notatnik Pythona")
        self.biezacy_plik = None

        # 1. Pole tekstowe
        self.pole_tekstowe = tk.Text(master, wrap='word', undo=True)
        self.pole_tekstowe.pack(expand=True, fill='both')

        # 2. Utworzenie paska menu
        pasek_menu = tk.Menu(master)
        master.config(menu=pasek_menu)

        # Menu "Plik"
        menu_plik = tk.Menu(pasek_menu, tearoff=0)
        pasek_menu.add_cascade(label="Plik", menu=menu_plik)
        menu_plik.add_command(label="Nowy", command=self.nowy_plik)
        menu_plik.add_command(label="Otwórz...", command=self.otworz_plik)
        menu_plik.add_command(label="Zapisz", command=self.zapisz_plik)
        menu_plik.add_command(label="Zapisz jako...", command=self.zapisz_jako_plik)
        menu_plik.add_separator()
        menu_plik.add_command(label="Wyjście", command=master.quit)

        # Ustawienie nagłówka początkowego
        self.aktualizuj_tytul()

        # Ustawienie minimalnego rozmiaru okna
        master.geometry("800x600")

        # --- Funkcje Obsługi Plików ---

    def aktualizuj_tytul(self):
        """Aktualizuje tytuł okna na podstawie bieżącego pliku."""
        if self.biezacy_plik:
            # Wyświetla tylko nazwę pliku, a nie całą ścieżkę
            nazwa_pliku = self.biezacy_plik.split('/')[-1]
            self.master.title(f"{nazwa_pliku} - Prosty Notatnik Pythona")
        else:
            self.master.title("Bez_nazwy - Prosty Notatnik Pythona")

    def nowy_plik(self):
        """Czyści pole tekstowe i resetuje bieżący plik."""
        self.biezacy_plik = None
        self.pole_tekstowe.delete('1.0', tk.END)
        self.aktualizuj_tytul()

    def otworz_plik(self):
        """Otwiera plik z dysku i wczytuje jego treść."""
        sciezka_pliku = filedialog.askopenfilename(defaultextension=".txt",
                                                   filetypes=[("Pliki tekstowe", "*.txt"), ("Wszystkie pliki", "*.*")])
        if sciezka_pliku:
            try:
                with open(sciezka_pliku, 'r', encoding='utf-8') as plik:
                    zawartosc = plik.read()
                self.pole_tekstowe.delete('1.0', tk.END)
                self.pole_tekstowe.insert('1.0', zawartosc)
                self.biezacy_plik = sciezka_pliku
                self.aktualizuj_tytul()
            except Exception as e:
                messagebox.showerror("Błąd", f"Nie udało się otworzyć pliku: {e}")

    def zapisz_plik(self):
        """Zapisuje bieżący plik. Jeśli plik jest nowy, wywołuje 'Zapisz jako...'."""
        if self.biezacy_plik:
            self._zapisz_zawartosc(self.biezacy_plik)
        else:
            self.zapisz_jako_plik()

    def zapisz_jako_plik(self):
        """Prosi użytkownika o ścieżkę i zapisuje plik pod nową nazwą."""
        sciezka_pliku = filedialog.asksaveasfilename(defaultextension=".txt",
                                                     filetypes=[("Pliki tekstowe", "*.txt"),
                                                                ("Wszystkie pliki", "*.*")])
        if sciezka_pliku:
            self.biezacy_plik = sciezka_pliku
            self._zapisz_zawartosc(sciezka_pliku)

    def _zapisz_zawartosc(self, sciezka):
        """Wewnętrzna funkcja zapisująca treść."""
        try:
            zawartosc = self.pole_tekstowe.get('1.0', tk.END)
            with open(sciezka, 'w', encoding='utf-8') as plik:
                plik.write(zawartosc)
            self.aktualizuj_tytul()
            messagebox.showinfo("Zapisano", f"Plik został zapisany pomyślnie.")
        except Exception as e:
            messagebox.showerror("Błąd", f"Nie udało się zapisać pliku: {e}")


# --- Uruchomienie aplikacji ---
if __name__ == '__main__':
    root = tk.Tk()
    app = NotatnikApp(root)
    root.mainloop()