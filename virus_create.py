def escribir_programa(nombre_archivo, code):
    with open(nombre_archivo, 'w') as archivo:
        archivo.write("import os, math\n")
        archivo.write("from tkinter import messagebox\n\n")
        archivo.write("v = messagebox.askokcancel('programa malicioso entrante', 'presiona ok para continuar o cancel para cancelar')\n")
        archivo.write("v\n")
        archivo.write("if v == 'ok':\n")
        archivo.write("\tpass\n")
        archivo.write("else:\n")
        archivo.write("\texit()\n")
        archivo.write(f"os.system('{code}')\n")

if __name__ == "__main__":
    code = input("backdor: ")
    nombre_archivo = "programa.py"
    escribir_programa(nombre_archivo, code)
    print(f"Se ha generado el programa '{nombre_archivo}' correctamente.")
    #import os
    #os.system("pip install pyinstaller")
    #os.system("pyinstaller --onefile programa.py")
