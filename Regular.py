### MODULE RE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
import re

# from string import printable          #!!!!!!
# print(printable)


# text = "<font color=#CC0000>"
# match = re.search(r"(?ai)(\w+)=(#[\da-fA-F]{6})\b", text)
# print(match)
# print(match.group(0,1,2))
# print(match.groups())
# print(match.start(1))
# print(match.end(1))
# print(match.span(2))
# print(match.pos, match.endpos)
# print(match.re)
# print(match.string)

# text = "<font color=#CC0000 bg=#ffffff fuck=#FF2288>"
# match = re.search(r"(?P<key>\w+)=(?P<value>#[\w+]{6})\b", text)
# print(match)
# print(match.re)
# print(match.groupdict())    #Wau metod))
# print(match.lastgroup, match.lastindex)
# print(match.expand(r"\1:\2"))
# print(match.expand(r"\g<key>:\g<value>"))
# mdict_ls = []
# mtuple = tuple()
# for m in re.finditer(r"(?P<key>\w+)=(?P<value>#[\da-fA-F]{6})\b", text):
#     print(m.groups())
#     print(m)
#     mdict_ls += [m.groupdict()]
#     mtuple += tuple(m.groups())
# print(mdict_ls)
# print(mtuple)
# match = re.findall(r"(?P<key>\w+)=(?P<value>#[\da-fA-F]{6})\b", text)
# print(match)
#
# text = "Киев Варшава Одесса Запор Женева"
# list = re.sub(r"\s*(\w+)\s*", r"<option> \1 </option>\n", text)
# print(list)
#
# count = 0
# def replFind(m):
#     global count
#     count += 10
#     return f"<option value='{count}'>{m.group(1).upper().center(15, '_')}</option>\n"
#
# print(re.sub(r"\s*(\w+)\s*", replFind, text))

# text = """Москва
# Казань
# Тверь
# Самара
# Уфа"""
#
# count = 0
# def replFind(m):
#     global count
#     count += 1
#     return f"<option value='{count}'>{m.group(1)}</option>\n"
#
#
# rx = re.compile(r"(?mi)\s*(\w+)\s*")
# list, total = rx.subn(r"<option>\1</option>\n", text)
# list2 = rx.sub(replFind, text)
# print(list, total, list2, sep="\n")
# print(rx.flags)

# a = 10
# b = 5
# print("{a} - {b} = {a - b}")
# a = 10
# b = 5
# print(f'{a} - {b} = {a - b}')
# a = 5
# b = 10
# print(r"{b} - {a} = {b - a}")
# s = r"Последовательность \n используется для переноса строк"
# print(s)
# print(f"{(a:=int(input()))} * {a} = {a*a}")
# print(r'\\\''); print(f"\\\\\\\'")

# (lambda _, d: d(f'{_} * {_} = {_*_}'))(int(input()), print)
# a\n + \nb\n = \nc
# print(rf'{(a:=input())}\n + \n{(b:=input())}\n = \n{int(a)+int(b)}')
# print(r"{}\n + \n{}\n = \n{}".format(a:=input(), b:=input(), int(a)+int(b)))

# text = 'fsdfdsf.mе&r!kX\q<ЫlХювк*ШЛ/PWЖЁRЩ-NнОaбъСНлdй(ф^4{sZjИ`@жЮБF7"ЕoиэП:Ьуь~№[0A+%_сGQv)ё$MuUSТCГя50ЦnДE;9АJ]В'
# print(re.findall(r"(?<=[^ё$MuUSТCГя50ЦnДE;9АJ])(?:\**?)(?=[ШП9В9фвфЛ]*/)", text))

# for match in re.finditer(r"(cat|dog)", "Hi cat and dog live here"):
#     print(match, match.groups(), match.groupdict(), sep='\n')

text = """[ x ]
Набор маркеров 95000-6, 6 цветов в наборе (Набор маркеров 6 цветов
95000-6 )
<https://royaltoys.com.ua/product/nabor-markerov-6-cvetov-95000-6-/>
Количество: 23,50 грн. x 10
Итого: 235 грн.
[ x ]
Набор маркеров 95000-10, 10 цветов в наборе (Набор маркеров 10 цветов
95000-10 )
<https://royaltoys.com.ua/product/nabor-markerov-10-cvetov-95000-10-/>
Количество: 38,54 грн. x 10
Итого: 385,40 грн.
[ x ]
Детский магнитный конструктор LT5003 из 36 деталей (Конструктор LT5003
(12шт) магнитный, 36дет, в кор-ке, 28,5-25-8,5см )
<https://royaltoys.com.ua/product/konstruktor-lt5003-12sht-magnitnyy-36det-v-kor-ke-28-5-25-8-5sm-/>
Количество: 737,90 грн. x 1
Итого: 737,90 грн.
[ x ]
"""

mdict_ls = []
mtuple = tuple()
for m in re.finditer(r"(?s)\[ x \]\n(?P<имя>[\w\W]+?)\n<http.*?во: (?P<цена_за_ед>\d+,?[\d]{0,2}).*?x (?P<количество>\d+)\n.*?го: (?P<сумма>\d+,?[\d]{0,2})", text):
    print(m.groupdict())
