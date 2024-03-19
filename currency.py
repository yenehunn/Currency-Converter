from forex_python.converter import CurrencyRates
from forex_python.converter import CurrencyCodes
cur = CurrencyRates()
def currency():
    while True:

        curr_code =["EUR","IDR","BGN","ILS","GBP","DKK","CAD","ETB","JPY","HUF","RON","MYR","SEK","SGD","HKD","AUD","CHF","KRW","CNY","TRY","HRK","NZD","THB","USD","SAR","NOK","RUB" ,"INR","MXN","CZK","BRL","PLN","PHP","ZAR"]
        option = str(curr_code)
        amount = int (input("enter currency amount "))
        source_curr = input("enter the source currency ")
        target_curr = input("enter the target currency ")
        if source_curr and target_curr in curr_code:

              if source_curr =='USD' and target_curr=='ETB':
                  exchange_amount = amount* 56.56
                  print(f"Exchange rate from {amount} {source_curr} to {target_curr} is {exchange_amount} {target_curr}")
              
              elif source_curr =='GBP' and target_curr=='ETB':
                  exchange_amount = amount* 72.08
                  print(f"Exchange rate from {amount} {source_curr} to {target_curr} is {exchange_amount} {target_curr}")
              elif source_curr == 'CNY' and target_curr == 'ETB':
                  exchange_amount = amount * 7.86
                  print(f"Exchange rate from {amount} {source_curr} to {target_curr} is {exchange_amount} {target_curr}")
              elif source_curr == 'CAD' and target_curr == 'ETB':
                  exchange_amount = amount *41.77
                  print(F"Exchange rate from {amount} {source_curr} to {target_curr} is {exchange_amount} {target_curr}")
              elif source_curr == 'EUR' and target_curr == 'ETB':
                  exchange_amount = amount *61.62
                  print(F"Exchange rate from {amount} {source_curr} to {target_curr} is {exchange_amount} {target_curr}")          
              elif source_curr == 'AUD' and target_curr == 'ETB':
                  exchange_amount = amount *37.12
                  print(F"Exchange rate from {amount} {source_curr} to {target_curr} is {exchange_amount} {target_curr}") 
              elif source_curr == 'JPY' and target_curr == 'ETB':
                  exchange_amount = amount *0.37
                  print(F"Exchange rate from {amount} {source_curr} to {target_curr} is {exchange_amount} {target_curr}")     
              elif source_curr == 'INR' and target_curr == 'ETB':
                  exchange_amount = amount *0.68
                  print(F"Exchange rate from {amount} {source_curr} to {target_curr} is {exchange_amount} {target_curr}")   
              elif source_curr == 'NZD' and target_curr == 'ETB':
                  exchange_amount = amount *34.42
                  print(F"Exchange rate from {amount} {source_curr} to {target_curr} is {exchange_amount} {target_curr}")  
              elif source_curr == 'CHF' and target_curr == 'ETB':
                  exchange_amount = amount *64.06
                  print(F"Exchange rate from {amount} {source_curr} to {target_curr} is {exchange_amount} {target_curr}")
              elif source_curr == 'ZAR' and target_curr == 'ETB':
                  exchange_amount = amount *3.01
                  print(F"Exchange rate from {amount} {source_curr} to {target_curr} is {exchange_amount} {target_curr}") 
              elif source_curr == 'RUB' and target_curr == 'ETB':
                  exchange_amount = amount *0.61
                  print(F"Exchange rate from {amount} {source_curr} to {target_curr} is {exchange_amount} {target_curr}") 
              elif source_curr == 'BGN' and target_curr == 'ETB':
                  exchange_amount = amount *31.50
                  print(F"Exchange rate from {amount} {source_curr} to {target_curr} is {exchange_amount} {target_curr}")
              elif source_curr == 'SGD' and target_curr == 'ETB':
                  exchange_amount = amount *42.29
                  print(F"Exchange rate from {amount} {source_curr} to {target_curr} is {exchange_amount} {target_curr}")
              elif source_curr == 'HKD' and target_curr == 'ETB':
                  exchange_amount = amount *7.23
                  print(F"Exchange rate from {amount} {source_curr} to {target_curr} is {exchange_amount} {target_curr}")
              elif source_curr == 'SEK' and target_curr == 'ETB':
                  exchange_amount = amount *5.45
                  print(F"Exchange rate from {amount} {source_curr} to {target_curr} is {exchange_amount} {target_curr}") 
              elif source_curr == 'THB' and target_curr == 'ETB':
                  exchange_amount = amount *1.57
                  print(F"Exchange rate from {amount} {source_curr} to {target_curr} is {exchange_amount} {target_curr}") 
              elif source_curr == 'HUF' and target_curr == 'ETB':
                  exchange_amount = amount *0.15
                  print(F"Exchange rate from {amount} {source_curr} to {target_curr} is {exchange_amount} {target_curr}")
              elif source_curr == 'NOK' and target_curr == 'ETB':
                  exchange_amount = amount *5.33
                  print(F"Exchange rate from {amount} {source_curr} to {target_curr} is {exchange_amount} {target_curr}") 
              elif source_curr == 'MXN' and target_curr == 'ETB':
                  exchange_amount = amount *3.38
                  print(F"Exchange rate from {amount} {source_curr} to {target_curr} is {exchange_amount} {target_curr}")
              elif source_curr == 'MYR' and target_curr == 'ETB':
                  exchange_amount = amount *12.00
                  print(F"Exchange rate from {amount} {source_curr} to {target_curr} is {exchange_amount} {target_curr}")
              elif source_curr == 'BRL' and target_curr == 'ETB':
                  exchange_amount = amount *11.33
                  print(F"Exchange rate from {amount} {source_curr} to {target_curr} is {exchange_amount} {target_curr}") 
              elif source_curr == 'SAR' and target_curr == 'ETB':
                  exchange_amount = amount *15.09
                  print(F"Exchange rate from {amount} {source_curr} to {target_curr} is {exchange_amount} {target_curr}") 
              elif True:
              
                exchange_rate =cur.get_rate(source_curr,target_curr)
                print(f"Exchange rate from {amount} {source_curr} to {target_curr}: {exchange_rate} {target_curr}")
        else:
            print("INVALID ENTRAY")      
currency()

