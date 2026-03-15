#!/usr/bin/python3
all_text = "llgl ooo sss nn ff g"
print(f"String Befor Count ( '{all_text}' )")
print("-"*40)
counts = {}
for char in all_text:
    counts[char] = counts.get(char, 0) + 1

for key,value in counts.items():
    print(f"{key} => {value}")
