<?php
$x=("Anita lava la tina cooperando con su madre");
$array= explode(" ",$x);
//var_dump($array);
for ($i=0; $i<count($array);$i++){
    $palabra=$array[$i];
    $n=strlen($palabra);
    $c=$n-2;
    for ($j=0; $j<$n-1 ;$j++){
        if ($palabra[$j] == $palabra[$j+1]){
             $c=$c-1;
             //$j=0;
        }     
   }    //var_dump($palabra,$n);
    echo $palabra[0],$c,$palabra[$n-1],' '; 
}
//var_dump($palabra);
?>