#write a program to find the factorial of a nummber
def fact(n):
  if n==1 or num==0:
    return 1
  else:
    return n*fact(n-1)
  n = int(input())
  result = fact(n)
  if(n==result):
    print(f"{n} is Factorial")
  else:
    print(f"{n} is not a Factorial")
