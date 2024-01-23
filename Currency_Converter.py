from forex_python.converter import CurrencyRates

def get_exchange_rate(base_currency, target_currency):
    c = CurrencyRates()
    exchange_rate = c.get_rate(base_currency, target_currency)
    return exchange_rate

def convert_currency(amount, exchange_rate):
    converted_amount = amount * exchange_rate
    return converted_amount

def main():
    print("Καλωσορίσατε στον μετατροπέα νομισμάτων!")
    print("H forex-python υποστηρίζει πληθώρα νομισμάτων. Για τις ανάγκες της εργασίας ωστόσο, οι διαθέσιμες επιλογές είναι οι εξής:")
    print("Ευρώ (EUR)")
    print("Δολλάριο ΗΠΑ (USD)")
    print("Λίρα Μεγάλης Βρετανίας (GBP)")