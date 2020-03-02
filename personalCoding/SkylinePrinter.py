def myfunc(word):
    Skyline = ""
    for index, letter in enumerate(word):
        if index % 2 == 0:
            Skyline += letter.lower()
        else:
            Skyline += letter.upper()
    return Skyline

print(myfunc('somebiglargestringsomebiglargestringsomebiglargestringsomebiglargestringsomebiglargestringsomebiglargestringsomebiglargestringsomebiglargestringsomebiglargestringsomebiglargestringsomebiglargestring'))