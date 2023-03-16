import sqlite3
from translate import Translator

conn = sqlite3.connect('db.sqlite')
cursor = conn.cursor()

print("**********************")
print("* App Idiomas Python *")
print("**********************\n")

confirm = input("¿Desea ingresar un dato en ingles a la database ? (s / n): ")

if confirm.lower() == "s":
    
    dato = input("Ingresa un dato en ingles a traducir: ")
    
    traductor = Translator(from_lang = 'en', to_lang = 'es')
    texto = traductor.translate(dato)
    print("La palabra/frase ingresada por el usuario : " + "'" + dato + "'" + " y su traduccion al español es: " + "'" + texto + "'")
       
    autor = input("¿Cual es tu nombre completo? : ")
    
    query = "SELECT * FROM ingles WHERE dato = ?"
    cursor.execute(query, (dato,))
    resultado = cursor.fetchone()
    
    if resultado is None:
    
        cursor.execute("INSERT INTO ingles (dato, traduccion, autor) VALUES (?, ?, ?)", (dato, texto, autor))
        
    else:
        
        print("El dato: '" + dato + "', ya esta en la base de datos ingles")
    
else:
    
    print("No hay dato entrante por parte del usuario, es una lastima")

confirm2 = input("¿Desea traer un dato aleatorio de la database ? (s/n):") 

if confirm2.lower() == "s":
    
    cursor.execute("SELECT * FROM ingles ORDER BY RANDOM() LIMIT 1")
    busqueda = cursor.fetchone()
    print("Dato : " + busqueda[0] + ", Traduccion : " + busqueda[1] + ", Autor : " + busqueda[2])
    
else:
    
    print("No quisistes traer ningun dato aleatorio, que pena \n")
    
conn.commit()
conn.close()

print("********************")
print("* Fin del Programa *")
print("********************")