__author__ = 'thuejean-charles'
#!/usr/bin/env python
# coding: utf-8
import socket
import Tkinter
import ttk
def server():
        socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #Host = '192.168.0.11' # l'ip locale de l'ordinateur
        #Port = 234         # choix d'un port
        print Host
        print Port
# on bind notre socket :
        socket.bind((Host, Port))

# On est a l'ecoute d'une seule et unique connexion :
        socket.listen(1)

# Le script se stoppe ici jusqu'a ce qu'il y ait connexion :
        client, adresse = socket.accept() # accepte les connexions de l'exterieur
        print "L'adresse",adresse,"vient de se connecter au serveur !"
        while 1:
                RequeteDuClient = client.recv(255) # on recoit 255 caracteres grand max
                if not RequeteDuClient: # si on ne recoit plus rien
                        break  # on break la boucle (sinon les bips vont se repeter)
                print RequeteDuClient,"\a"         # affiche les donnees envoyees, suivi d'un bip sonore

fenetre = Tkinter.Tk()
Var_add_ip=Tkinter.IntVar()
Var_add_port=Tkinter.IntVar()
fenetre.title("Server")
fenetre.minsize(width=400, height=330)
add_ip=ttk.Entry(fenetre, text="adresse du server", textvariable=Var_add_ip)
add_ip.grid(row=0, column=0)
add_port=ttk.Entry(fenetre, text="port", textvariable=Var_add_port)
add_port.grid(row=0, column=1)
Host=Var_add_ip
Port=Var_add_port


Btn_ok=bouton=ttk.Button(fenetre,text="Ok",command= server)
Btn_ok.grid(row=1, column=1)
fenetre.mainloop()