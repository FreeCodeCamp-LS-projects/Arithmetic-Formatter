import sys

def arithmetic_arranger(problems, result=False):

  lin1 = ""
  lin2 = ""
  lin3 = ""
  lin4 = ""

#Condition 1: Not more than 5 operations
  if len(problems) > 5 :
    return "Error: Too many problems."
    #sys.exit(0)
  else:
    pass
#    print ("son: ", len(problems), 'operaciones')


#Condition 2: Only numbers?
  a=0
  for i in problems :
    a = a+1
    s = i.split(' ')
    if (s[0].isdigit() is False) or (s[2].isdigit() is False):
        return "Error: Numbers must only contain digits."
        #sys.exit(0)

#Condition 3: Number should be not higher than 9999

    if (int(s[0]) > 9999) or (int(s[2]) > 9999):
        return "Error: Numbers cannot be more than four digits."
        #sys.exit(0)
#Condition 4: only + or -

    if (s[1].find("+")) != -1 or (s[1].find("-")) != -1:
        pass
    else:    
        return "Error: Operator must be '+' or '-'."
        sys.exit(0)
        
#Ordering

    if len(s[0]) < len(s[2]):
        max = len(s[2]) + 2
        min1 = max - len(s[0])
        min2 = max - len(s[2]) - 1
        min3 = max - len(str(eval(i)))
        lin1 += min1 * ' ' + s[0] + '    ' 
        lin2 += s[1] + (min2 * ' ') + s[2] + '    ' 
        lin3 += max * '-' + '    ' 
        lin4 += min3*' ' + str(eval(i)) + '    '

    if len(s[0]) > len(s[2]):
        max = len(s[0]) + 2
        min1 = max - len(s[0])
        min2 = max - len(s[2]) - 1
        min3 = max - len(str(eval(i)))
        lin1 += min1 * ' ' + s[0] + '    ' 
        lin2 += s[1] + (min2 * ' ') + s[2] + '    ' 
        lin3 += max * '-' + '    ' 
        lin4 += min3*' ' + str(eval(i)) + '    '

    if len(s[0]) == len(s[2]):
        max = len(s[0]) + 2
        min1 = max - len(s[0])
        min2 = max - len(s[2]) - 1
        min3 = max - len(str(eval(i)))
        lin1 += min1 * ' ' + s[0] + '    ' 
        lin2 += s[1] + (min2 * ' ') + s[2] + '    ' 
        lin3 += max * '-' + '    ' 
        lin4 += min3*' ' + str(eval(i)) + '    '

  lin1 = lin1.rstrip()
  lin1 += lin1.join("\n")
  lin2 = lin2.rstrip()
  lin2 += lin2.join("\n")
  lin3 = lin3.rstrip()
  lin4 = lin4.rstrip()

  if result:
      lin3 += lin3.join("\n")
      return lin1 + lin2 + lin3 + lin4

  else:
      return lin1 + lin2 + lin3

#return arranged_problems