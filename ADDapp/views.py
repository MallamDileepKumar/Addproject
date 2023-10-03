from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
def add(request):
    res = HttpResponse("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>ADDapp</title>
</head>
<body bgcolor="cyan">
<form action="./output" method="">
    first number:<input type="number" name="t1">
    second number:<input type="number" name="t2"><br>
    <button type="submit">ADD</button>
</form>

</body>
</html> """)
    return res
def output(request):
    v1 = int(request.GET['t1'])
    v2 = int(request.GET['t2'])
    res1 = v1+v2
    return HttpResponse("The addition two number is " + str(res1))
