# # 改行やら
# print('I don\'t know.')
# print("say \"I don't know\".\nHow are you?")
# print(r'C:\name\name')

# # 上下を開けてかつ、改行をしてくれる。
# print("""
# line1
# line2
# line3
# line4
# """)

# #連続文字を掛け算で
# print("Wow! " * 3 + "FGO")

# #長い文字
# s = ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
#      "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")

# print(s)

word = "python"
# print(word[0])
# print(word[-1]) #リング構造みたいになっている。

# print(word[0:2]) #out:py

# #一部を変えたいとき→コピー
word = "j" + word[1:]
print(word)
print(len(word))

##メソッド
s = "My name is Mike. Hi Mike."
print(s)

#何で始まるのか
is_start = s.startswith("X")
print(is_start)

print("######################################")

#前から検索
print(s.find("Mike"))
#最後に出現する箇所
print(s.rfind("Mike"))
#何個あるの？
print(s.count("Mike"))
#最初のみ大文字
print(s.capitalize())
#すべての文字の最初を大文字
print(s.title())
#全部大文字
print(s.upper())
#全部小文字
print(s.lower())

#もじ入れ替え
print(s.replace("Mike","Shion"))

#代入の仕方（format）

# >>> "a is {}".format("a")
# 'a is a'
# >>> "a is {}".format("test")
# 'a is test'
# >>> "a is {}{}{}".format(1,2,3)
# 'a is 123'
# >>> "a is {1}{2}{0}".format(1,2,3)
# 'a is 231
# >>> "My name is {1} {0}".format("Serizawa","Shion")
# 'My name is Shion Serizawa'
# >>> "My name is {1} {0}. Watashi ha {0} {1}".format("Serizawa","Shion")
# 'My name is Shion Serizawa. Watashi ha Serizawa Shion'
# >>> "My name is {name} {family}. Watashi ha {family} {name}".format(family = "Serizawa",name = "Shion")
# 'My name is Shion Serizawa. Watashi ha Serizawa Shion'
# >>> x = str(12)
# >>> type(x)
# <class 'str'>
# >>> x
# '12'

#f-stringの方が処理が速い！！ (python3.6より)
a = 'a'
print(f'a is {a}')
 
x, y, z = 1, 2, 3
print(f'a is {x}, {y}, {z}')
print(f'a is {z}, {y}, {x}')
 
name = 'Jun'
family = 'Sakai'
print(f'My name is {name} {family}. Watashi ha {family} {name}')