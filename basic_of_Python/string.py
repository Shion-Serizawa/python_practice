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
print(word[0])
print(word[-1]) #リング構造みたいになっている。

print(word[0:2]) #out:py

#一部を変えたいとき→コピー
word = "j" + word[1:]
print(word)
print(len(word))