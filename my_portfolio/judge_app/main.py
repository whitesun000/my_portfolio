from pyscript import document

def compare(event):
    pA = document.querySelector("#priceA").value
    wA = document.querySelector("#weightA").value
    pB = document.querySelector("#priceB").value
    wB = document.querySelector("#weightB").value

    if pA and wA and pB and wB:
        unitA = float(pA) / float(wA)
        unitB = float(pB) / float(wB)

        if unitA < unitB:
            diff = unitB - unitA
            res = f"★商品Aの方がお得！<br><small>1単位あたり {diff:.2f}円 安いです</small>"
        elif unitB < unitA:
            diff = unitA - unitB
            res = f"★商品Bの方がお得！<br><small>1単位当たり {diff: .2f}円 安いです</small>"
        else:
            res = "どちらも同じ価格です！"
        
        document.querySelector("#result_area").innerHTML = res
    else:
        document.querySelector("#result_area").innerText = "すべての欄を入力してね"