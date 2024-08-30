import random

print(f"First combination of lock number {random.randint(0,999) :03d}")
sec_comb =str(random.randint(1,6))+str(random.randint(1,6))+str(random.randint(1,6))+str(random.randint(1,6))
print("Second combination of lock number",sec_comb)