<html>
<head>
    <title>3D-Scanner</title>
</head>
<body>
<script>setTimeout(function() { window.location=window.location;},1000);</script>
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
<p><a href="pull.php" target="_blank">Pull changes</a></p>
</body>
</html>
