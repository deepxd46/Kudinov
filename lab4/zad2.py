def eti_slowa(predlozhenie1, predlozhenie2):
    slowa1 = set(predlozhenie1.lower().split())
    slowa2 = set(predlozhenie2.lower().split())

    eti = slowa1.intersection(slowa2)
    return eti 

slowa1 = "Солнце светит ярко в небе"
slowa2 = "В небе плывут яркие облака"

eti = eti_slowa(slowa1, slowa2)
print("Слова, которые есть в обоих предложениях:", eti)

