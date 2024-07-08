import random


# Расшифровка без одинаковых чисел в паре (8=4+4) и без перестановок (7=3+4 и 7=4+3)
def decrypt_key(key):
    result = ""
    for i in range(1, key // 2 + 1):
        for j in range(i, key):
            if key % (i + j) == 0 and i != j:
                result += str(i) + str(j)
    return result


# Расшифровка с одинаковыми числами в паре (8=4+4), но без перестановок (7=3+4 и 7=4+3)
def decrypt_key2(key):
    result = ""
    for i in range(1, key // 2 + 1):
        for j in range(i, key):
            if key % (i + j) == 0:
                result += str(i) + str(j)
    return result


# Расшифровка с одинаковыми числами в паре (8=4+4), и с перестановками (7=3+4 и 7=4+3)
def decrypt_key3(key):
    result = ""
    for i in range(1, key):
        for j in range(1, key):
            if key % (i + j) == 0:
                result += str(i) + str(j)
    return result


key_number = random.randint(3, 20)
print(key_number)

print(decrypt_key(key_number))
print(decrypt_key2(key_number))
print(decrypt_key3(key_number))
