<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);

include_once 'functions.php';
$pid = getPid();

if ($pid == -1){
    exec("bash /home/pi/3D-Scanner/run.sh", $output, $returnValue);
/*    foreach($output as $value) {
            echo $value."<br />";
        }
        echo "<br />".$returnValue;*/
    header("Location: /");
}
?>
