currency_dict = {'GBP_GBP': 1, 'GBP_USD': 1.26, 'GBP_EUR': 1.15, 'GBP_JPY': 187.43, 'GBP_AUD': 1.91, 'GBP_CHF': 1.11,
                 'USD_GBP': 0.79, 'USD_USD': 1, 'USD_EUR': 0.91, 'USD_JPY': 148.56, 'USD_AUD': 1.51, 'USD_CHF': 0.88,
                 'EUR_GBP': 0.87, 'EUR_USD': 1.10, 'EUR_EUR': 1, 'EUR_JPY': 162.82, 'EUR_AUD': 1.66, 'EUR_CHF': 0.97,
                 'JPY_GBP': 0.0053, 'JPY_USD': 0.0067, 'JPY_EUR': 0.0061, 'JPY_JPY': 1, 'JPY_AUD': 0.010, 'JPY_CHF': 0.0059,
                 'AUD_GBP': 0.52, 'AUD_USD': 0.66, 'AUD_EUR': 0.60, 'AUD_JPY': 98.29, 'AUD_AUD': 1, 'AUD_CHF': 0.58,
                 'CHF_GBP': 0.90, 'CHF_USD': 1.13, 'CHF_EUR': 1.04, 'CHF_JPY': 168.52, 'CHF_AUD': 1.71, 'CHF_CHF': 1,
}
def search_dict():
    for currency, exchange_rate in currency_dict.items():
        if currency == search_currency:
            print("the current exchange rate is:")
            print(exchange_rate)
            convert_amount = float(input("How much currency would you like to convert?: "))
            print("You would get", exchange_rate * convert_amount, "of this currency")

while True:
    print("This currency converter can calculate using GBP, USD, EUR, JPY, AUD and CHF")
    search_currency = input("Please type the currency's you want to convert in the format of GBP_USD: ").upper()
    search_dict()
    Another_calc = input("would you like to do another?: ").upper()
    if Another_calc == "NO":
        break