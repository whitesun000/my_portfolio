from pyscript import document

# 履歴を保存するリスト
history_list = []

def update_display(result_text, operation_text):
    # 結果を表示
    document.querySelector("#result_area").innerText = result_text

    # 履歴リストの先頭に追加
    history_list.insert(0, operation_text)

    # 履歴エリアを更新（最大5件表示）
    history_html = ""
    for item in history_list[:5]:
        history_html += f"<div>{item}</div>"
    document.querySelector("#history_area").innerHTML = history_html

# 足し算
def calculate(event):
    v1, v2 = document.querySelector("#num1").value, document.querySelector("#num2").value
    document.querySelector("#operator").innerText = " + "
    if v1 and v2:
        res = int(v1) + int (v2)
        update_display(f"答え：{res}", f"{v1} + {v2} = {res}")

# 引き算
def subtraction(event):
    v1, v2 = document.querySelector("#num1").value, document.querySelector("#num2").value
    document.querySelector("#operator").innerText = " - "
    if v1 and v2:
        res = int(v1) - int (v2)
        update_display(f"答え：{res}", f"{v1} - {v2} = {res}")

# 掛け算
def multiplication(event):
    v1, v2 = document.querySelector("#num1").value, document.querySelector("#num2").value
    document.querySelector("#operator").innerText = " x "
    if v1 and v2:
        res = int(v1) * int (v2)
        update_display(f"答え：{res}", f"{v1} x {v2} = {res}")
# 割り算
def division(event):
   v1, v2 = document.querySelector("#num1").value, document.querySelector("#num2").value
   document.querySelector("#operator").innerText = " ÷ "
   if v1 and v2:
       if v2 == "0":
            document.querySelector("#result_area").innerText = "0では割れません！"    
       else:
            res = int(v1) / int (v2)
            update_display(f"答え：{res}", f"{v1} ÷ {v2} = {res}")

# クリアボタンの処理
def clear_all(event):
    document.querySelector("#num1").value = ""
    document.querySelector("#num2").value = ""
    document.querySelector("#result_area").innerText = "クリアしました"
    document.querySelector("#operator").innerText = " + "