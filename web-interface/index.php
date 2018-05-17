<html>
<head>
    <title>3D-Scanner</title>
</head>
<body>
<p>Last <a href="log.txt">stdout</a> | <a href="error.txt">stderr</a></p>
<p><a href="test.png">Testbild</a></p>
<p>Status:
    <?php
    include_once 'functions.php';
    $pid = getPid();
    if($pid == -1) {
        echo "Not running<br /><a href='run.php'>Start</a>";
    } else {
        echo "Running<br />Pid: $pid";
    }
    ?>
</p>
</body>
</html>
