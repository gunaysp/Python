def flatten_fonksiyon(l):
    flattened = []
    for i in l:
        if isinstance(i, list):#type belirliyoruz, liste mi değil mi
            flattened.extend(flatten_fonksiyon(i))# eğer listeyse,listeyi açmak için
        else:
            flattened.append(i)#eğer listeyse direk eklenir
    return flattened

liste = [[1, 2, [1, 5, 6]], [7, 8], [3, 4, 9]]
print(flatten_fonksiyon(liste))
print(flatten_fonksiyon(liste[::-1]))