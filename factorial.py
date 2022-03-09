<html>
<head>
<script>
<marquee behavior="scroll" direction="left"><p style="color:blue"><font size="+7">Scrolls from right to left.</marquee></p>
<marquee scrolldirection="left"> welcome to the java world</marquee>
function show(){

var i, no, fact;
fact=1;
no=Number(document.getElementById("num").value);
for(i=1; i<=no; i++)  
{
fact= fact*i;
}  
document.getElementById("answer").value= fact;
}
</script>
</head>
<body>
Enter Num: <input id="num">
<button onclick="show()">Factorial</button>
<input id="answer">
</body>
</html>
