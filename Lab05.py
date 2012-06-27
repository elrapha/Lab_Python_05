#Problem 2
def factorial(value):
    result=1
    for i in range(value,0,-1):
        result=result*i
    return result
num=5
print num,' Factorial ? ', factorial(num)

#Problem 3
def fibonacci(n):
    result=[1,1]
    if n==1:
        return [1]
    elif n==2:
        return [1,1]
    else:
        for i in range(n-2):
            result.append(result[i]+result[i+1])
    return result
num=5
print 'First ',num,' Fibonacci\t', fibonacci(num)

#Problem 4
from math import sqrt
def prime(num):
    isPrime=False
    if num>=2:
        isPrime=True
        stop=int(sqrt(num))+1
        for i in range(2,stop):
            if num%i==0:
                isPrime=False
                break
    return isPrime
num=9
print num,' is Prime ? ', prime(num) 


#Challenge Problems
#Problem 5
def isPalindrome(instring):
    limit=len(instring)/2
    isPal=True
    for i in range(limit):
        if instring[0+i]!=instring[0-i-1]:
            isPal=False
    return isPal

instring="Able was i ere I saw elba"
print '"'+instring + '" is Palindrome ? ', isPalindrome(instring)

#Problem 6
def isSubstring(instring1,instring2):
    isSub=False
    len1=len(instring1)
    len2=len(instring2)
    limit=len2-len1
    if limit>=0:
        for i in range(limit+1):
            tempstr=instring2[i:len1+i]
            #print tempstr
            if tempstr==instring1:
                isSub=True
                break
    return isSub

str1='maba'
str2='cromabatana'
print '"'+str1 +'" in '+ '"'+str2+'" ? ',isSubstring(str1,str2)
        
#Problem       
def scores(me,fred,jill):
    length=len(me)
    score=0
    for i in range(length):
        if fred[i]==me[i] and jill[i]==me[i]:
            score=score+0
            continue
        elif fred[i]==me[i] or jill[i]==me[i]:
            score=score+1
            continue
        elif fred[i]==jill[i]:
            score=score+2
            continue
        else:
            score=score+1
    return score

me="AAABCDA"
fred="AADBACA"
jill="AACADDC"
print 'score is ', scores(me,fred,jill)
















            
    
    
    
    
    























    
