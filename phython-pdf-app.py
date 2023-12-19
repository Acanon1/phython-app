import PyPDF2
from tkinter import filedialog
from tkinter import Tk

def read_pdf(file_path):
    try:
        # crear un objetivo al path del archivo pdf
        with open(file_path, 'rb') as pdfFileObj:
            # crear un lector del PDF
            pdfReader = PyPDF2.PdfReader(pdfFileObj)
            
            # Imprimir el numero de paginas del PDF
            print(f"Number of pages: {len(pdfReader.pages)}")

    except FileNotFoundError:
        print(f"The file at '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

root = Tk()
root.withdraw()

# seleccionar un archivo PDF
file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])

if not file_path:
    print("No file selected. Exiting.")
else:
    # llamar a la funcion para leer el PDF
    read_pdf(file_path)
