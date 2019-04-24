def duplicate_count(text)
  test = text.downcase.split('')
  test.uniq.count { |i| test.count(i) > 1}
end
