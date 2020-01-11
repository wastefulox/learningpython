how_many_s = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for i in how_many_s:
  if hasattr(i, "count"):
    print(i.count("s"))