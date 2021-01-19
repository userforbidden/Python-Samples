def merge(words,more):
    sentence = []
    [sentence.append(w) for w in words]
    [sentence.append(w) for w in more] 
    return sentence

if __name__ == "__main__":
    words = ['Hello','world']
    more = ['Tharani', 'Maaneeivaannan']
    print(merge(words,more))