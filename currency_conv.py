print('ΜΕΤΑΤΡΟΠΕΑΣ ΝΟΜΙΣΜΑΤΩΝ')
print('ΠΑΤΗΣΤΕ:\n1 = ΕΝΑΡΞΗ ΜΕΤΑΤΡΟΠΗΣ\n2 = EXIT')
select=int(input())

while select<1 or select>2:
        print('ΔΩΣΑΤΕ ΛΑΘΟΣ ΕΠΙΛΟΓΗ')
        select=int(input())
else:

        if select==2:
                print('ΕΥΧΑΡΙΣΤΟΥΜΕ!')
                exit()
      
        else:
                amount=float(input('ΠΟΣΟ ΜΕΤΑΤΡΟΠΗΣ : '))
                print ('Τι νόμισμα θέλετε να μετατρέψετε;')
                print ('1=EUR\n2=USD\n3=JY\n4=RR\n5=1CD')
                EUR=1 #1
                USD=1.1 #2
                JY=157.24 #3
                RR=101.18 #4
                CD=1.46 #5
                
                nomisma=int(input('ΝΟΜΙΣΜΑ: '))


                while nomisma<1 or nomisma>5:
                        print('Δώσατε λάθος επιλογή')
                        nomisma=int(input('ΝΟΜΙΣΜΑ: '))
                else:
                        if nomisma==1:
                                posomet=amount
                        elif nomisma==2:
                                posomet=amount/USD
                        elif nomisma==3:
                                posomet=amount/JY
                        elif nomisma==4:
                                posomet=amount/RR
                        elif nomisma==5:
                                posomet=amount/CD


                nomismamet=int(input("ΜΕΤΑΤΡΟΠΗ ΣΕ: "))
                while nomismamet<1 or nomismamet>5:
                        print('Δώσατε λάθος επιλογή')
                        nomismamet=int(input("ΜΕΤΑΤΡΟΠΗ ΣΕ: "))
                else:
                        if nomismamet==1:
                                teliko=posomet
                        elif nomismamet==2:
                                teliko=posomet*USD
                        elif nomismamet==3:
                                teliko=posomet*JY
                        elif nomismamet==4:
                                teliko=posomet*RR
                        elif nomismamet==5:
                                teliko=posomet*CD
                print('το τελικο ποσο ειναι: ', teliko)                

