month = int(input("今は何月ですか？ (数字を入力) >>"))

if month in [1, 3, 5, 7, 8, 10, 12]:
    print("31日までありますね")  # ブロック1

else:
    if month != 2:
        print("30日までですね")  # ブロック2

    else:
        print("1年で一番寒い月ですね")  # ブロック3

    print("年が明けてから")

print(f"{month}箇月が過ぎました")

# ブロック1  1.3.5.7.8.10.12 , "31日までありますね" , "{month}箇月が過ぎました"
# ブロック2  4.6.9.11 , "30日までですね" , "年が明けてから" , "{month}箇月が過ぎました"
# ブロック3  2 , "1年で一番寒い月ですね" , "年が明けてから" , "{month}箇月が過ぎました"

