<?php
	$fin = file("lab1.txt");

	$i=0;
	$j=0;
	$k=0;
	$l=0;
	foreach($fin as $str)
	{
		if($str[0] == '+')
		{
			$str[0] = ' ';
			$true[$i] = $str;
			$i++;
		}
		if($str[0] == '-')
		{
			$str[0] = ' ';
			$false[$j] = $str;
			$j++;
		}
		if($str[0] == '*')
		{
			$str[0] = ' ';
			$qws[$k] = $str;
			$k++;
		}
		if($str[0] == '*' or $str[0] == '+' or $str[0] == '-')
		{
			$str[0] = ' ';
			$all_s[$l] = $str;
			$l++;
		}
	}

	echo "<pre>";
/*
	echo("true");
	print_r($true);
	echo("false");
	print_r($false);
	echo("qws");
 */
	print_r($all_s);

	foreach($all_s as $string)
	{
		if(in_array($string, $qws ))
			echo("<b>".$string."<b><p>");
		if(in_array($string, $true ))
			echo("<font color = green>".$str."<b><p>");
	}
?>
