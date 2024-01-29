#Σε terminal και πριν το τρέξουμε, γράφουμε: "pip install forex-python" για να γίνει εγκατάσταση της βιβλιοθήκης.
#προαιρετικά και pip install datetime σε terminal 

import sys
from datetime import datetime
from forex_python.converter import CurrencyRates

#ορίζουμε σημερινή ημερομηνία, η οποία ανανεώνεται καθημερινά και τη μεταβλήτη c για τις συναλλαγματικές ισοτιμίες.
today=datetime.now()
c = CurrencyRates()

#ορίζουμε dictionary για να περιορίσουμε τα διαθέσιμα νομίσματα της forex-python σε μόλις 10 επιλογές.
currencies = ['EUR','USD','GBP','CHF','JPY','AUD','CAD','CNY','SEK','NOK']

#καθορίζουμε 3 def's
#1o def: καθορισμός μεθοδολογίας ΑΡΙ request στην forex-python για να λάβει τις σημερινές ισοτιμίες
def get_exchange_rate(base_currency, target_currency):
    exchange_rate = c.get_rate(base_currency, target_currency)
    return exchange_rate

#2ο def: Καθορισμός μαθηματικής πράξη μετατροπής νομίσματος.
def convert_currency(amount, exchange_rate):
    converted_amount = amount * exchange_rate
    return converted_amount

#menu με το οποίο ο χρήστης ενημερώνεται για τις διαθέσιμες σημερινές ισοτιμίες.
print("Καλωσορίσατε στον μετατροπέα νομισμάτων!")
print (f"Για σήμερα,{today.strftime("%d-%m-%Y")}, οι ισοτιμίες της Ευρωπαϊκής Κεντρικής Τράπεζας έχουν ως εξής:")
for currency in currencies:
    rate = float(c.get_rate(currency, "EUR"))
    print(f"1 {currency} ισοδυναμεί με {rate:.2f} EUR")

#3ο def: Ο χρήστης ενημερώνεται για τις επιλογές που έχει.
def main():
    print("H forex-python υποστηρίζει πληθώρα νομισμάτων. Για τις ανάγκες της εργασίας ωστόσο, οι διαθέσιμες επιλογές είναι οι εξής:")
    print("Ευρώ (EUR)")
    print("Δολλάριο ΗΠΑ (USD)")
    print("Λίρα Μεγάλης Βρετανίας (GBP)")
    print("Ελβετικό Φράγκο (CHF)")
    print("Γιεν Iαπωνίας (JPY)")
    print("Δολλάριο Αυστραλίας (ΑUD)")
    print("Δολλάριο Καναδά (CAD)")
    print("Γουόν Κίνας (CNY)")
    print("Κορώνα Σουηδίας (SEK)")
    print("Κορώνα Νορβηγίας (ΝΟΚ)")
    print("Εξοδος/Exit (ESC)")
    
#input αρχικής νομισματικής μονάδας
    base_currency = input("Παρακαλώ εισάγετε τη συντομογραφία της αρχικής νομισματικής μονάδας! (πχ: EUR): ").upper()
#αν επιλογή = ESC, τερματίζει ο αλγόριθμος   
    if base_currency == "ESC":
        print ("Σας ευχαριστούμε πολύ!")
        sys.exit()
#αν η επιλογή του δεν είναι στις διαθέσιμες, απαιτείται εκ νέου input
    else:
        while base_currency not in currencies:
            base_currency = input("Μη αποδεκτή νομισματική μονάδα! Παρακαλώ προσπαθηστε πάλι!").upper() 
        breakpoint
#input τελικής νομισματικής μονάδας
    target_currency = input("Παρακαλώ εισάγετε τη συντομογραφία της τελικής νομισματικής μονάδας! (πχ: USD): ").upper()
#αν επιλογή = ESC, τερματίζει ο αλγόριθμος 
    if target_currency == 'ESC':
        print ("Σας ευχαριστούμε πολύ!")   
        sys.exit()
#αν η επιλογή του δεν είναι στις διαθέσιμες, απαιτείται εκ νέου input
    else:   
        while target_currency not in currencies:
            target_currency = input("Μη αποδεκτή νομισματική μονάδα! Παρακαλώ προσπαθηστε πάλι!").upper() 
        breakpoint
        
#εάν έχει εισάγει επιτυχώς το νόμισμα βάσης και στόχος (Τrue), ζητείται η εισαγωγή δεκαδικού ποσού
    while True:
        try:
            amount = float(input("Παρακαλώ εισάγετε το ποσό μετατροπής!: "))
            break
#εαν δεν βάλει δεκαδικό ποσό, απαιτείται εκ νέου input
        except ValueError:
           print ("Μη αποδεκτή τιμή! Παρακαλώ εισάγετε ένα έγκυρο νούμερο!")
#κλήση 1ου def
    exchange_rate = get_exchange_rate(base_currency, target_currency)
#κλήση 2ου def
    converted_amount = convert_currency(amount, exchange_rate)
#Εκτύπωση αποτελεσμάτων και ενημέρωση σχετικά με τις ισοτιμίες
    print(f'Η σημερινή ισοτιμία για τα νομίσματα που επιλέξατε είναι: {exchange_rate:.2f} (στοιχεία από την Ευρωπαϊκή Κεντρική Τράπεζα).')
    print('Οι ισοτιμίες ανανεώνονται καθημερινά στις 16:00 ώρα Ελλάδας.')
    print(f'{amount} {base_currency} ισοδυναμούν με {converted_amount:.2f} {target_currency}.')
    print ('Σας ευχαριστούμε πολύ! Team 229.') 
#τερματισμός
    sys.exit()
       
if __name__ == "__main__":
    main() 