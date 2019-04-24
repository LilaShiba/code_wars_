def is_isogram(s):
  s = s.lower()
  for x in s:
      if s.count(x) > 1:
        return False
  return True
        
