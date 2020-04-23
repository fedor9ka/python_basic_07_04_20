"""Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной
первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое слово состоит
из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
 Необходимо использовать написанную ранее функцию int_func().
"""


def int_func(word: str):
    test = []
    for i in word:
        if ord(i) in range(97, 123):
            test.append(i)
    if ''.join(test) == word:
        return word.title()


def int_func_1(sentence):
    try:
        return ' '.join(int_func(i) for i in sentence.split())
    except TypeError:
        print('Необходимы слова из маленьких латинских символов')


print(int_func('hgfrbwkbf'))

print(int_func_1('hgfr bw kbf'))
