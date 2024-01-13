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
                print ('1=EUR\n2=USD\n3=JY\n4=RR\n5=CD')
                EUR=1 #1
                USD=1.1 #2
                JY=157.24 #3
                RR=101.18 #4
                CD=1.46 #5
                
                A=["1","2","3","4","5"]
                nomisma=input('ΝΟΜΙΣΜΑ: ')


                while nomisma not in A:
                        print('Δώσατε λάθος επιλογή')
                        nomisma=input('ΝΟΜΙΣΜΑ: ')
                else:
                        while True:
                                try:
                                        amount=float(input('ΠΟΣΟ ΜΕΤΑΤΡΟΠΗΣ : '))
                                except ValueError:
                                        print('Δώσατε λάθος επιλογή')
                                else:
                                        break
                        if nomisma=="1":
                                posomet=amount
                        elif nomisma=="2":
                                posomet=amount/USD
                        elif nomisma=="3":
                                posomet=amount/JY
                        elif nomisma=="4":
                                posomet=amount/RR
                        elif nomisma=="5":
                                posomet=amount/CD

                nomismamet=input("ΜΕΤΑΤΡΟΠΗ ΣΕ: ")
                while nomismamet not in A:
                        print('Δώσατε λάθος επιλογή')
                        nomismamet=input("ΜΕΤΑΤΡΟΠΗ ΣΕ: ")
                else:
                        if nomismamet=="1":
                                teliko=posomet
                                t="EUR"
                        elif nomismamet=="2":
                                teliko=posomet*USD
                                t="USD"
                        elif nomismamet=="3":
                                teliko=posomet*JY
                                t="JY"
                        elif nomismamet=="4":
                                teliko=posomet*RR
                                t="RR"
                        elif nomismamet=="5":
                                teliko=posomet*CD
                                t="CD"
                print('το τελικο ποσο ειναι: ', teliko,t)                

