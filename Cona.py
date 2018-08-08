# connection

import pyodbc
con = pyodbc.connect('Trusted_Connection=yes', driver = '{SQL Server}',
                     server = "DESKTOP-EADQI0F", database = "Ospedale di Cona")

#DESKTOP-KHGKJGA\MSSQLSERVER01

queryA = "SELECT DISTINCT * FROM Patient"
queryB = "SELECT * FROM Patient JOIN Doc on Doc.DoctorKey = Patient.DoctorKey WHERE Patient.DoctorKey = 1"
queryC = "SELECT COUNT(*) FROM Patient"


def launchquery (query):  # launch SELECT commands
    cur = con.cursor()
    db_cmd = query
    res = cur.execute(db_cmd)
    for r in res:
        print (r)


benvenuto =("\n\n"            
 "  __                     _       _            _ _    ___ \n"         
 " / _ \                   | |     | |          | ()  / __| \n"              
 "| |  | |_ _ _   __  _| | _ | | __    _| |  | |     _  _ _   _ _ \n"
 "| |  | / _| ' \ / _ \/ ` |/ _` | |/ _ \  / _` | | | |    / _ \| ' \ / _` |\n"
 "| |_| \_ \ |) |  _/ (| | (| | |  _/ | (| | | | |_| () | | | | (| |\n"
  " \__/|_/ ._/ \_|\,|\_,||\_|  \,||  \_\_/|| ||\,|\n\n"
"Benvenuto nell'interfaccia interattiva dell'Ospedale di Cona (FE).\n\n"
      "Buongiorno Dottore."
           )

menu =("\n\nScelga un'operazione da effettuare.\n\n"
      "1: Esamina tutti i pazienti\n"
      "2: Esamina tutti i pazienti del Dr. Rossi\n"
      "3: Conta quanti pazienti segue l'Ospedale\n"
      "4: Cancella un Dottore\n"
      "5: Inserisci un nuovo Dottore \n"
      "6: Aggiorna un Dottore\n"
      "7: Esegui un comando SQL manuale \n"
      "8: Esci dall'interfaccia \n\n"
      "Scelga operazione da effettuare:")


def execA():
    launchquery(queryA)
    return "done A"


def execB():
    launchquery(queryB)
    return "done B"


def execC():
    launchquery(queryC)
    return "done C"


def executechoice(x):
    if int(x) == 1:
        execA()
    else:
        if int(x) == 2:
            execB()
        else:
            if int(x) == 3:
                execC()
            else:
                if int (x) == 4:
                    id = input("Quale dottore vuoi cancellare? Inserisci ID:")
                    c = con.cursor()
                    queryD = "DELETE FROM Doc WHERE DoctorKey = '%s' " % id
                    c.execute(queryD)
                    con.commit()
                else:
                    if int(x) == 5:
                        identifier = input("Inserisci l'ID UNIVOCO che identifica il Dottore")
                        name = input("Inserisci il nome del Dottore")
                        queryI = "INSERT INTO Doc VALUES (%s, '%s')" % (identifier, str(name))
                        c = con.cursor()
                        c.execute(queryI)
                        con.commit()
                    else:
                        if int(x) == 6:
                            id_o= input("Inserisci il vecchio ID")
                            id_n = input("Inserisci il nuovo ID")
                            name = input("Inserisci il nuovo Nome")
                            queryU = "UPDATE Doc SET DoctorKey = %s WHERE DoctorKey =  %s" % (int(id_n), int(id_o))
                            c = con.cursor()
                            c.execute(queryU)
                            con.commit()
                        else:
                            if int(x) == 7:
                                scelta = input("Esplorare o modificare i dati? E / M")
                                if scelta == "M":
                                    queryM = input("Inserisci una query manuale:\n")
                                    c = con.cursor()
                                    c.execute(queryM)
                                    con.commit()
                                else:
                                    queryM = input("Inserisci una query manuale:\n")
                                    launchquery(queryM)
                            else: exit(-1)

def main():
    x = 0
    print(benvenuto)
    while (x != 7):
        print(menu)
        x = input("")
        executechoice(x)

main()