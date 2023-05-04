<!DOCTYPE html>
<html>
  <head>
    <title>Accueil</title>
    <link rel="stylesheet" href="style.css">
  </head>
  <body>
    <header>
      <nav>
        <ul>
          <li><a href="index.php">Accueil</a></li>
          <li><a href="ajout_ticket.php">Ajouter un ticket</a></li>
          <li><a href="afficher_tickets.php">Afficher les tickets</a></li>
        </ul>
      </nav>
    </header>
    <main>
      <h1>Bienvenue sur le site de gestion de tickets</h1>
      <p>Cliquez sur "Ajouter un ticket" pour ajouter un nouveau ticket ou sur "Afficher les tickets" pour retrouver les tickets existant.

      Les pages php lancent un fichier python present dans le sous dossier Odoo. Dans celui-ci on retrouve les fonctions de recherche de tickets existant et une fonction d'ajout d'un ticket. 
      Pour plus d'information sur les requetes api possibles, suivre le lien suivant : https://www.odoo.com/documentation/16.0/developer/reference/external_api.html
      Enfin, lors du parametrage de la connexion Odoo sur votre propre serveur, il faut changer les identifiants de connexion situes dans le fichier python.
      Il faut egalement changer le lien de l'interpreteur python3 situe dans la page php. 

      </p>
    </main>
    <footer>
		<p>&copy; 2023 Projet Odoo</p>
	</footer>
  </body>
</html>
