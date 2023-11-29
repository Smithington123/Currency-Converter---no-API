def calculation(x, y):
    return x * y
#values against GDP
GBP, USD, EUR, JPY, AUD, CHF = 1, 1.26, 1.15, 187.43, 1.91, 1.11

#values against USD
GBP_USD, USD_USD, EUR_USD, JPY_USD, AUD_USD, CHF_USD = 0.79, 1, 0.91, 148.56, 1.51, 0.88

#values against EUR
GBP_EUR, USD_EUR, EUR_EUR, JPY_EUR, AUD_EUR, CHF_EUR = 0.87, 1.10, 1, 162.82, 1.66, 0.97

#values against JPY
GBP_JPY, USD_JPY, EUR_JPY, JPY_JPY, AUD_JPY, CHF_JPY = 0.0053, 0.0067, 0.0061, 1, 0.010, 0.0059

#values against AUD
GBP_AUD, USD_AUD, EUR_AUD, JPY_AUD, AUD_AUD, CHF_AUD = 0.52, 0.66, 0.60, 98.29, 1, 0.58

#values against CHF
GBP_CHF, USD_CHF, EUR_CHF, JPY_CHF, AUD_CHF, CHF_CHF = 0.90, 1.13, 1.04, 168.52, 1.71, 1


print("This currency converter can calculate anyone of these into each other: GBP, US Dollar, Euro, Japanese Yen, Australian Dollar or Swiss Franc")
currency_choice = input("which currency would you like to exchange?: ")
currency_choice2 = input("which currency would you like to exchange into?: ")
amount = (float(input("How much of that currency would you like to convert?: ")))

#GBP to other currency
if currency_choice in ("GBP", "gbp", "Great British Pound", "Great British pound", "Great british pound", "great british pound", "British Pound", "British pound", "british pound", "Pound Sterling", "Pound sterling", "pound sterling", "pound", "£"):
    if currency_choice2 in ("USD", "usd", "united states dollar", "US dollar", "us dollar", "$"):
        print(amount, " GBP would be ", round(calculation(amount, USD), 2), "USD",)
        #Euro
    elif currency_choice2 in ("Euro", "euro", "eur", "EUR", "Eur"):
        print(amount, " GBP would be ", round(calculation(amount, EUR), 2), "Euro's",)
        #Japanese Yen
    elif currency_choice2 in ("JPY", "jpy", "Jpy", "Japanese Yen", "japanese yen", "Japanese yen", "JY", "jy", "Jy", "Yen", "yen"):
        print(amount, " GBP would be ", round(calculation(amount, JPY), 2), "JPY",)
        #Australian Dollar
    elif currency_choice2 in ("AUD", "aud", "Aud", "AuD", "Australian Dollar", "Australian dollar", "australian dollar", "Au dollar", "AU dollar", "AU Dollar", "au dollar"):
        print(amount, " GBP would be ", round(calculation(amount, AUD), 2), "AUD", )
        #Swiss Franc
    elif currency_choice2 in ("CHF", "Chf", "Swiss Franc", "Swiss franc", "swiss franc", "franc"):
        print(amount, " GBP would be ", round(calculation(amount, CHF), 2), "Swiss Francs", )
    elif currency_choice2 in ("GBP", "gbp", "Great British Pound", "Great British pound", "Great british pound", "great british pound", "British Pound", "British pound", "british pound", "Pound Sterling", "Pound sterling", "pound sterling", "pound", "£"):
        print(amount, " would be ", calculation(amount, USD), "USD", )

