corrective_note_data = {
    'document_language': 'pl',
    'corrective_note_number':'FVK/000354/11/23',
    'corrective_note_issue_date':'2024-02-17',
    'correcting_document':'FVK/000354/11/23',
    'from_date':' 2023-12-14',
    'regarding_sales_from_date':'2023-12-14',
    'logo_url':'documents/static/images/nova_logo.png',
    'duplicate_from_date':'2024-01-31', # Duplikat
    'stamp_url':'documents/static/images/nova_logo.png',
    'document_currency':'EUR',
    'currency':'PLN', #Waluta systemowa
    'sender':{
        'name': 'PEKAO - CARGO Agencja Celna Sp. z o.o.',
        'street':'ul. Wirażowa',
        'building_number':'35',
        'postal_code':'02-158',
        'city':'Warszawa',
        'country':'Poland',
        'vat_id':'PL5220103271', 
        'transfer_details':{
           'eur': 'Pekao S.A.',
           'swift_code': 'PKOPPLPWXXX\nPL57 1240 1037 1978 0000 0691 7997',
           'vat_pl':'Pekao S.A.',
           'swift_code_pl':'PKOPPLPWXXX\nPL31 1240 1037 1111 0000 0691 7971'
        },
     },
     'recipient':{
        'name':'MIKKA - HANSEN R. WĄSIK SPÓŁKA JAWNA',
        'street':': ul. Sebastiana Klonowica' ,
        'building_number':'24/67',
        'postal_code':'02-158',
        'city':' Kraków',
        'country':'Poland',
        'vat_id':'PL6793176807'
      },
      'addresse':{
          'name': 'MIKKA - HANSEN R. WĄSIK SPÓŁKA JAWNA',
          'street':' Tuchowska',
          'building_nr':'76a',
          'postal_code':'33-100',
          'city':'Tarnów',
          'country':'Polska'
      },
    'forwarding_position':'PEKAO/0261/01/24',
    'notes':'TCNU8225333 \n\n 40 HC - TCNU8225333 \n CN SHA - Shanghai -> - BalticHub Gdańsk SA',
    'correction_reasons':[
        'Incorrect buyer data',
        'Accepted complaint',
        'VAT rate change',
        'Incorrect description of the service object'
     ],
     'type_currency_document': 2,
     'items':[
        {
            'orig':{
                'title':'Fracht morski',
                'quantity':'1',
                'measure_unit':'pcs',
                'unit_price':'1 200,00 ',
                'tax':'23%',
                'amount':'1 200,00',
                'tax_amount':'276,00',
                'total':'1 476,00',
                'currency':'PLN',
                    # For multi currency invoice type(2)
                'exchange_rate':'0,2309',
                'amount_in_document_currency':'277,08',
                'tax_amount_in_document_currency':'63,73',
                'total_in_document_currency':'340,81'
            },
            'fix':{
                'title':'Fracht morski',
                'quantity':'1',
                'measure_unit':'pcs', 
                'unit_price':'1 000,00 ',
                'tax':'23%',
                'amount':'1 000,00',
                'tax_amount':'',
                'total':'',
                'currency':'PLN',
                # For multi currency invoice type(2)
                'exchange_rate':'0,2309',
                'amount_in_document_currency':'230,90',
                'tax_amount_in_document_currency':'53,11',
                'total_in_document_currency':'284,01'  
            },
            'diffrence':{
                'title':'Fracht morski',
                'quantity':'0',
                'measure_unit':'pcs', 
                'unit_price':'-200',
                'tax':'23%',
                'amount':'-200',
                'tax_amount':'',
                'total':'',
                'currency':'PLN',
                # For multi currency invoice type(2)
                'exchange_rate':'0,2309',
                'amount_in_document_currency':'-46,18',
                'tax_amount_in_document_currency':'-10,62',
                'total_in_document_currency':'-56,80' 
            }
        },
        {
            'orig':{
                'title':'THC',
                'quantity':'1',
                'measure_unit':'pcs',
                'unit_price':'1 300,00',
                'tax':'8%',
                'amount':'1 300,00',
                'tax_amount':'104,00',
                'total':'1 404,00',
                'currency':'PLN',
                # For multi currency invoice type(2)
                'exchange_rate':'0,2309 ',
                'amount_in_document_currency':'300,17',
                'tax_amount_in_document_currency':'24,01',
                'total_in_document_currency':'324,18'
            },
            'fix':{
                'title':'THC',
                'quantity':'1',
                'measure_unit':'pcs',
                'unit_price':'1 300,00',
                'tax':'23%',
                'amount':'1 300,00',
                'tax_amount':'104,00',
                'total':'1 404,00',
                'currency':'PLN',
                # For multi currency invoice type(2)
                'exchange_rate':'0,2309 ',
                'amount_in_document_currency':'300,17',
                'tax_amount_in_document_currency':'69,04',
                'total_in_document_currency':'369,21'

            },
            'diffrence':{
                'title':'THC',
                'quantity':'0',
                'measure_unit':'pcs',
                'unit_price':'0,00',
                'tax':'23%',
                'amount':'0,00',
                'tax_amount':'104,00',
                'total':'',
                'currency':'PLN',
                # For multi currency invoice type(2)
                'exchange_rate':'0,2309 ',
                'amount_in_document_currency':'0,00',
                'tax_amount_in_document_currency':'45,03',
                'total_in_document_currency':'45,03'   
            }
        },
        {
            'orig':{
                'title':'Opłata dokumentacyjna',
                'quantity':'1',
                'measure_unit':'pcs',
                'unit_price':'2 300,00',
                'tax':'8%',
                'amount':'2 300,00',
                'tax_amount':'184,00',
                'total':'2 484,00',
                'currency':'PLN',
                # For multi currency invoice type(2)
                'exchange_rate':'0,2309',
                'amount_in_document_currency':'531,07',
                'tax_amount_in_document_currency':'42,49',
                'total_in_document_currency':'573,56'
            },
            'fix':{
                'title':'Opłata dokumentacyjna',
                'quantity':'1',
                'measure_unit':'pcs',
                'unit_price':'2 100,00',
                'tax':'8%',
                'amount':'2 100,00',
                'tax_amount':'',
                'total':'',
                'currency':'PLN',
                # For multi currency invoice type(2)
                'exchange_rate':'0,2309',
                'amount_in_document_currency':'484,89',
                'tax_amount_in_document_currency':'38,79',
                'total_in_document_currency':'523,68'
            },
            'diffrence':{
                'title':'Opłata dokumentacyjna',
                'quantity':'1',
                'measure_unit':'pcs',
                'unit_price':'-200,00',
                'tax':'8%',
                'amount':'-200,00',
                'tax_amount':'',
                'total':'',
                'currency':'PLN',
                # For multi currency invoice type(2)
                'exchange_rate':'0,2309',
                'amount_in_document_currency':'-46,18',
                'tax_amount_in_document_currency':'-3,70',
                'total_in_document_currency':'-49,88'
            }
        },
     ],
    'way_of_payment': 'Bank Transfer',
    'day_of_payment':'2023-02-15',
    'split_payment': 1,
    'tax_diffrence':[
        {
         'tax_rate':'8%',
         'net':'-831,24',
         'tax':'-66,50',
         'gross':'-897,74'
        },
        {
         'tax_rate':'23%',
         'net':'738,88',
         'tax':'169,94',
         'gross':'908,82'
        }
    ],
    'total_diffrence':
        {
            'net':'92,36',
            'tax':'103,44',
            'gross':'11,08'        
        },
    'original_document_tax':{
        'tax_in_document_currency':'130,23',
        'tax_in_system_currency':'564,01',
    },
    'exchange_rate_original_document': #before correction 
          {
            'currency':'EUR',
            'rate':'4,3309',
            'quote_currency':'PLN',
            'provider_name':'Narodowy Bank Polski',
            'table_name':'241/A/NBP/2023',
            'table_date':'2023-12-13',

          },
    'document_tax':{
        'tax_in_document_currency':'160,94',
        'tax_in_system_currency':'697,02'
    },
    'exchange_rate_document':{ #after correction
            'currency':'EUR',
            'rate':'4,3309',
            'quote_currency':'PLN',
            'provider_name':'Narodowy Bank Polski',
            'table_name':'241/A/NBP/2023',
            'table_date':'2023-12-13',
    },
    'amount_of_tax_increase': {
        'amount_in_currency':'447,99',
        'amount_in_document_currency':'103,44',
    },
    'exchange_rates':[ # for exchange rate section
        {
            'currency':'PLN',
            'rate':'0,2309',
            'quote_currency':'EUR',
            'provider_name':'Narodowy Bank Polski',
            'table_name':'241/A/NBP/2023',
            'table_date':'2023-12-13',
        },
        #  {
        #     'currency':'BYN',
        #     'rate':'0,2309',
        #     'quote_currency':'EUR',
        #     'provider_name':'Narodowy Bank Polski',
        #     'table_name':'241/A/NBP/2023',
        #     'table_date':'2023-12-13',
        # },
        

    ], #prowerit jawlyaetsya li eto massiwom ili net
    'exchange_rate_provider_name':'Narodowy Bank Polski',
    'exchange_rate_table_name':'241/A/NBP/2023',
    'exchange_rate_date':'2023-12-13',
    'issuer_name':"Mikita Kharko",

    'total_to_pay':{

    },
   'stamp_url':'documents/static/images/nova_logo.png',

    
}