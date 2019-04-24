def solve(arr)
  outter = 0
  while outter < arr.length
    inner = 0
    while inner <= arr.length
      if inner == arr.length
        return arr[outter]
      elsif outter == inner || -(arr[outter]) != arr[inner]
        inner += 1
      else
        break
      end
    end
    outter += 1
  end
end
