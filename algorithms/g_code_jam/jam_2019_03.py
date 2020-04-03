def _get_case():
    condition = input() # max, length
    upper_bound, length = map(int, condition.split(" "))
    prods = input()
    encrp_prod = list(map(int, prods.split(" ")))
    return int(upper_bound), int(length), encrp_prod


def _uppercase_alphabet():
    ord_A = ord('A')
    return [chr(ord_A + shift) for shift in range(26)]


def gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


total_case = int(input())
for i in range(total_case):
    upper_bound, length, encry_words = _get_case()
    primes = [0] * (length + 1)
    for index in range(1, length):
        if encry_words[index -1] == encry_words[index]:
            primes[index] = 0
        else:
            primes[index] = gcd(encry_words[index -1], encry_words[index])
    print(primes)

    for index in range(length):
        if primes[index] > 0 and primes[index + 1] == 0:
            primes[index + 1] = encry_words[index] // primes[index]
    print(primes)

    for index in range(length - 1, -1, -1):
        if primes[index + 1] > 0 and primes[index] == 0:
            primes[index] = encry_words[index] // primes[index+1]
    print(primes)

    word_mapping = {int(prime):letter for prime, letter in zip(sorted(set(primes)), _uppercase_alphabet())}
    print(["{}:{}".format(prime, word_mapping[prime]) for prime in sorted(word_mapping)])
    print("Case #{}: {}".format(i+1, "".join([ word_mapping[prime] for prime in primes])))
