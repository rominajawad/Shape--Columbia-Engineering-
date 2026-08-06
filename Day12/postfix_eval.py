def postfix_eval(expr):
  s = []
  for token in expr:
    if isinstance(token,int):
      s.append(token)
    elif isinstance(token,str):
      rval = s.pop()
      lval = s.pop()
      # apply an operator
      if token == '+':
        s.append(lval+rval)
      elif token == '-':
        s.append(lval-rval)
      elif token == '*':
        s.append(lval*rval)
      elif token == '/':
        s.append(lval//rval)
      else:
        return None
    else:
        return None
  return s.pop()

if __name__ == '__main__':
  x = [ 5, 3, '+', 2, '*']
  print(postfix_eval(x))