#USD to other currency
elif currency_choice in ("USD", "usd", "united states dollar", "US dollar", "us dollar", "$"):
    if currency_choice2 in ("USD", "usd", "united states dollar", "US dollar", "us dollar", "$"):
        print(amount, " GBP would be ", round(calculation(amount, USD_USD), 2), "USD",)
        #Euro
    elif currency_choice2 in ("Euro", "euro", "eur", "EUR", "Eur"):
        print(amount, " GBP would be ", round(calculation(amount, EUR_USD), 2), "Euro's",)
        #Japanese Yen
    elif currency_choice2 in ("JPY", "jpy", "Jpy", "Japanese Yen", "japanese yen", "Japanese yen", "JY", "jy", "Jy", "Yen", "yen"):
        print(amount, " GBP would be ", round(calculation(amount, JPY_USD), 2), "JPY",)
        #Australian Dollar
    elif currency_choice2 in ("AUD", "aud", "Aud", "AuD", "Australian Dollar", "Australian dollar", "australian dollar", "Au dollar", "AU dollar", "AU Dollar", "au dollar"):
        print(amount, " GBP would be ", round(calculation(amount, AUD_USD), 2), "AUD", )
        #Swiss Franc
    elif currency_choice2 in ("CHF", "Chf", "Swiss Franc", "Swiss franc", "swiss franc", "franc"):
        print(amount, " GBP would be ", round(calculation(amount, CHF_USD), 2), "Swiss Francs")
        #GBP
    elif currency_choice2 in ("GBP", "gbp", "Great British Pound", "Great British pound", "Great british pound", "great british pound", "British Pound", "British pound", "british pound", "Pound Sterling", "Pound sterling", "pound sterling", "pound", "£"):
        print(amount, " would be ", calculation(amount, GBP_USD), "GBP")

#Euro to other currency
elif currency_choice in ("Euro", "euro", "eur", "EUR", "Eur"):
    if currency_choice2 in ("USD", "usd", "united states dollar", "US dollar", "us dollar", "$", "Dollar", "dollar"):
        print(amount, " GBP would be ", round(calculation(amount, USD_EUR), 2), "USD",)
        #Euro
    elif currency_choice2 in ("Euro", "euro", "eur", "EUR", "Eur"):
        print(amount, " GBP would be ", round(calculation(amount, EUR_EUR), 2), "Euro's",)
        #Japanese Yen
    elif currency_choice2 in ("JPY", "jpy", "Jpy", "Japanese Yen", "japanese yen", "Japanese yen", "JY", "jy", "Jy", "Yen", "yen"):
        print(amount, " GBP would be ", round(calculation(amount, JPY_EUR), 2), "JPY",)
        #Australian Dollar
    elif currency_choice2 in ("AUD", "aud", "Aud", "AuD", "Australian Dollar", "Australian dollar", "australian dollar", "Au dollar", "AU dollar", "AU Dollar", "au dollar"):
        print(amount, " GBP would be ", round(calculation(amount, AUD_EUR), 2), "AUD", )
        #Swiss Franc
    elif currency_choice2 in ("CHF", "Chf", "Swiss Franc", "Swiss franc", "swiss franc", "franc"):
        print(amount, " GBP would be ", round(calculation(amount, CHF_EUR), 2), "Swiss Francs")
        #GBP
    elif currency_choice2 in ("GBP", "gbp", "Great British Pound", "Great British pound", "Great british pound", "great british pound", "British Pound", "British pound", "british pound", "Pound Sterling", "Pound sterling", "pound sterling", "pound", "£"):
        print(amount, " would be ", calculation(amount, GBP_EUR), "GBP")

#Yen to other currency
elif currency_choice in ("JPY", "jpy", "Jpy", "Japanese Yen", "japanese yen", "Japanese yen", "JY", "jy", "Jy", "Yen", "yen"):
    if currency_choice2 in ("USD", "usd", "united states dollar", "US dollar", "us dollar", "$", "Dollar", "dollar"):
        print(amount, " GBP would be ", round(calculation(amount, USD_JPY), 2), "USD",)
        #Euro
    elif currency_choice2 in ("Euro", "euro", "eur", "EUR", "Eur"):
        print(amount, " GBP would be ", round(calculation(amount, EUR_JPY), 2), "Euro's",)
        #Japanese Yen
    elif currency_choice2 in ("JPY", "jpy", "Jpy", "Japanese Yen", "japanese yen", "Japanese yen", "JY", "jy", "Jy", "Yen", "yen"):
        print(amount, " GBP would be ", round(calculation(amount, JPY_JPY), 2), "JPY",)
        #Australian Dollar
    elif currency_choice2 in ("AUD", "aud", "Aud", "AuD", "Australian Dollar", "Australian dollar", "australian dollar", "Au dollar", "AU dollar", "AU Dollar", "au dollar"):
        print(amount, " GBP would be ", round(calculation(amount, AUD_JPY), 2), "AUD", )
        #Swiss Franc
    elif currency_choice2 in ("CHF", "Chf", "Swiss Franc", "Swiss franc", "swiss franc", "franc"):
        print(amount, " GBP would be ", round(calculation(amount, CHF_JPY), 2), "Swiss Francs")
        #GBP
    elif currency_choice2 in ("GBP", "gbp", "Great British Pound", "Great British pound", "Great british pound", "great british pound", "British Pound", "British pound", "british pound", "Pound Sterling", "Pound sterling", "pound sterling", "pound", "£"):
        print(amount, " would be ", calculation(amount, GBP_JPY), "GBP")

