# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

str = "Hi! Hello!"

def remove_exclamation_marks(str):
    return str.replace('!', '')
print(remove_exclamation_marks(str))


# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

str = '!Hi!'

def remove_last_em(str):
    if str.endswith("!"):
        return str[:-1]
    else:
        return str
print(remove_last_em(str))

# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"

str = 'Hi! !Hi! Hi!'

def remove_word_with_one_em(str):
    return ' '.join(i for i in str.split() if i.count('!') != 1)
print(remove_word_with_one_em(str))