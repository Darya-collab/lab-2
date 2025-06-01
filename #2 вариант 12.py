# -*- coding: utf-8 -*-

'''
Вариант 12. Транзиция и трансверсия

Задача: 
Даны две строки ДНК `s1` и `s2` одинаковой длины. Необходимо вычислить отношение количества транзиций к количеству 
трансверсий между этими строками.


'''

s1 = "GCAACGCAACAAGAAAACCCTTAGGGACTGGATTATTTCGTCGTAGTTGTAGTTATTGGAAGTACGGGCATCAACCCAGTT"
s2 = "TTATCTGACAAGAAAGCCGTCAACGGCTGGATAATTTCGGCGATCGTGCTGGTTACTGGCGGTACGAGTGTTCCTTTGGGT"

# Функция для вычисления отношения транзиций к трансверсиям
def calculate_transition_transversion_ratio(s1, s2):
    transitions = 0
    transversions = 0
    
    # Определяем, какие замены являются транзициями, а какие — трансверсиями
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            # Проверяем, является ли замена транзицией
            if (s1[i] == 'A' and s2[i] == 'G') or (s1[i] == 'G' and s2[i] == 'A') or \
               (s1[i] == 'C' and s2[i] == 'T') or (s1[i] == 'T' and s2[i] == 'C'):
                transitions += 1
            else:
                transversions += 1
    
    # Возвращаем отношение транзиций к трансверсиям
    return transitions / transversions



# Вычисляем отношение транзиций к трансверсиям
ratio = calculate_transition_transversion_ratio(s1, s2)

# Выводим результат
print(ratio)

