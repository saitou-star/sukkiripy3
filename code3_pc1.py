# (1) price * 1.1 <= 300000   〇
# price × 1.1 が 300000以下であれば

# (2) n = 0　　×
# 

# (3) "gihu" in kansai　〇
# kansai(変数）に gifu（文字列） があれば

# (4) a + b > 60 and day == 3  〇
# a + b が60より大きく、かつ　変数dayが3と等しいければ

# (5) False　〇
# Falseならば

# 1. initial == "K"
# 2. point >= 80 and point < 256  , 80 <= point < 256
# 3. bmi < 20 or bmi > 25   
# 4. year % 4 == 0
# 5. not(day in[28, 30, 31])

# (1)
isError = False
n = 100

if isError == False and n < 100:
    print("いいね！")

# (2)
number = int(input("数値を入力 >>"))
if number % 2 == 0:
    print("偶数です")

else:
    print("奇数です")

# (3)
greeting = input("挨拶を入力 >>")

if greeting == "こんにちは":
    print("ようこそ")

elif greeting == "景気は？":
    print("ぼちぼちです")

elif greeting == "さようなら":
    print("お元気で！")

else:
    print("どうしました？")