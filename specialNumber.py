def primecollect(prime):
  print("in primecollect")
  p = 2
  while (p * p <= 1000):
    if (prime[p] == True):
      for i in range(p * 2, 1000, p):
        prime[i] = False
    p += 1
  
def diff(prime):
  print("in prime")
  c=0
  for i in range(50,1000001):
    sumf=0
    sumnf=0
    f=1
    s=str(i)
    for j in range(len(s)):
      if(f==1):
        sumf+=int(s[j])
        f=0
      else:
        sumnf+=int(s[j])    
        f=1  
    if(prime[abs(sumf-sumnf)]):
      c+=1
  return c    
def main():
   prime=[True for i in range(1000)]
   prime[0]=False
   prime[1]=False
   primecollect(prime) 
   print("back out")
   c=diff(prime) 
   print(c)  
main()
