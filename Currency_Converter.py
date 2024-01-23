import sys
from forex_python.converter import CurrencyRates

def get_exchange_rate(base_currency, target_currency):
    c = CurrencyRates()
    exchange_rate = c.get_rate(base_currency, target_currency)
    return exchange_rate

def convert_currency(amount, exchange_rate):
    converted_amount = amount * exchange_rate
    return converted_amount

currency_dict={'EUR','USD','GBP','CHF','YEN','AUD','CAD','CNY','SEK','NOK','ESC'}
def main():
    print("Καλωσορίσατε στον μετατροπέα νομισμάτων!")
    print("H forex-python υποστηρίζει πληθώρα νομισμάτων. Για τις ανάγκες της εργασίας ωστόσο, οι διαθέσιμες επιλογές είναι οι εξής:")
    print("Ευρώ (EUR)")
    print("Δολλάριο ΗΠΑ (USD)")
    print("Λίρα Μεγάλης Βρετανίας (GBP)")
    print("Ελβετικό Φράγκο (CHF)")
    print("Γιεν Iαπωνίας (YEN)")
    print("Δολλάριο Αυστραλίας (ΑUD)")
    print("Δολλάριο Καναδά (CAD)")
    print("Γουόν Κίνας (CNY)")
    print("Κορώνα Σουηδίας (SEK)")
    print("Κορώνα Νορβηγίας (ΝΟΚ)")
    print("Εξοδος/Exit (ESC)")

    base_currency = input("Παρακαλώ εισάγετε τη συντομογραφία της αρχικής νομισματικής μονάδας! (πχ: EUR): ").upper()
    
    while base_currency not in currency_dict:
        base_currency = input("Μη αποδεκτή νομισματική μονάδα! Παρακαλώ προσπαθηστε πάλι!").upper() 
    breakpoint
    
    if base_currency == 'ESC':
        print ("Σας ευχαριστούμε πολύ!")
        sys.exit()
    else: 
        target_currency = input("Παρακαλώ εισάγετε τη συντομογραφία της τελικής νομισματικής μονάδας! (πχ: USD): ").upper()

    while target_currency not in currency_dict:
        target_currency = input("Μη αποδεκτή νομισματική μονάδα! Παρακαλώ προσπαθηστε πάλι!").upper() 
    breakpoint
    
    if target_currency == 'ESC':
        print ("Σας ευχαριστούμε πολύ!")   
        sys.exit()
    
    while True:
        try:
            amount = float(input("Παρακαλώ εισάγετε το ποσό μετατροπής!: "))
            break
        except ValueError:
           print ("Μη αποδεκτή τιμή! Παρακαλώ εισάγετε ένα έγκυρο νούμερο!")

    exchange_rate = get_exchange_rate(base_currency, target_currency)
    
    converted_amount = convert_currency(amount, exchange_rate)
    
    print(f'Η σημερινή ισοτιμία για τα νομίσματα που επιλέξατε είναι: {exchange_rate} (στοιχεία από την Ευρωπαϊκή Κεντρική Τράπεζα).')
    print('Οι ισοτιμίες ανανεώνονται καθημερινά στις 16:00 ώρα Ελλάδας.')
    print(f'{amount} {base_currency} ισοδυναμούν με {converted_amount:.2f} {target_currency}.')
    print ('Σας ευχαριστούμε πολύ! Team 229.') 
    
    sys.exit()
       
if __name__ == "__main__":
    main() 
    