def ko_paytma(*sonlar):
    if not sonlar:
        return 0

    natija = 1
    for son in sonlar:
        natija *= son
    return natija


print(ko_paytma(2, 3, 4, 5))