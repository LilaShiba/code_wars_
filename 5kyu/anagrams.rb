def anagrams(word, words)
  ans = []
  for x in words do
    if word.chars.sort_by(&:downcase).join == x.chars.sort_by(&:downcase).join
      ans.push(x)
    end
  end
  return ans
end
