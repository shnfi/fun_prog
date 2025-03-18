string = "T4 l16 _36 510 _27 s26 _11 320 414 {6 }39 C2 T0 m28 317 y35 d31 F1 m22 g19 d38 z34 423 l15 329 c12 ;37 19 h13 _30 F5 t7 C3 325 z33 _21 h8 n18 132 k24"

string = string.split(" ")

ans = []
for i in range(50) :
    ans.append("NO WAY")

for i in string :
    _char = i[0]
    _index = int(i[1:])

    ans[_index] = _char

stringed_ans = "".join(ans[0:ans.index("NO WAY")])

print(stringed_ans)