#AUD to other currency
elif currency_choice in ("AUD", "aud", "Aud", "AuD", "Australian Dollar", "Australian dollar", "australian dollar", "Au dollar", "AU dollar", "AU Dollar", "au dollar"):
    if currency_choice2 in ("USD", "usd", "united states dollar", "US dollar", "us dollar", "$", "Dollar", "dollar"):
        print(amount, " GBP would be ", round(calculation(amount, USD_AUD), 2), "USD",)
        #Euro
    elif currency_choice2 in ("Euro", "euro", "eur", "EUR", "Eur"):
        print(amount, " GBP would be ", round(calculation(amount, EUR_AUD), 2), "Euro's",)
        #Japanese Yen
    elif currency_choice2 in ("JPY", "jpy", "Jpy", "Japanese Yen", "japanese yen", "Japanese yen", "JY", "jy", "Jy", "Yen", "yen"):
        print(amount, " GBP would be ", round(calculation(amount, JPY_AUD), 2), "JPY",)
        #Australian Dollar
    elif currency_choice2 in ("AUD", "aud", "Aud", "AuD", "Australian Dollar", "Australian dollar", "australian dollar", "Au dollar", "AU dollar", "AU Dollar", "au dollar"):
        print(amount, " GBP would be ", round(calculation(amount, AUD_AUD), 2), "AUD", )
        #Swiss Franc
    elif currency_choice2 in ("CHF", "Chf", "Swiss Franc", "Swiss franc", "swiss franc", "franc"):
        print(amount, " GBP would be ", round(calculation(amount, CHF_AUD), 2), "Swiss Francs")
        #GBP
    elif currency_choice2 in ("GBP", "gbp", "Great British Pound", "Great British pound", "Great british pound", "great british pound", "British Pound", "British pound", "british pound", "Pound Sterling", "Pound sterling", "pound sterling", "pound", "£"):
        print(amount, " would be ", calculation(amount, GBP_AUD), "GBP")

#CHF to other currency
elif currency_choice in ("CHF", "Chf", "Swiss Franc", "Swiss franc", "swiss franc", "franc"):
    if currency_choice2 in ("USD", "usd", "united states dollar", "US dollar", "us dollar", "$", "Dollar", "dollar"):
        print(amount, " GBP would be ", round(calculation(amount, USD_CHF), 2), "USD",)
        #Euro
    elif currency_choice2 in ("Euro", "euro", "eur", "EUR", "Eur"):
        print(amount, " GBP would be ", round(calculation(amount, EUR_CHF), 2), "Euro's",)
        #Japanese Yen
    elif currency_choice2 in ("JPY", "jpy", "Jpy", "Japanese Yen", "japanese yen", "Japanese yen", "JY", "jy", "Jy", "Yen", "yen"):
        print(amount, " GBP would be ", round(calculation(amount, JPY_CHF), 2), "JPY",)
        #Australian Dollar
    elif currency_choice2 in ("AUD", "aud", "Aud", "AuD", "Australian Dollar", "Australian dollar", "australian dollar", "Au dollar", "AU dollar", "AU Dollar", "au dollar"):
        print(amount, " GBP would be ", round(calculation(amount, AUD_CHF), 2), "AUD", )
        #Swiss Franc
    elif currency_choice2 in ("CHF", "Chf", "Swiss Franc", "Swiss franc", "swiss franc", "franc"):
        print(amount, " GBP would be ", round(calculation(amount, CHF_CHF), 2), "Swiss Francs")
        #GBP
    elif currency_choice2 in ("GBP", "gbp", "Great British Pound", "Great British pound", "Great british pound", "great british pound", "British Pound", "British pound", "british pound", "Pound Sterling", "Pound sterling", "pound sterling", "pound", "£"):
        print(amount, " would be ", calculation(amount, GBP_CHF), "GBP")
