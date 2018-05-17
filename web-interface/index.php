<html>
<head>
    <title>3D-Scanner</title>
</head>
<body>
<p><a href="log.txt">Last log</a></p>
<p>Status:
    <?php
    include_once 'functions.php';
    $pid = getPid();
    if($pid == -1) {
        echo "Not running";
    } else {
        echo "Running<br />Pid: $pid";
    }
    ?>
</p>
</body>
</html>
