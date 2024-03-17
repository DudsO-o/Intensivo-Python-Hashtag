import pyautogui
import pandas as pd
import time
import tkinter as tk

tabela = pd.read_csv(r"C:\Users\duds\Documents\Coding\Hashtag Python\C01\produtos.csv")
link = ("https://dlp.hashtagtreinamentos.com/python/intensivao/login")

pyautogui.PAUSE = 0.5

# Abre o navegador
pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")
time.sleep(6)

# Abre o site
pyautogui.hotkey("ctrl", "t")
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(1)

# Faz login 
pyautogui.click(x=1813, y=449)
pyautogui.write("email@gmail.com")
pyautogui.press("tab")
pyautogui.write("senha123")
pyautogui.press("tab")
pyautogui.press("enter")

# Create a simple tkinter window
counter_window = tk.Tk()
counter_window.title("Loop Count")
counter_window.geometry("500x50")
counter_label = tk.Label(counter_window, text="Loop count: 0", font=("Montserrat", 20), anchor="center")
counter_label.pack()

count = 0

# Cadastra os produtos
for linha in tabela.index:
    # Update the loop count in the tkinter window
    count += 1
    counter_label.config(text=f"Loop count: {count}")
    counter_window.update()

    pyautogui.click(x=1856, y=329)
    pyautogui.write(tabela.loc[linha, "codigo"])
    pyautogui.press("tab")
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    if not pd.isna(tabela.loc[linha, "obs"]):
        pyautogui.write(tabela.loc[linha, "obs"])
    pyautogui.press("tab")
    pyautogui.press("enter")

counter_label.config(text=f"Task Completed Successfully!", font=("Montserrat", 20), anchor="center")
counter_window.update()
counter_window.mainloop()