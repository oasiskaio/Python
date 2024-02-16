# Inserir cada célula de cada linha em um campo do sistema
import openpyxl
import pyautogui

workbook = openpyxl.load_workbook('vendas_de_produtos.xlsx') #usa a biblioteca para ler a planilha
vendas_sheet = workbook['vendas'] # vai ler a pagina vendas

for linha in vendas_sheet.iter_rows(min_row=2): #vai ler a partir da segunda linha
    # nome
    pyautogui.click(1504,217,duration=1.5)
    pyautogui.write(linha[0].value)
    # produto
    pyautogui.click(1518,241,duration=1.5)
    pyautogui.write(linha[1].value)
    # quantidade
    pyautogui.click(1515,266,duration=1.5)
    pyautogui.write(str(linha[2].value))
    # categoria
    pyautogui.click(1590,293,duration=1.5)
    pyautogui.write(linha[3].value)
    pyautogui.click(1444,321,duration=1.5)
    pyautogui.click(939,578,duration=1.5)
    
    