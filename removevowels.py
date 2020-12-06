import string
def removeVowel(s):
    for letter in s:
        if letter in 'AEIOUaeiou':
            s=(s.replace(letter,''))

    print(s)
s = input('Enter a string: ')
removeVowel(s)

'''def disemvowel(s):
    return s.translate(None,"aeiouAEIOU")
s = input('Enter a string: ')
disemvowel(s)'''
