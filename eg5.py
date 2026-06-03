text = "python programming"
count = 0

for ch in text:
    if ch in "aeiou":
        count = count + 1

print("Total vowels =", count)