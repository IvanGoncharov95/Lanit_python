def dash (n):

   return '' if n<=0 else '-'+dash(n-1)

print(dash(int(input('введите количество тире: '))))