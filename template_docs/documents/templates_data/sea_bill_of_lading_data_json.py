

sea_bol_data = {
    'logo_url':'documents/static/images/nova_logo.png',
    'document_title':'BILL OF LADING', #BILL OF LADING or SEA WAYBILL
    'bl_number': 'BOL-1711469537',
    'shipper':{
        'name':'POLMLEK SP. Z O. O',
        'street': 'HOZA 51',
        'postal_code':'00-681',
        'city':'WARSZAWA',
        'country': 'POLAND',
        'country_prefix':'PL',
        'additional_info': 'Additional info for shipper',
    },
    'consignee':{
        'name':'1UP CARGO INC',
        'street': '20 BAY STREET, 11TH FLOOR',
        'postal_code':'M5J 2N8',
        'city':'TORONTO',
        'country': 'CANADA',
        'country_prefix':'CA',
        'additional_info': 'Additional info for consignee',
    },
    'agent':{
        'name':'AIRPORT HANDLING SERVICES SP. Z O. O.',
        'street': 'Jasionka 942',
        'postal_code':'36-002',
        'city':'Jasionka',
        'country': 'POLAND',
        'country_prefix':'PL',
        'additional_info': 'Additional info for agent',
    },
    'notify_party':'SAME AS CONSIGNEE',
    'pre_carriage':{}, # ???????
    'place_of_reciept':'Hong Kong',
    'vessel' : 'Madison Maersk',
    'voy_no':'v77777',
    'port_of_loading':'Hong Kong',
    'port_of_discharge':'GDANSK',
    'place_of_delivery':'GDANSK',
    'final_destination_for_merchants_reference':'WROCLAW',
    'containers':[
        {
            'number':'TCLU3143317',
            'type':'20DV',
            'seals': [
               's11111',
               's2222',
               's3333'
            ],
            'cargo':[
                {
                    'name':'shoes',
                    'package_type':'pallets',
                    'quantity': '12',
                    'weight': '1200 KG',
                    'dimensions':'230 CBM'
                },
                 {
                    'name':'cargo1',
                    'package_type':'pallets',
                    'quantity': '12',
                    'weight': '1200 KG',
                    'dimensions':'320 CBM'
                }
            ]
        },
        {
            'number':'TGHU3143317',
            'type':'40DV',
            'seals': [
               's11111',
               's2222',
            ],
            'cargo':[
                {
                    'name':'shoes',
                    'package_type':'pallets',
                    'quantity': '12',
                    'weight': '1200 KG',
                    'dimensions':'128 CBM'
                },
                 {
                    'name':'cargo1',
                    'package_type':'pallets',
                    'quantity': '12',
                    'weight': '1200 KG',
                    'dimensions':'230 CBM'
                },
                {
                    'name':'cargo1',
                    'package_type':'pallets',
                    'quantity': '12',
                    'weight': '1200 KG',
                    'dimensions':'230 CBM'
                }
            ]
        },
        {
            'number':'CBHU3143317',
            'type':'40HC',
            'seals': [
               's11111',
               's2222',
               's3333'
            ],
            'cargo':[
                {
                    'name':'shoes',
                    'package_type':'pallets',
                    'quantity': '12',
                    'weight': '1200 KG',
                    'dimensions':'128 CBM'
                },
                 {
                    'name':'cargo1',
                    'package_type':'pallets',
                    'quantity': '12',
                    'weight': '1200 KG',
                    'dimensions':'230 CBM'
                }
            ]
        }
    ],
    'weight' : '2300 KGS',
    'measurement' : '120 CBM',
    'rate': '10 ',
    'per' : 'KG',
    'amount': '23000 ',
    'currency' : 'USD',
    'total_cargo_weight':'2100 KGS',
    'freight_payment_type': 'Freight prepaid', #Freight collect 
    'freight_payable_at' : 'Destination',
    'shipped_on_board_date': '17.04.2024',
    'dated_on':'28.04.2024',
    'dated_place':'POZNAN'


}

