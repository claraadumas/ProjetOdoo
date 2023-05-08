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
       

        
   

        $file = 'Odoo/data.json'; 
        $ecritureBDD = array('ticket' => $nomticket);
        file_put_contents('Odoo/data.json', json_encode($ecritureBDD));


        $output = shell_exec("C:/Users/arman/AppData/Local/Microsoft/WindowsApps/python3.9.exe Odoo/ticketCopie.py ".'chercher_ticket');
        echo $output; 
        // mettre le contenu du fichier dans une variable
        $data = file_get_contents($file); 
        $tickets = json_decode($data);

        if (count($tickets) > 0) {
          echo '<table>';
          echo '<thead><tr><th>ID Odoo</th><th>Ticket ID</th><th>Prénom Nom</th><th>Email</th><th>Description</th></tr></thead>';
          echo '<tbody>';
          foreach ($tickets as $ticket) {
            echo '<tr>';
            echo '<td>' . $ticket->number . '</td>';
            echo '<td>' . $ticket->name . '</td>';
            echo '<td>' . $ticket->partner_name . '</td>';
            echo '<td>' . $ticket->partner_email . '</td>';
            echo '<td>' . $ticket->description . '</td>';
            echo '</tr>'; 
          }
          echo '</tbody>';
          echo '</table>';

        // Affichage d'un message de confirmation
        echo "<p>Le ticket a bien été récupéré !</p>";

        } else {
          echo '<p>Aucun ticket à afficher pour le moment.</p>';
        }




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