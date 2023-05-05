#!/usr/bin/env python

import xmlrpc.client  ##bibliothèque permettant de faire des requètes api pour Odoo, voir plus d'information sur le site : https://www.odoo.com/documentation/16.0/developer/reference/external_api.html
import sys
import re


###identifiant de connexion Odoo //A changer 


url = 'http://localhost:8069'  ##adresse du serveur, peut être local ou pas
db = 'ProjetOdoo' ##nom de la base de données
username = 'armand.michaud@hotmail.com' ##adresse mail de connexion
password = 'arbre1001'  ##mot de passe de connexion


def removeendline(value):
    ##permet d'enlever les fins de lignes d'un string
    return ''.join(value.splitlines())



def chercher_ticket(tic):
    ##permet la récupération des tickets avec conditions
    
    res=models.execute_kw(db, uid, password, 'helpdesk.ticket', 'search_read',[[['name', '=', tic]]], {'fields': ['number', 'name', 'description','partner_name','partner_email'] })

    for ticket in res :
        if ticket['name'] != False :
            ticket['name']=removeendline(ticket['name'])
        if ticket['partner_name'] != False :
            ticket['partner_name']=removeendline(ticket['partner_name'])
        if ticket['partner_email'] != False :
            ticket['partner_email']=removeendline(ticket['partner_email'])
        if ticket['description'] != False :
            ticket['description']=removeendline(ticket['description'])
        

        print("-nom du ticket : ", ticket['name'])
        print("nom du demandeur : ", ticket['partner_name'])
        print("email du demandeur : ", ticket['partner_email'])
        print("description de la demande :", ticket['description'])
        
        print("")
       


def recuperation_ticket():
    ##permet la récupération des tickets. Enlève les fin de ligne s'il y en a 
    tic = 'Unticket'
    res=models.execute_kw(db, uid, password, 'helpdesk.ticket', 'search_read',[], {'fields': ['number', 'name', 'description','partner_name','partner_email'] })

    for ticket in res :
        if ticket['name'] != False :
            ticket['name']=removeendline(ticket['name'])
        if ticket['partner_name'] != False :
            ticket['partner_name']=removeendline(ticket['partner_name'])
        if ticket['partner_email'] != False :
            ticket['partner_email']=removeendline(ticket['partner_email'])
        if ticket['description'] != False :
            ticket['description']=removeendline(ticket['description'])
        

        print("-id : ", ticket['name'])
        print("nom du demandeur : ", ticket['partner_name'])
        print("email du demandeur : ", ticket['partner_email'])
        print("description de la demande :", ticket['description'])
        
        print("")
       
        
        


def creation_ticket(nom_ticket,description_ticket,nom_partner,email_partner):
    ##permet la création d'un ticket, prend en paramètre le nom du ticket, sa descrption, le nom du créateur du ticket et son email
    nom_partner=nom_partner.replace('_', ' ')
    ticket_data = {
        'name': nom_ticket,
        'description': description_ticket,
        'partner_name':nom_partner,
        'partner_email':email_partner
        #'partner_id': 1  # Replace 1 with the ID of the customer associated with this ticket
    }
    models.execute_kw(db, uid, password, 'helpdesk.ticket', 'create', [ticket_data])
    

try:
    ##Connexion à l'api
    common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
    uid = common.authenticate(db, username, password, {})
    # Create a new customer record
    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
    
    
    
    ##permet en fonction des arguments passés lors de l'execution du script python d'obtenir le type de requete a effectuer. La récupération des informations se fait dans le print
    if len( sys.argv ) > 1:
        if sys.argv[1]=='create_ticket' :  
            ##permet d'obtenir le commentaire de l'utilisateur
            fichier = open("Odoo/commentaire.txt", "r")
            description = fichier.read()
            fichier.close() 
            creation_ticket(sys.argv[2],description,sys.argv[3],sys.argv[4])
        elif sys.argv[1]=='recup_ticket':
            recuperation_ticket()
        elif sys.argv[1]=='chercher_ticket':
            chercher_ticket(sys.argv[2])
        
except:
    print("erreur de connexion")      
    
    
  
   

    
    


