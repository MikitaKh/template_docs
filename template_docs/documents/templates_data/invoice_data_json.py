
invoice_data={
    'invoice_number':' FVK/000354/11/23',
    'logo_url':'documents/static/images/nova_logo.png',
    'stamp_url':'documents/static/images/nova_logo.png',
    'issue_date':'2024-02-06',
    'service_date':'2024-01-31',
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
      'forwarding_position':'PEKAO/0263/01/24 PEKAO/0270/01/24',
      'type_currency_document': 2,  # single currency or multi currency document
      'document_currency': 'EUR',
      'currency':'PLN', #Waluta systemowa
      'document_exchange_rate':'4,3309',
      'document_language':'en',
      'items':[
          {
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
           {
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
           {
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

          }
      ],
      'way_of_payment': 'Bank Transfer',
      'day_of_payment':'2023-02-15',
      'split_payment' : 'Split Payment Method',
      'summary_in_converted_currency':[
          {
              'tax_rate':'8%',
              'net_value':'831,24 ',
              'tax_value':'66,50',
              'gross_value':'897,74' 
          },
          {
              'tax_rate':'23%',
              'net_value':'277,08',
              'tax_value':'63,73',
              'gross_value':'340,81'
          }

      ],
      'summary_grand_total_in_converted_currency':{
          'net_value': '1 108,32',
          'tax_value':'130,23',
          'gross_value': '1 238,55'
      },
      'summary':[
          {
              'tax_rate':'8%',
              'net_value':'3 600,02',
              'tax_value':'288,00',
              'gross_value':'3 888,02'  
          },
          {
               'tax_rate':'23%',
              'net_value':'1 200,01',
              'tax_value':'276,01',
              'gross_value':'1 476,02' 
          }
      ],
      'summary_grand_total':{
              'net_value':'4 800,03',
              'tax_value':'564,01',
              'gross_value':'5 364,04'
      },
      'exchange_rates':[
          {
            'base_currency':'PLN',
            'rate':'0,2309',
            'quote_currency':' EUR'
          },
        #   {
        #      'base_currency':'BRL',
        #      'rate':'0,1867',
        #      'quote_currency':'EUR'
        #   }

      ],
      'exchange_rate_provider_name':'Narodowy Bank Polski',
      'exchange_rate_table_name':'241/A/NBP/2023',
      'exchange_rate_date':'2023-12-13',
      'notes':"-> - Punta Caucedo, Santo Domingo, Dominican",
      'issuer_name':"Mikita Kharko",
      


          
      


}


