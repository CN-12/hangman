word = list(input("word please "))
print("게임 시작!")
life = 0
답 = ["_" for i in range(len(word))]
while True:
    print(f"현재 목숨은 {life} {답}")
    check = 0
    if life == 11:
        print("죽음 ㅅㄱ")
        exit()
    kw = input()
    for i in range(len(word)):
        if word[i] == kw:
            답[i] = kw
            check = 1
    if check == 0:
        life += 1
    if word == 답:
        print("맞춤 ㅅㄱ")
        exit()

    