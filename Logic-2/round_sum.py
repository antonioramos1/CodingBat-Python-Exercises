def round_sum(a, b, c):
    def round10(num):
       if num % 10 >= 5:
           num += (10 - (num % 10))
       num -= (num % 10)
       return num
  
    sum_rounded_abc = round10(a) + round10(b) + round10(c)
    return round10(sum_rounded_abc)
    
