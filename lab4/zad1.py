def naiti_slowa(a):
    slowa = a.split()
    b = []

    for slowo in slowa:
        if len(slowo) > 0 and slowo[0].lower() == slowo[-1].lower():
            b.append(slowo)
    return b 

vvod = "Арена тестировщик карта красная око"
vivod = naiti_slowa(vvod)
print('Слова начинающиеся и заканчивающиеся на одну и ту же букву:', vivod)