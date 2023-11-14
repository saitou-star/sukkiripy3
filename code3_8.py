
name = input("あなたの名前を教えて下さい >>")
print(f"{name}さん、こんにちは")

if name == "松田":
    print("松田さんに会えてうれしいです。")

# else文がない
# else文を書かないといけない場合は、「pass」と書く



food = input(f"{name}さんの好きな食べ物を教えてください。 >>")

if "カレー" in food:
    print("素敵です。とにかくカレーは最高ですよね！！")

else:
    print(f"私{food}が好きですよ。")