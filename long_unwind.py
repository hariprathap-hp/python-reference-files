import requests
import json
import pandas as pd

#To refer : https://www.ritchieng.com/pandas-selecting-multiple-rows-and-columns/
#Multiple filter criteris in Pandas : https://www.ritchieng.com/pandas-multi-criteria-filtering/

new_url = 'https://www.nseindia.com/api/option-chain-indices?symbol=BANKNIFTY'

headers = {'User-Agent': 'Mozilla/5.0'}
page = requests.get(new_url,headers=headers)
dajs = json.loads(page.text)


def fetch_oi(expiry_dt):

    ce_values = [data['CE'] for data in dajs['records']['data'] if "CE" in data and data['expiryDate'] == expiry_dt]
    pe_values = [data['PE'] for data in dajs['records']['data'] if "PE" in data and data['expiryDate'] == expiry_dt]
    
    values = [data['PE'] for data in dajs['records']['data'] if "PE" in data and data['expiryDate'] == expiry_dt]
    val_CE = [data['CE'] for data in dajs['records']['data'] if "CE" in data and data['expiryDate'] == expiry_dt]
    values.extend(val_CE)

    ce_dt = pd.DataFrame(ce_values).sort_values(['openInterest'],ascending=False)
    pe_dt = pd.DataFrame(pe_values).sort_values(['openInterest'],ascending=False)

    value_dt = pd.DataFrame(values)


    new_ce_dt = ce_dt[((ce_dt.pchangeinOpenInterest >= -1000) & (ce_dt.pchangeinOpenInterest <= 1000)) & ((ce_dt.pChange >= -1000) & (ce_dt.pChange <= 1000))]
    new_pe_dt = pe_dt[((pe_dt.pchangeinOpenInterest >= -1000) & (pe_dt.pchangeinOpenInterest <= 1000)) & ((pe_dt.pChange >= -1000) & (pe_dt.pChange <= 1000))]
    #long_build = value_dt[((value_dt.pchangeinOpenInterest >= -250) & (value_dt.pchangeinOpenInterest <= 250)) & ((value_dt.pChange >= -250) & (value_dt.pChange <= 250))]
    long_unwind = value_dt[((value_dt.pchangeinOpenInterest <= 0)) & ((value_dt.pChange <= 0))]

    new_CE_DT = pd.DataFrame(new_ce_dt).sort_values(['openInterest'],ascending=False)
    new_PE_DT = pd.DataFrame(new_pe_dt).sort_values(['openInterest'],ascending=False)

    new_long_unwind = pd.DataFrame(long_unwind).sort_values(['openInterest'],ascending=False)

    new_CE = new_CE_DT.iloc[:40, [3,4,5,6,7,8,9,10,11]]
    new_PE = new_PE_DT.iloc[:20, [3,4,5,6,7,8,9,10,11]]
    
    new_long_Unwind = new_long_unwind.iloc[:30, [3,4,5,6,7,8,9,10,11]]

    #print("Printing OI for Call Options")
    #print(new_CE)
    #print("Printing OI for Put Options")
    #print(new_PE)
    print("\n\nPrinting Long UnWind")
    print(new_long_Unwind)

def main():
    expiry_dt = '22-Apr-2021'
    fetch_oi(expiry_dt)

if __name__ == '__main__':
    main()

