#!/usr/bin/env python

import xmlrpc.client
import sys
import re

url = 'http://localhost:8069'
db = 'ProjetOdoo'
username = 'armand.michaud@hotmail.com'
password = 'arbre1001'


def removeendline(value):
    return ''.join(value.splitlines())






def recuperation_ticket():
    res=models.execute_kw(db, uid, password, 'helpdesk.ticket', 'search_read', [], {'fields': ['number', 'name', 'description','partner_name','partner_email'] })

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
       
        
        

      
def creation_ticket(nom_ticket,description_ticket,nom_partner,email_partner):
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
    common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
    uid = common.authenticate(db, username, password, {})
    # Create a new customer record
    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
    
    fichier = open("Odoo/commentaire.txt", "r")
    description = fichier.read()
    fichier.close()
    

    if len( sys.argv ) > 1:
        if sys.argv[1]=='create_ticket' :   
            creation_ticket(sys.argv[2],description,sys.argv[3],sys.argv[4])
        elif sys.argv[1]=='recup_ticket':
            recuperation_ticket()
        
except:
    print("erreur de connexion")      
    
    
  
   

    
    


