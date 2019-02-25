def intersect(list1, list2):
  both = sorted(unique(list1) + unique(list2))
  intersections = []
  for i in range(0, len(both)-1):
     if both[i] == both[i+1]:
      intersections.append(both[i])
  return intersections
