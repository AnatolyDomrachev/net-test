<html>
 <head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>123</title>
 </head>
 <body>

<form name="test" method="post" action="input.php">

<?php
$fin = file("all_labs.txt");
//print_r($fin[2][0]);
$i=0;
foreach($fin as $str)
{
	if($str[0] == '*')
	{

		$str[0] = ' ';
		$buf['qws'] = trim($str);
		$i++;
		$j=0;
	}

	if($str[0] == '-' or $str[0] == '+' )
	{
		$str[0] = ' ';
		$buf2[$j] = trim($str);
		$j++;
		$buf['ans'] = $buf2;
	}

	if(isset($buf))
	$qwest[$i] = $buf;

}

//print_r($qwest[1]);

$i = 0;
foreach($qwest as $qws)
{
	$num[$i] = $i;
	$i++;
}

shuffle($num);

$i = 0;
foreach($qwest as $qws)
{
	echo "<b>".$qwest[$num[$i]]['qws']."</b>";
	echo "<p>";
	foreach($qwest[$num[$i]]['ans'] as $answer)
	{
		echo "<input type=radio name = a[$i] value = \"$answer\"> $answer <p>";
	}
	$i++;
	echo "<p>";
}

?>


<input type=submit>

 </body>
</html>
