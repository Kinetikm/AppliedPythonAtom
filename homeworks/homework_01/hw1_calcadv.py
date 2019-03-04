#!/usr/bin/env python
# coding: utf-8

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

def advanced_calculator(input_string):
     raise NotImplementedError
     if (is_bracket_correct(input_string)==False):
        return None
     print()
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

     def norm_into_pol(input_string):
          input_string=input_string+"|"
          input_string=input_string.replace ("--", "")
          l1=list() #k
          l2=list() #m
          lv=""
          i=0
          while(i<len(input_string)):
               letter=input_string[i]
               print()
               print("eto l1", l1)
               print("eto l2", l2)
               print("eto letter",letter)
               print("eto lv",lv)
               if (letter ==")"):
                    if (lv=="|"):
                         return("!!!") #5
                    elif (lv=="("): #3
                         if (len(l2)>0 and lv!=""):
                              lv=l2.pop()
                              if (lv=="("):
                                   lv=""
                         
                    else: #2
                         l1.append(lv)
                         if (len(l2)>0 and lv!=""):
                              lv=l2.pop()
                              if (lv=="("):
                                   lv=""
                         else:
                              lv=""
          
               elif (letter =="+" or letter=="-"):
                    if (lv=="|" or lv=="("): #1
                         l2.append(lv)
                         lv=letter  
                         #l1.append(letter)
                    elif (lv==""):
                         lv=letter;    
                    else: #2
                         l1.append(lv)
                         if (len(l2)>0):
                              lv=l2.pop()
                         else:
                              lv=""
          
               elif (letter =="*"  or letter =="/"):
                    if (lv=="*" or lv=="/"): #2
                         l1.append(lv)
                         if (len(l2)>0):
                              lv=l2.pop()
                         else:
                              lv=""
                    elif(lv!=""): #1
                         l2.append(lv)
                         lv=letter  
                    else:
                         lv=letter
                         #l1.append(letter)
               
               elif (letter =="|"):
                    if (lv=="|" or lv==""): #4
                         l2.reverse()
                         result_string="".join(l1)
                         return (result_string)
                    elif(lv=="("): #5
                         return("!!!")
                    else: #2
                         pass
               elif(letter=="("):
                    if(lv==""):
                         lv="("
                    else:
                         l2.append(lv)
                         lv=letter

               else:
                    l1.append(letter)
     

          

def polish_write(input_string):
     operators = {"+", "-", "*", "/"}
     stack = []
     #input_string=input_string.replace ("mult", " * ")
     #input_string=input_string.replace ("divide", " / ")
     #string = ''.join([input_string[i] for i in range(len(input_string)) if i%2==0])
     string=input_string
     #string=string.replace ("()","")
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
     try:
          return stack.pop()
     except:
          return(None)
