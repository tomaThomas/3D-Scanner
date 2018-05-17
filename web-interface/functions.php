<?php
function getPid() {
    if ($file = fopen("/home/pi/3D-Scanner/LOCK", "r")) {
        if(!feof($file)) {
            $pid = fgets($file);
            echo "<br />pid: ".$pid;
            if (file_exists( "/proc/$pid" )){
                fclose($file);
                return $pid;
            }else{
                unlink("/home/pi/3D-Scanner/LOCK");
            }
        }
        fclose($file);
    }
    return -1;
}
?>