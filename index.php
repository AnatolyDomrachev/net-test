<html>
 <head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>123</title>
 </head>
 <body>
<?php
$fin = file("lab1.txt");
echo "<pre>";
//print_r($fin[2][0]);
$i=0;
foreach($fin as $str)
{
	if($str[0] == '*')
	{
		//if(isset($buf2))

		$str[0] = ' ';
		$buf['qws'] = $str;
		$i++;
		$j=0;
	}

	if($str[0] == '-' or $str[0] == '+' )
	{
		$str[0] = ' ';
		$buf2[$j] = $str;
		$j++;
		$buf['ans'] = $buf2;
	}

	$qwest[$i] = $buf;

}

print_r($qwest);

?>
<form name="test" method="post" action="input.php">

<input type=radio name = a[0] value = 'qwe asd zxc'> qwe asd zxc<p>
<input type=radio name = a[0] value = 'qwe asd zxc0'> qwe asd zxc0<p>
<input type=radio name = a[0] value = 'qwe asd zxc1'> qwe asd zxc1<p>

<input type=radio name = a[1] value = 'qwe asd zxc'> qwe asd zxc<p>
<input type=radio name = a[1] value = 'qwe asd zxc0'> qwe asd zxc0<p>
<input type=radio name = a[1] value = 'qwe asd zxc1'> qwe asd zxc1<p>

<input type=submit>

 </body>
</html>
