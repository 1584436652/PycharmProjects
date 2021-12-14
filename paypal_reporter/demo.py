'''
@Time    : 2021/10/9 19:17
@Author  : LKT
@FileName: demo.py
@Software: PyCharm
 
'''
import json
from paypal import PayPalInterface


paypal_api = PayPalInterface(

    API_USERNAME='sb-kiw4k8056759_api1.business.example.com',

    API_PASSWORD='7QZJLNW2HJFZUCBR',

    API_SIGNATURE='ASXdDrlbTVyCpgzeV32eDNNYww9lAifsgY8B7KlOxQgmjM-TzW1OyNPy',

    API_ENVIRONMENT='SANDBOX',  # ['SANDBOX', 'PRODUCTION'],

    API_AUTHENTICATION_MODE='3TOKEN', # ['3TOKEN', 'CERTIFICATE']

    DEBUG_LEVEL=0,

    HTTP_TIMEOUT=30
)



# https://developer.paypal.com/docs/classic/api/merchant/GetRecurringPaymentsProfileDetails_API_Operation_NVP/

balance_details = paypal_api._call('GetBalance')

print(balance_details)

print(balance_details['L_AMT0'] + ' ' + balance_details['L_CURRENCYCODE0'])

pal_details = paypal_api._call('GetPalDetails')

print(pal_details)