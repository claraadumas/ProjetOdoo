<!DOCTYPE html>
<html>
  <head>
    <title>recherche_ticket</title>
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
  </body>

  <main>
      <h1>Recherche les tickets</h1>
      <?php

      if ($_SERVER["REQUEST_METHOD"] == "POST") {
        // Récupération des données du formulaire
       
        $nomticket =$_POST["nomticket"];
       

        
   


        $arg = $nomticket;
        $output = shell_exec("C:/Users/arman/AppData/Local/Microsoft/WindowsApps/python3.9.exe Odoo/ticket.py ".'chercher_ticket '.$arg);
        echo $output; 




        // Affichage d'un message de confirmation
        echo "<p>Le ticket a été ajouté avec succès !</p>";
      } else {
        // Affichage du formulaire d'ajout de ticket
        echo '
          <form method="post" action="recherche_ticket.php">
            <label for="nomticket">Id ticket :</label>
            <input type="text" id="nomticket" name="nomticket" required><br>
            <button type="submit">Chercher le ticket</button>
          </form>
        ';
      }
        
      
      ?>

</main>
  <footer>
		<p>&copy; 2023 Projet Odoo</p>
	</footer>
</html>