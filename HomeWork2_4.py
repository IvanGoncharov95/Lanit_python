s = (input(" "))
symbols = 0
words = s.split()
num_words = len(words)
print(num_words)
for line in s:
    symbols += len(line.split())
print(symbols)

