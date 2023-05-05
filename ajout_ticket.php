<!DOCTYPE html>
<html>
  <head>
    <title>Ajouter un ticket</title>
    <link rel="stylesheet" href="style.css">
  </head>
  <body>
    <header>
      <nav>
        <ul>
          <li><a href="index.php">Accueil</a></li>
          <li><a href="ajout_ticket.php">Ajouter un ticket</a></li>
          <li><a href="recherche_ticket.php">Rechercher les tickets</a></li>
          <li><a href="afficher_tickets.php">Afficher les tickets</a></li>
        </ul>
      </nav>
    </header>
    <main>
      <h1>Ajouter un ticket</h1>
      <?php
        if ($_SERVER["REQUEST_METHOD"] == "POST") {
          // Récupération des données du formulaire
          $nom = $_POST["nom"];
          $prenom = $_POST["prenom"];
          $email = $_POST["email"];
          $nomticket =$_POST["nomticket"];
          $description = $_POST["description"];

          
          file_put_contents("Odoo/commentaire.txt", $description);


			    $arg = $nomticket." ".$prenom."_".$nom." ".$email;
			    $output = shell_exec("C:/Users/arman/AppData/Local/Microsoft/WindowsApps/python3.9.exe Odoo/ticket.py ".'create_ticket '.$arg);
          echo $output; 
			



          // Affichage d'un message de confirmation
          echo "<p>Le ticket a été ajouté avec succès !</p>";
        } else {
          // Affichage du formulaire d'ajout de ticket
          echo '
            <form method="post" action="ajout_ticket.php">
              <label for="nom">Nom :</label>
              <input type="text" id="nom" name="nom" required><br>
              <label for="prenom">Prénom :</label>
              <input type="text" id="prenom" name="prenom" required><br>
              <label for="email">Adresse email :</label>
              <input type="email" id="email" name="email" required><br>
              <label for="nomticket">Id ticket :</label>
              <input type="text" id="nomticket" name="nomticket" required><br>
              <label for="description">Description du problème :</label><br>
              <textarea id="description" name="description" rows="5" cols="50" required></textarea><br>
              <button type="submit">Ajouter le ticket</button>
            </form>
          ';
        }
      ?>
    </main>
    <footer>
		<p>&copy; 2023 Projet Odoo</p>
	</footer>
  </body>
</html>
