import pandas as pd
df=pd.read_csv(r'eurofxref.csv')
currency=list(df[' USD'])
value=list(df['1.0946'])
currency.append('USD')
currency.append('EUR')
value.append(1.0946)
value.append(1)



print('ΜΕΤΑΤΡΟΠΕΑΣ ΝΟΜΙΣΜΑΤΩΝ')
print('ΠΑΤΗΣΤΕ:\n1 = ΕΝΑΡΞΗ ΜΕΤΑΤΡΟΠΗΣ\n2 = EXIT')
select=input()

while select!="1" and select!="2":
        print('ΔΩΣΑΤΕ ΛΑΘΟΣ ΕΠΙΛΟΓΗ')
        print('ΠΑΤΗΣΤΕ:\n1 = ΕΝΑΡΞΗ ΜΕΤΑΤΡΟΠΗΣ\n2 = ΕΞΟΔΟΣ')
        select=input()
else:

        if select=="2":
                print('ΕΥΧΑΡΙΣΤΟΥΜΕ!')
                exit()
      
        else:
                print ('Τι νόμισμα θέλετε να μετατρέψετε;')
                print ('1 =Japanese yen(JPY)\n2 = Bulgaria lev (BGN)\n3 = Czech koruna (CZK)\n4 = Danish krone(DKK)\n5 = British pound (GBP)')
                print('6 = Hungarian forint(HUF)\n7 = Polish złoty PLN\n8 = Romanian leu(RON)\n9 = Swedish krona (SEK)\n10 = Swiss franc (CHF)\n11 = Icelandic króna (ISK)')
                print('12 =Norwegian krone(NOK)\n13 = Turkish lira (TRY)\n14 = Australian dollar (AUD)\n15 = Brazilian real (BRL)\n16 = Canadian dollar(CAD)\n17 = Chinese yuan (CNY)')
                print('18 = Hong Kong dollar(HKD)\n19 = Indonesian rupiah (IDR)\n20 = Israeli new shekel (ILS)\n21 = Indian rupee(INR)\n22 = South Korean won(KRW)\n23 = Mexican peso (MXN)')
                print('24 = Malaysian ringgit(MYR)\n25 = New Zealand dollar(NZD)\n26 = Philippine peso(PHP)\n27 = Singapore dollar(SGD)\n28 = Thai baht (THB)\n29 = South African rand(ZAR)\n30 = United States dollar (USD)')
                print('31 = Euro (EUR)')
                
                A=range(1,32)
               
                while True: 
                        try:
                                nomisma=int(input('ΝΟΜΙΣΜΑ: '))
                                while nomisma not in A:
                                        print('Δώσατε λάθος επιλογή')
                                        nomisma=int(input('ΝΟΜΙΣΜΑ: '))
                                else:
                                                   
                                        while True:
                                                try:
                                                        amount=float(input('ΠΟΣΟ ΜΕΤΑΤΡΟΠΗΣ : '))
                                                except ValueError:
                                                        print('Δώσατε λάθος επιλογή')
                                                else:
                                                        break
                                        posomet = amount/value[nomisma-1]
                        except ValueError:
                                 print('Δώσατε λάθος επιλογή')
                        else:
                                break
                while True:
                        try:
                                nomismamet=int(input("ΜΕΤΑΤΡΟΠΗ ΣΕ: "))
                                while nomismamet not in A:
                                        print('Δώσατε λάθος επιλογή')
                                        nomismamet=int(input("ΜΕΤΑΤΡΟΠΗ ΣΕ: "))
                                else:
                                        teliko=posomet*value[nomismamet-1]
                        except ValueError:
                                 print('Δώσατε λάθος επιλογή')
                        else:
                                break
                       
                print('το τελικο ποσο ειναι: ', teliko,currency[nomismamet-1])                

