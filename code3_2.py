name = input("あなたの名前を教えてください >>")
print("{}さん、こんにちわ".format(name))
food = input(f"{name}さんの好きな食べ物を教えてください >>")

if food == "カレー":
    print("素敵です。カレーは最高ですよね!!")

else:
    print(f"私も{food}が好きですよ")


print(food);print(name) # ;で区切ると一行で二つの文を書ける