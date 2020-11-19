def sign(x):
  if x == 0:
    raise Exception("0 neither positive nor negative")
  elif x > 0:
    return 1
  else:
    return -1


def get_sign_changes(coeffs):
  coeffs = list(filter(lambda x: x != 0, coeffs))
  
  last_sign = sign(coeffs[0])
  sign_changes = 0
 
  for x in coeffs[1:]:
    if sign(x) != last_sign:
      sign_changes = sign_changes + 1

    last_sign = sign(x)

  return sign_changes

def roots(a,b,c,d,e,f):
  sign_changes = get_sign_changes([a,b,c,d,e,f])

  print("sign_changes: " + str(sign_changes))
  if sign_changes == 0 or sign_changes % 2 == 0:
    print("Das Polynom hat eine gerade Anzahl von positiven reellen Wurzeln")
  else:
    print("Das Polynom hat eine ungerade Anzahl von positiven reellen Wurzeln.")

#roots(1,-2,-1,2,1,2)
roots(0,0,0,0,0,0)

