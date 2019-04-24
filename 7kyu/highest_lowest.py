ef high_and_low(num):
  num = num.split()
  num = [int(i) for i in num]
  return str(max(num))+" "+str(min(num))
