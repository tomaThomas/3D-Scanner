<html>
<head>
    <title>Pull</title>
</head>
<body>
<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);

exec("bash /home/pi/3D-Scanner/pull.sh", $output, $returnValue);
foreach($output as $value) {
    echo $value."<br />";
}
echo "<br />".$returnValue."<br />";

echo "<a href='/'>Zurück</a>";
?>
</body>
</html>
