# Importujemy moduł tkinter do tworzenia GUI
import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox
 
# Tworzymy główne okno aplikacji
root = tk.Tk()
root.title("STG")
root.geometry("400x200")
 
# Tworzymy menu główne
menu = tk.Menu(root)
 
# Tworzymy podmenu help
help = tk.Menu(menu, tearoff=0)
 
# Tworzymy funkcję, która będzie wyświetlać informacje o programie
def about():
    tk.messagebox.showinfo(title="O programie", message="To jest program stowrzony na stegno")
 
# Dodajemy opcję "O programie" do podmenu help
help.add_command(label="O programie", command=about)
 
# Dodajemy podmenu help do menu głównego
menu.add_cascade(label="Help", menu=help)
 
# Skonfigurujemy menu główne jako menu okna głównego
root.config(menu=menu)
 
# Tworzymy funkcję, która będzie wywoływana po kliknięciu pierwszego przycisku
def first_button():
    # Tworzymy nowe okno
    window1 = tk.Toplevel(root)
    window1.title("Pierwsze zadanie")
    # Tworzymy etykiety i pola tekstowe do wprowadzania danych
    label1 = tk.Label(window1, text="Wybierz plik audio:")
    label1.grid(row=0, column=0, padx=10, pady=10)
    entry1 = tk.Entry(window1)
    entry1.grid(row=0, column=1, padx=10, pady=10)
    label2 = tk.Label(window1, text="Wpisz wyraz do ukrycia:")
    label2.grid(row=1, column=0, padx=10, pady=10)
    entry2 = tk.Entry(window1)
    entry2.grid(row=1, column=1, padx=10, pady=10)
    label3 = tk.Label(window1, text="Wpisz nazwę dla wygenerowanego pliku:")
    label3.grid(row=2, column=0, padx=10, pady=10)
    entry3 = tk.Entry(window1)
    entry3.grid(row=2, column=1, padx=10, pady=10)
    # Tworzymy przycisk do wyboru pliku audio
    def browse_file():
        # Używamy filedialog do otwarcia okna dialogowego
        filename = filedialog.askopenfilename(title="Wybierz plik audio", filetypes=[("Pliki audio", "*.mp3 *.wav")])
        # Wstawiamy nazwę pliku do pola tekstowego
        entry1.delete(0, tk.END)
        entry1.insert(0, filename)
    button1 = tk.Button(window1, text="Przeglądaj", command=browse_file)
    button1.grid(row=0, column=2, padx=10, pady=10)
    # Tworzymy przycisk do wykonania zadania
    def execute_task():
        # Pobieramy dane z pól tekstowych
        audio_file = entry1.get()
        word = entry2.get()
        output_file = entry3.get()
        # Sprawdzamy, czy dane są poprawne
        if audio_file and word and output_file:
            # Tutaj należy dodać kod do ukrywania wyrazu w pliku audio i zapisywania go pod podaną nazwą
            # Na przykład:
            # hide_word(audio_file, word, output_file)
            # Pokazujemy komunikat o sukcesie
            tk.messagebox.showinfo("Sukces", "Wygenerowano plik " + output_file)
        else:
            # Pokazujemy komunikat o błędzie
            tk.messagebox.showerror("Błąd", "Wprowadź poprawne dane")
    button2 = tk.Button(window1, text="Wykonaj", command=execute_task)
    button2.grid(row=3, column=1, padx=10, pady=10)
 
# Tworzymy funkcję, która będzie wywoływana po kliknięciu drugiego przycisku
def second_button():
    # Tworzymy nowe okno
    window2 = tk.Toplevel(root)
    window2.title("Drugie zadanie")
    # Tworzymy etykiety i pola tekstowe do wprowadzania danych
    label1 = tk.Label(window2, text="Wybierz plik audio:")
    label1.grid(row=0, column=0, padx=10, pady=10)
    entry1 = tk.Entry(window2)
    entry1.grid(row=0, column=1, padx=10, pady=10)
    label2 = tk.Label(window2, text="Wpisz wyraz do ukrycia:")
    label2.grid(row=1, column=0, padx=10, pady=10)
    entry2 = tk.Entry(window2)
    entry2.grid(row=1, column=1, padx=10, pady=10)
    # Dodajemy etykietę i pole tekstowe do wpisania klucza
    label4 = tk.Label(window2, text="Wpisz klucz:")
    label4.grid(row=2, column=0, padx=10, pady=10)
    entry4 = tk.Entry(window2)
    entry4.grid(row=2, column=1, padx=10, pady=10)
    label3 = tk.Label(window2, text="Wpisz nazwę dla wygenerowanego pliku:")
    label3.grid(row=3, column=0, padx=10, pady=10)
    entry3 = tk.Entry(window2)
    entry3.grid(row=3, column=1, padx=10, pady=10)
    # Tworzymy przycisk do wyboru pliku audio
    def browse_file():
        # Używamy filedialog do otwarcia okna dialogowego
        filename = filedialog.askopenfilename(title="Wybierz plik audio", filetypes=[("Pliki audio", "*.mp3 *.wav")])
        # Wstawiamy nazwę pliku do pola tekstowego
        entry1.delete(0, tk.END)
        entry1.insert(0, filename)
    button1 = tk.Button(window2, text="Przeglądaj", command=browse_file)
    button1.grid(row=0, column=2, padx=10, pady=10)
    # Tworzymy przycisk do wykonania zadania
    def execute_task():
        # Pobieramy dane z pól tekstowych
        audio_file = entry1.get()
        word = entry2.get()
        key = entry4.get()
        output_file = entry3.get()
        # Sprawdzamy, czy dane są poprawne
        if audio_file and word and key and output_file:
            # Tutaj należy dodać kod do ukrywania wyrazu w pliku audio z użyciem klucza i zapisywania go pod podaną nazwą
            # Na przykład:
            # hide_word_with_key(audio_file, word, key, output_file)
            # Pokazujemy komunikat o sukcesie
            tk.messagebox.showinfo("Sukces", "Wygenerowano plik " + output_file)
        else:
            # Pokazujemy komunikat o błędzie
            tk.messagebox.showerror("Błąd", "Wprowadź poprawne dane")
    button2 = tk.Button(window2, text="Wykonaj", command=execute_task)
    button2.grid(row=4, column=1, padx=10, pady=10)
 
