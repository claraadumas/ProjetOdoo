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
          <li><a href="afficher_tickets.php">Afficher les tickets</a></li>
        </ul>
      </nav>
    </header>
    <main>
      <h1>Afficher les tickets</h1>
      <?php

        $output = shell_exec("C:/Users/arman/AppData/Local/Microsoft/WindowsApps/python3.9.exe Odoo/ticket.py ".'recup_ticket ');

        echo $output;

        
      ?>
    </main>
  </body>
  <footer>
		<p>&copy; 2023 Projet Odoo</p>
	</footer>
</html>
