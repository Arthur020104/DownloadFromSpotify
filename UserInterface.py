import tkinter as tk
from tkinter import filedialog, messagebox,ttk
from SpotifiDownload import DownloadFromPlaylist

def browse_folder_path():
    folder_path = filedialog.askdirectory()
    folder_path_entry.delete(0, tk.END)
    folder_path_entry.insert(0, folder_path)

def process_data():
    text_input = text_input_entry.get()
    folder_path = folder_path_entry.get()

    if text_input == "" or folder_path == "":
        messagebox.showerror("Erro", "Necessário preencher todos os campos.")
    else:
        code, message = DownloadFromPlaylist(folder_path,text_input)
        if code:
            messagebox.showerror("Erro", message)
        else:
            messagebox.showinfo("Sucesso",message)

root = tk.Tk()
root.title("Download de playlist Spotify")
root.geometry("800x450")
root.configure(bg="#000000")  # Set the background color of the root window

# Create text input label and entry
text_input_label = tk.Label(root, text="Link da playlist:", bg="#000000", fg="white", font=("Helvetica", 12))
text_input_label.pack()
text_input_entry = tk.Entry(root, font=("Helvetica", 12), bg="#000000", fg="white")
text_input_entry.pack()

# Create folder path input label, entry, and browse button
folder_path_label = tk.Label(root, text="Selecione o caminho da pasta:", bg="#000000", fg="white", font=("Helvetica", 12))
folder_path_label.pack()
folder_path_entry = tk.Entry(root, font=("Helvetica", 12), bg="#090909", fg="white")
folder_path_entry.pack()
folder_path_button = tk.Button(root, text="Procurar", command=browse_folder_path, bg="#1A1A1A", fg="white", font=("Helvetica", 12,"bold"))
folder_path_button.pack()

# Create a button to process the data
process_button = tk.Button(root, text="Fazer Download", command=process_data, bg="#1A1A1A", fg="white", font=("Helvetica", 12,"bold"))
process_button.pack()

# Start the Tkinter event loop
root.mainloop()