#Calculadora simples de comissão
leave = False
while leave == False:

    valor_total = input("Valor total do carregamento: (Use ponto para valores fracionados)\n  ")
    porcentagem = input("Porcentagem de comissão: (Use ponto para valores fracionados) \n  ")
    dolar = input("Moeda em dólar? (s/n)\n  ")

    valor_bruto = float(valor_total) / 100 * float(porcentagem)



    import requests
    from bs4 import BeautifulSoup

    url = "https://www.google.com/search?q=dolar&oq=dolar&aqs=chrome.0.69i59j69i57j69i59j0i271j69i60l2j69i61l2.727j0j7&sourceid=chrome&ie=UTF-8"
    url_r = requests.get(url)

    #Para converter a list resultante de soup.findAll para um string
    def listToString(s):
        str1 = ""

        for ele in s:
            str1 += ele

        return str1


    #Retirando os dados que eu quero do codigo html
    soup = BeautifulSoup(url_r.content, 'html5lib')
    table = soup.findAll('div', attrs = {'class' : 'BNeawe iBp4i AP7Wnd'})


    #Convertendo para uma string especifica usando a função de converter lista para string
    #E usando replace para deixar a string preparada para ser convertida para float
    #Para que possa ser usada no calculo
    table_str = listToString(table[1])
    table_str = table_str.replace("," , ".")
    table_str = table_str.replace(" Real brasileiro" , "")

    valor_dolar = float(table_str)







    if dolar == 's':
        dolar = True
    else:
        dolar = False

    if dolar == True:
        valor_liquido = float(valor_bruto) * float(valor_dolar)
    else:
        valor_liquido = valor_bruto


    print("O valor em reais da comissão é de " + str(valor_liquido) + " reais.\n \n \n")
    leave = input("Deseja fazer outro calculo? (s/n)\n  ")
    if leave == 's':
        leave = False
    else:
        leave = True