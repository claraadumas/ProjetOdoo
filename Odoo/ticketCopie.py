#!/usr/bin/env python
import xmlrpc.client
import sys
import json

 # Authenticate with Odoo



def authentification():
    infos = {}
    with open('Odoo/conn.txt', 'r') as f:
        for line in f:
            key, value = line.strip().split(' = ')
            infos[key] = value
            
    return infos
   
 
def get_desc():
    fichier = open("commentaire.txt", "r")
    description = fichier.read()
    fichier.close()
    return description

def chercher_ticket(models,infos,tic):
    ##permet la récupération des tickets avec conditions
    
    res=models.execute_kw(infos['db'], infos['uid'], infos['password'], 'helpdesk.ticket', 'search_read',[[['name', '=', tic]]], {'fields': ['number', 'name', 'description','partner_name','partner_email'] })
    ecriture_json("Odoo/data.json",res);
    
    

def recuperation_ticket(models,infos):
    res=models.execute_kw(infos['db'], infos['uid'], infos['password'], 'helpdesk.ticket', 'search_read',[], {'fields': ['number', 'name', 'description','partner_name','partner_email'] })    
        
    ecriture_json("Odoo/data.json",res);


def creation_ticket(models,infos,nom_ticket,description_ticket,nom_partner,email_partner):
    ticket_data = {
        'name': nom_ticket,
        'description': description_ticket,
        'partner_name':nom_partner,
        'partner_email':email_partner
    }
    models.execute_kw(infos['db'],infos['uid'] , infos['password'], 'helpdesk.ticket', 'create', [ticket_data])
    
def recup_json(nom_fichier_json):
    with open(nom_fichier_json) as mon_fichier:
        data = json.load(mon_fichier)

    return data
    
def ecriture_json(nom_fichier_json,infos):
    with open(nom_fichier_json, 'w') as mon_fichier:
        json.dump(infos, mon_fichier)

def main():
    try : 
        infos=authentification()
        try: 
            common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(infos['url']))
            uid = common.authenticate(infos['db'],infos['username'], infos['password'], {})
            models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(infos['url']))
            infos['uid']=uid
            
            if len( sys.argv ) > 1:
                try :
                    if sys.argv[1]=='create_ticket' :  
                        data=recup_json('Odoo/data.json')
                        creation_ticket(models,infos,data['nomticket'],data['description'],data['prenom']+" "+data['nom'],data['email'])
                    elif sys.argv[1]=='recup_ticket':
                        recuperation_ticket(models,infos)
                    elif sys.argv[1]=='chercher_ticket':
                        data=recup_json('Odoo/data.json')
                        chercher_ticket(models,infos,data['ticket'])
                except: 
                    print("erreur lancement fonction")
            else : 
                print("aucun argument passé lors du lancement du programme. argv[2] argument du nom de la fonction à lancer")
                    
                
        except: 
            print("erreur de connexion au serveur")
        
    except : 
        print("problème de lecture du fichier d'authentification")



main()














