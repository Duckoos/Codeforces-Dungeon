a = input()
b = input()

dec_a = int(a, 2)
dec_b = int(b, 2)

result = dec_a ^ dec_b

print(bin(result)[2:].zfill(len(a)))

# lmao = "dasdasdhat"
# print("cat".zfill(len(lmao)))      # zfill() pads the output upto a certain length