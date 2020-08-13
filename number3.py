# мне не нравится этот вариант с созданием такого списка,надеюсь вы это увидите и сможете предложить изменения
a, b = ["winter", "winter", "spring", "spring", "spring", "summer", "summer", "summer", "eminem's diss AKA Fall",
        "eminem's diss AKA Fall", "eminem's diss AKA Fall", "winter"], {}
for ai, i in enumerate(a):
    b[str(ai + 1)] = str(i)
print(b[input()])
