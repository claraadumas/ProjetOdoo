<!DOCTYPE html>
<html>
  <head>
    <title>Afficher les tickets</title>
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
      <h1>Afficher les tickets</h1>
      <?php

        $output = shell_exec("C:/Users/arman/AppData/Local/Microsoft/WindowsApps/python3.9.exe Odoo/ticketCopie.py ".'recup_ticket ');
        echo $output;
        
        $file = 'Odoo/data.json'; 



        // mettre le contenu du fichier dans une variable
        $data = file_get_contents($file); 

        // décoder le flux JSON
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
        } else {
          echo '<p>Aucun ticket à afficher pour le moment.</p>';
        }
        

        
      ?>
    </main>
  </body>
  <footer>
		<p>&copy; 2023 Projet Odoo</p>
	</footer>
</html>
