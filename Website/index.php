<html>
    <head>
        <title>Mijn School</title>
    </head>

    <body>
        <h1>Welcome to my school</h1>
        <ul>
            <?php
            $json = file_get_contents('http://klas-service/');
            $obj = json_decode($json);
            $klassen = $obj->klas;
            foreach ($klas as $klassen) {
                echo "<li>$klas</li>";
            }
            ?>
        </ul>
    </body>
</html>
