def is_prime_number(num):
  if num >= 2:
    for y in range(2, num):
      if not (num % y):
        return False
  else:
    return False
  return True



def prime_gen(num): 
    number_list = []   
    for i in range(0,num):
        if is_prime_number(i):
            number_list.append(i)
    return number_list


