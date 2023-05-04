#!/usr/bin/env python
import xmlrpc.client
import sys

 # Authenticate with Odoo
url = 'http://localhost:8069'
db = 'ProjetOdoo'
username = 'armand.michaud@hotmail.com'
password = 'arbre1001'


def authentification():
    infos = {}
    with open('Odoo/conn.txt', 'r') as f:
        for line in f:
            key, value = line.strip().split(' = ')
            infos[key] = value
    return infos
   
 





def recuperation_ticket(infos):
    res=common.execute_kw(infos['db'],infos['uid'], infos['password'], 'helpdesk.ticket', 'search_read', [], {'fields': ['number', 'name'], 'limit': 5})
    print(res)


def creation_ticket(infos,nom_ticket,description_ticket,nom_partner,email_partner):
    nom_partner=nom_partner.replace('_', ' ')
    ticket_data = {
        'name': nom_ticket,
        'description': description_ticket,
        'partner_name':nom_partner,
        'partner_email':email_partner
       
        #'partner_id': 1  # Replace 1 with the ID of the customer associated with this ticket
    }
    infos["erreur"]="a passé"
    common.execute_kw(infos['db'],infos['uid'] , infos['password'], 'helpdesk.ticket', 'create', [ticket_data])
    

try:
    infos=authentification()

    common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
    uid = common.authenticate(infos['db'],infos['username'], infos['password'], {})
    infos['uid']=uid
    # Create a new customer record
    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
    
    fichier = open("Odoo/commentaire.txt", "r")
    description = fichier.read()
    fichier.close()
    

    if len( sys.argv ) > 1:
        if sys.argv[1]=='create_ticket' :   
            
            creation_ticket(infos,sys.argv[2],description,sys.argv[3],sys.argv[4])
        elif sys.argv[1]=='recup_ticket':
            recuperation_ticket(infos)
        
except:
    print(infos['db'],infos['uid'] , infos['password'])
    print("erreur de connexion")      
    
    
  
   

    
    



# f = open('data.txt','w')
# for i in res : 
#     for j in i : 
#         f.write(j+' '+str(i[j])+'\n')
# f.close()       
# f = open('data.txt','r')
# res=f.read()
# print(res)      
#f.close()

