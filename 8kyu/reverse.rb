def solution(str)
  word=""
  str_split = str.split('')
  while str_split.length >= 1 do
    word << str_split.pop
  end
  return word
end