# Tworzymy funkcję, która będzie wywoływana po kliknięciu trzeciego przycisku
def third_button():
    # Tworzymy nowe okno
    window3 = tk.Toplevel(root)
    window3.title("Trzecie zadanie")
    # Tworzymy etykiety i pola tekstowe do wprowadzania danych
    label1 = tk.Label(window3, text="Wybierz plik audio:")
    label1.grid(row=0, column=0, padx=10, pady=10)
    entry1 = tk.Entry(window3)
    entry1.grid(row=0, column=1, padx=10, pady=10)
    label2 = tk.Label(window3, text="Wybierz plik do ukrycia:")
    label2.grid(row=1, column=0, padx=10, pady=10)
    entry2 = tk.Entry(window3)
    entry2.grid(row=1, column=1, padx=10, pady=10)
    label3 = tk.Label(window3, text="Wpisz nazwę dla wygenerowanego pliku:")
    label3.grid(row=2, column=0, padx=10, pady=10)
    entry3 = tk.Entry(window3)
    entry3.grid(row=2, column=1, padx=10, pady=10)
    # Tworzymy przyciski do wyboru pliku audio i obrazu
    def browse_audio():
        # Używamy filedialog do otwarcia okna dialogowego
        filename = filedialog.askopenfilename(title="Wybierz plik audio", filetypes=[("Pliki audio", "*.mp3 *.wav")])
        # Wstawiamy nazwę pliku do pola tekstowego
        entry1.delete(0, tk.END)
        entry1.insert(0, filename)
    button1 = tk.Button(window3, text="Przeglądaj", command=browse_audio)
    button1.grid(row=0, column=2, padx=10, pady=10)
    def browse_image():
        # Używamy filedialog do otwarcia okna dialogowego
        filename = filedialog.askopenfilename(title="Wybierz obraz", filetypes=[("Pliki obrazów", "*.jpg *.png *.gif")])
                # Wstawiamy nazwę pliku do pola tekstowego
        entry2.delete(0, tk.END)
        entry2.insert(0, filename)
    button2 = tk.Button(window3, text="Przeglądaj", command=browse_image)
    button2.grid(row=1, column=2, padx=10, pady=10)
    # Tworzymy przycisk do wykonania zadania
    def execute_task():
        # Pobieramy dane z pól tekstowych
        audio_file = entry1.get()
        image_file = entry2.get()
        output_file = entry3.get()
        # Sprawdzamy, czy dane są poprawne
        if audio_file and image_file and output_file:
            # Tutaj należy dodać kod do ukrywania obrazu w pliku audio i zapisywania go pod podaną nazwą
            # Na przykład:
            # hide_image(audio_file, image_file, output_file)
            # Pokazujemy komunikat o sukcesie
            tk.messagebox.showinfo("Sukces", "Wygenerowano plik " + output_file)
        else:
            # Pokazujemy komunikat o błędzie
            tk.messagebox.showerror("Błąd", "Wprowadź poprawne dane")
    button3 = tk.Button(window3, text="Wykonaj", command=execute_task)
    button3.grid(row=3, column=1, padx=10, pady=10)
 
# Tworzymy trzy przyciski na głównym oknie, które będą wywoływać odpowiednie funkcje
button1 = tk.Button(root, text="Pierwsze zadanie", command=first_button)
button1.pack(padx=10, pady=10)
button2 = tk.Button(root, text="Drugie zadanie", command=second_button)
button2.pack(padx=10, pady=10)
button3 = tk.Button(root, text="Trzecie zadanie", command=third_button)
button3.pack(padx=10, pady=10)
 
# Uruchamiamy główną pętlę aplikacji
root.mainloop()
