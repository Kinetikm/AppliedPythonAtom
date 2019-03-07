#!/usr/bin/env python
# coding: utf-8

     
def advanced_calculator(input_string):
     #raise NotImplementedError
     if (is_bracket_correct(input_string)==False):
          return None
     print()
     print(input_string)
     symbols="+-*/(). 0123456789"
     for i in input_string:
          if i not in symbols:
               #print("плохой символ ",i)
               return(None)
     input_string=input_string.replace ("-- ", "+")
     input_string=input_string.replace ("--", "")
     input_string=input_string.replace ("++", "")
     input_string=input_string.replace ("+-", "-")
     input_string=input_string.replace ("+ -", " - ")
     input_string=input_string.replace ("- -", " + ")
     print(input_string)
     pol=norm_into_pol(input_string)
     print("Pol ",pol)
     if (pol=="!!!"):
          return(None)
     elif (type(pol)==str):
        a=polish_write(pol)
        print(a)
        return(a)
     else:
          return(None)

def is_bracket_correct(input_string):
     stack=[]
     for letter in input_string:
          if letter=="(":
               stack.append("(")
          elif letter=="[":
                    stack.append("[")
          elif letter=="{":
               stack.append("{")
          else:
               try:
                    if letter==")":
                         if stack.pop()!='(': 
                              stack.append(")")
                    elif letter=="]":
                         if stack.pop()!="[":
                              stack.append("]")
                    elif letter=="}":
                         if stack.pop()!="{":
                              stack.append("}")
                    else:
                         pass
               except:
                    return False
     try:
          stack.pop()
          return False
     except:
          return True


def polish_write(input_string):
     operators = {"+", "-", "*", "/"}
     stack = []
     string=input_string
     string=string.replace ("()","")
     string=string.replace ("+", " + ")
     string=string.replace ("-", " - ")
     string=string.replace ("*", " * ")
     string=string.replace ("/", " / ")
     string=string.replace ("  ", " ")
     print(string)
     for sym in string.split():
          if (sym in operators):
               try:
                    b = stack.pop()
                    a = stack.pop()
               except:
                    return(None)
               if sym == "+":
                    res = a+b
               elif sym == "-":
                    res = a-b
               elif sym == "*":
                    res = a*b
               elif sym == "/":
                    if (b == 0):
                         return (None)
                    else:
                         res = a/b
               else:
                    return (None)
               stack.append(res)
          else:
               try:
                    stack.append(float(sym))
               except:
                    return None
     print(stack)
     if (len(stack)==1):
          return stack.pop()
     else:
          return(None)

def norm_into_pol(input_string):
     input_string=input_string+"|"
     input_string=input_string.replace ("--", "")
     input_string=input_string.replace (". ", ".0 ")
     input_string=input_string.replace (" .", " 0.")
     input_string=input_string.replace ("+", " + ")
     input_string=input_string.replace ("-", " - ")
     input_string=input_string.replace ("*", " * ")
     input_string=input_string.replace ("/", " / ")
     if (input_string.find("/n",0,len(input_string)-1)!=-1 or input_string.find("()",0,len(input_string)-1)!=-1):
          return("!!!")
     l1=list() #k
     l2=list() #m
     lv=""
     i=0
     while(i<=len(input_string)):
          letter=input_string[i]
          # print()
          # print("eto l1", l1)
          # print("eto l2", l2)
          # print("eto letter",letter)
          # print("eto lv",lv)
          if (letter ==")"):
               if (lv=="|"):
                    return("!!!") #5
               elif (lv=="("): #3
                    if (len(l2)>0):
                         lv=l2.pop()
                         if (lv=="("):
                              lv=""
                         i+=1
                    else:
                         i+=1
                         lv=''
                    
                  
               else: #2
                    l1.append(lv)
                    if (len(l2)>0 and lv!=""):
                         lv=l2.pop()
                         if (lv=="(" and len(l2)>0 ):
                              lv=""
                    else:
                         lv=""
                         i+=1
               
          elif (letter =="+" or letter=="-"):
               if (lv=="|" or lv=="("): #1
                    l2.append(lv)
                    lv=letter  
                    i+=1
                    #l1.append(letter)
               elif (lv==""):
                    lv=letter; 
                    i+=1   
               else: #2
                    l1.append(lv)
                    if (len(l2)>0):
                         lv=l2.pop()
                    else:
                         lv=""
                    #i+=1 #!
     
          elif (letter =="*"  or letter =="/"):
               if (lv=="*" or lv=="/"): #2
                    l1.append(lv)
                    if (len(l2)>0):
                         lv=l2.pop()
                         i+=1 #!
                    else:
                         lv=""
               elif(lv!=""): #1
                    l2.append(lv)
                    lv=letter 
                    i+=1 
               else:
                    lv=letter
                    #l1.append(letter)
                    i+=1
          
          elif (letter =="|"):
               if (lv=="|" or lv=="" and len(l2)==0): #4
                    l2.reverse()
                    result_string="".join(l1)
                    return (result_string)
               elif (lv=="("): #5
                    return("!!!")
               else: #2
                    print("END")
                    l1.append(lv)
                    if (len(l2)>0):
                         #lv=l2.pop()
                         #l1.append(lv)
                         l2.reverse()
                         for li in l2:
                              if (li==")" or li=="(") :
                                   return("!!!")
                              else:
                                   l1.append(li)
                    result_string="".join(l1)
                    return (result_string)
     
          elif(letter=="("):
               if(lv==""):
                    lv="("
               else:
                    l2.append(lv)
                    lv=letter
               i+=1

          else:
               l1.append(letter)
               i+=1
          if ( letter ==" " and lv=="" and len(l2)!=0):
               lv=l2.pop()
          
     print()
     print("eto l1", l1)
     print("eto l2", l2)
     print("eto letter",letter)
     print("eto lv",lv)
