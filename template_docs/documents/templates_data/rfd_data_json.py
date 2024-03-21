from documents.templates_data.rfd_conditions import conditions , conditions_rfd_waybill

rfd_data ={
        #Podstawowe informacje
         'logo_url': 'documents/static/images/nova_logo.png',
         'template_language': 'en',
         'issuer': ' Mikita Kharko',
         'phone_issuer' : '+48546654543',
         'email_issuer': ' m.kharko@nova-tracking.com',
         'branch_issuer' : 'NOVA TRACKING SPÓŁKA Z OGRANICZONĄ ODPOWIEDZIALNOŚCIĄ /o. Warszawa',
         'nip':'PL9532641810',
         'city' : 'Warsaw',
         'date' : '04.01.2024',
         #tytuł dokumentu
         'document_type' : 'Zlecenie transportowe',
         'shipment_number' : 'NOV/009938/23/4',
         'info_about_invoice': 'Proszę podać na fakturze nr zlecenia',
         #dane przewoźnika
         'carrier':'Nova Tracking Sp. z o.o.',
         'carrier_address' :'ul. Zagrodnicza 20, 61-654 Poznań',
         'carrier_nip' :' 9532641810',
         'contact_person' : ['Jakub Malinowski' , 'Marcin Hajdul'], #może być array
         #dane dla rfdWaybill carrier
         'carrier_street':'ul. Zagrodnicza 20',
         'carrier_postal_code':'61-654',
         'carrier_city':'Poznań',
         'carrier_licension_nr':'3332221233',
         #srodek transportu
         'truck':'DW123454',
         'trailer' :'DW345444',
         'vehicle_type' : 'plandeka',
         'driver':'Marek Kowalski',
         'driver_id_card':'CB1234567',   #prawo jazdy
         'driver_passport':'ABC123456',
         'driver_phone':'604104102',
         #points for rfw shipping instruction
         'poi_points' : [
             {
                'name': 'FIRMA OPONIARSKA TC DĘBICA S.A.',
                'street':'1 Maja',
                'building_nr': '1',
                'country_code': 'PL',
                'postal_code': '39-208',
                'city': 'Dębica',
                'country': 'Polska',
                'open_hour': '09:00',
                'close_hour': '18:00',
                'date' : '2023-10-09, 08:00',
                #dla rfdWaybill  poistart
                'start_date':'2023-10-09 08:00',
                ######
                #cała lista ładunków dla poszczególnych punktów
                'actions':{
                    'poi_load' : [
                        {
                            'CBM' : '242',
                            'name': 'Buty',
                            'quantity':'450',
                            'weight_brutto':'24000',
                            'length' : '23',
                            'height': '43',
                            'width': '32',
                            'type': 'pallets',
                            'info': 'Attention fragile',
                            'dimensions': '32 X 12 X 53',
                            'total_weight' : '48000',
                        },
                        {
                            'CBM' : '325',
                            'name': 'Kwiaty',
                            'quantity':'450',
                            'weight_brutto':'24000',
                            'length' : '23',
                            'height': '43',
                            'width': '32',
                            'type': 'pallets',
                            'info': 'Testowe uwagi do ładunku',
                            'dimensions': '23 X 45 X 56',
                            'total_weight': '48000',
                       },
                        ],
                    'poi_custom':[
                        {
                            'CBM' : '242',
                            'name': 'Buty',
                            'quantity':'450',
                            'weight_brutto':'24000',
                            'length' : '23',
                            'height': '43',
                            'width': '32',
                            'type': 'pallets',
                            'info': 'Fragile',
                            'total_weight' : '48000', 
                        }
                    ],
                    'poi_unload' :[
                        {
                            'CBM' : '242',
                            'name': 'Buty',
                            'quantity':'450',
                            'weight_brutto':'24000',
                            'length' : '23',
                            'height': '43',
                            'width': '32',
                            'type': 'pallets',
                            'info': 'Attention fragile',
                            'dimensions': '32 X 12 X 53',
                            'total_weight' : '48000',
                        }
                    ],
                    'poi_open_t1':[
                        {
                            'CBM' : '242',
                            'name': 'Buty',
                            'quantity':'450',
                            'weight_brutto':'24000',
                            'length' : '23',
                            'height': '43',
                            'width': '32',
                            'type': 'pallets',
                            'info': 'Attention fragile',
                            'dimensions': '32 X 12 X 53',
                            'total_weight' : '48000',
                        }
                    ],
                    'poi_port_out':[
                        {
                            'CBM' : '242',
                            'name': 'Buty',
                            'quantity':'450',
                            'weight_brutto':'24000',
                            'length' : '23',
                            'height': '43',
                            'width': '32',
                            'type': 'pallets',
                            'info': 'Attention fragile',
                            'dimensions': '32 X 12 X 53',
                            'total_weight' : '48000',
                        }
                    ],
                    'poi_document_reciept':[
                        {
                            'CBM' : '242',
                            'name': 'Buty',
                            'quantity':'450',
                            'weight_brutto':'24000',
                            'length' : '23',
                            'height': '43',
                            'width': '32',
                            'type': 'pallets',
                            'info': 'Attention fragile',
                            'dimensions': '32 X 12 X 53',
                            'total_weight' : '48000',
                        }
                    ],
                    'poi_empty_road':[
                        {
                            'CBM' : '242',
                            'name': 'Buty',
                            'quantity':'450',
                            'weight_brutto':'24000',
                            'length' : '23',
                            'height': '43',
                            'width': '32',
                            'type': 'pallets',
                            'info': 'Attention fragile',
                            'dimensions': '32 X 12 X 53',
                            'total_weight' : '48000',
                        }
                    ],
                    'poi_unload_empty':[
                        {
                            'CBM' : '242',
                            'name': 'Buty',
                            'quantity':'450',
                            'weight_brutto':'24000',
                            'length' : '23',
                            'height': '43',
                            'width': '32',
                            'type': 'pallets',
                            'info': 'Attention fragile',
                            'dimensions': '32 X 12 X 53',
                            'total_weight' : '48000',
                        }
                    ],
                    'poi_load_full':[
                        {
                            'CBM' : '242',
                            'name': 'Buty',
                            'quantity':'450',
                            'weight_brutto':'24000',
                            'length' : '23',
                            'height': '43',
                            'width': '32',
                            'type': 'pallets',
                            'info': 'Attention fragile',
                            'dimensions': '32 X 12 X 53',
                            'total_weight' : '48000',
                        }
                    ],
                    'poi_unload_full':[
                        {
                            'CBM' : '242',
                            'name': 'Buty',
                            'quantity':'450',
                            'weight_brutto':'24000',
                            'length' : '23',
                            'height': '43',
                            'width': '32',
                            'type': 'pallets',
                            'info': 'Attention fragile',
                            'dimensions': '32 X 12 X 53',
                            'total_weight' : '48000',
                        }
                    ],
                    'poi_port_in':[
                        {
                            'CBM' : '242',
                            'name': 'Buty',
                            'quantity':'450',
                            'weight_brutto':'24000',
                            'length' : '23',
                            'height': '43',
                            'width': '32',
                            'type': 'pallets',
                            'info': 'Attention fragile',
                            'dimensions': '32 X 12 X 53',
                            'total_weight' : '48000',
                        } 
                    ]
                },
                'ref_number' : 'CDSA4562311',
                'contact_person' : 'Bartosz',
                'contact_person_phone' : '6785334322',
                'info':'Po zaladunku odprawa adres sms\n ttt  weer'
             },
             {
                'name': 'Mahle Behr Ostrow Wielkopolski Sp.',
                'street':'Wodna',
                'building_nr': '15',
                'country_code': 'PL',
                'postal_code': '63-400',
                'city': 'Ostrów Wielkopolski',
                'country': 'Polska',
                'open_hour': '09',
                'close_hour': '18',
                'date' : '2023-10-10, 10:00',
                #dla rfdWaybill  poistart
                'start_date':'2023-10-10 10:00',
                #####
                'actions':{
                    'poi_load' : [
                        {
                            'CBM' : '242',
                            'name': 'Buty',
                            'quantity':'450',
                            'weight_brutto':'24000',
                            'length' : '23',
                            'height': '43',
                            'width': '32',
                            'type': 'pallets',
                            'info': '',
                            'total_weight' : '48000',
                        },
                    ],
                    'poi_custom':[
                        {
                            'CBM' : '242',
                            'name': 'Buty',
                            'quantity':'450',
                            'weight_brutto':'24000',
                            'length' : '23',
                            'height': '43',
                            'width': '32',
                            'type': 'pallets',
                            'info': '',
                            'total_weight' : '48000',
                        },
                    ],
                    'poi_unload' :[
                        {
                            'CBM' : '242',
                            'name': 'Buty',
                            'quantity':'450',
                            'weight_brutto':'24000',
                            'length' : '23',
                            'height': '43',
                            'width': '32',
                            'type': 'pallets',
                            'info': '',
                            'total_weight' : '48000',
                        },
                        {
                            'CBM' : '',
                            'name': 'Kwiaty',
                            'quantity':'450',
                            'weight_brutto':'24000',
                            'length' : '23',
                            'height': '43',
                            'width': '32',
                            'type': 'pallets',
                            'info': 'Testowe uwagi do ładunku',
                            'dimensions': '',
                            'total_weight': '48000',
                        },
                    ],
                    'poi_open_t1':[
                        {
                            'CBM' : '242',
                            'name': 'Buty',
                            'quantity':'450',
                            'weight_brutto':'24000',
                            'length' : '23',
                            'height': '43',
                            'width': '32',
                            'type': 'pallets',
                            'info': '',
                            'total_weight' : '48000',
                        },
                    ],
                    'poi_port_out':[
                        {
                            'CBM' : '242',
                            'name': 'Buty',
                            'quantity':'450',
                            'weight_brutto':'24000',
                            'length' : '23',
                            'height': '43',
                            'width': '32',
                            'type': 'pallets',
                            'info': '',
                            'total_weight' : '48000',
                        },
                    ],
                    'poi_document_reciept':[
                        {
                            'CBM' : '242',
                            'name': 'Buty',
                            'quantity':'450',
                            'weight_brutto':'24000',
                            'length' : '23',
                            'height': '43',
                            'width': '32',
                            'type': 'pallets',
                            'info': '',
                            'total_weight' : '48000',
                        },
                    ],
                    'poi_empty_road':[
                        {
                            'CBM' : '242',
                            'name': 'Buty',
                            'quantity':'450',
                            'weight_brutto':'24000',
                            'length' : '23',
                            'height': '43',
                            'width': '32',
                            'type': 'pallets',
                            'info': '',
                            'total_weight' : '48000',
                        },
                    ],
                    'poi_unload_empty':[
                        {
                            'CBM' : '242',
                            'name': 'Buty',
                            'quantity':'450',
                            'weight_brutto':'24000',
                            'length' : '23',
                            'height': '43',
                            'width': '32',
                            'type': 'pallets',
                            'info': '',
                            'total_weight' : '48000',
                        },
                    ],
                    'poi_load_full':[
                        {
                            'CBM' : '242',
                            'name': 'Buty',
                            'quantity':'450',
                            'weight_brutto':'24000',
                            'length' : '23',
                            'height': '43',
                            'width': '32',
                            'type': 'pallets',
                            'info': '',
                            'total_weight' : '48000',
                        },
                    ],
                    'poi_unload_full':[
                        {
                            'CBM' : '242',
                            'name': 'Buty',
                            'quantity':'450',
                            'weight_brutto':'24000',
                            'length' : '23',
                            'height': '43',
                            'width': '32',
                            'type': 'pallets',
                            'info': '',
                            'total_weight' : '48000',
                        },
                    ],
                    'poi_port_in':[
                        {
                            'CBM' : '242',
                            'name': 'Buty',
                            'quantity':'450',
                            'weight_brutto':'24000',
                            'length' : '23',
                            'height': '43',
                            'width': '32',
                            'type': 'pallets',
                            'info': '',
                            'total_weight' : '48000',
                        },
                    ]
                },
                'ref_number' : 'CDSA4562311',
                'contact_person' : 'Adam Nowak',
                'contact_person_phone' : '6785554322',
                'info':'Załadunek rampa 23'
             }
         ],
         #dla rfd waybill są wybierane ładunki które mają typ LOAD
          'cargos': [
              {
                'CBM' : '242',
                'name': 'Buty',
                'quantity':'450',
                'weight_brutto':'24000',
                'length' : '23',
                'height': '43',
                'width': '32',
                'type': 'pallets',
                'info': 'Towar na paletach',
                'dimensions': '23 X 45 X 12',
                'total_weight' : '48000',
              },
              {
                'CBM' : '123',
                'name': 'Kwiaty',
                'quantity':'450',
                'weight_brutto':'24000',
                'length' : '23',
                'height': '43',
                'width': '32',
                'type': 'pallets',
                'info': 'Testowe uwagi do ładunku',
                'dimensions': '12 X 23 X 12',
                'total_weight': '48000',
              }
          ],
         #payments
         "prefix_or_txt_arr":
              ['',
               "lub"],
         'fracht_txt_arr':
            ["Fracht przewozowy 1200 PLN netto + VAT",
              "Fracht przewozowy 2 037,00 PLN netto + VAT"
            ],
         'payment_term_txt_arr':
              ["Termin p\u0142atno\u015bci: 60 dni od daty wystawienia",
                "Termin p\u0142atno\u015bci: 7 dni od od daty otrzymania dokumentu"
              ],
         'fracht': '1200',
         'fracht_currency':'PLN',
         'goods_value': 2300,
         'goods_value_currency' : 'EUR',
         'extra_cost' : 1200,
         'extra_cost_currency': 'EUR',
         'shipment_note': 'Notatka ogólna test',
         'shipment_internal_note' : 'Notatka wewnętrzna test\nZ nowej string',
         #Dane dla zlecnia LCL SEA
         #'pin': '3444533',
         #'ref_number':'TRSU1233',
         #'custom_type':'T1',
         #'custom_point': 'HERMES" SPÓŁKA Z OGRANICZONĄ ODPOWIEDZIALNOŚCIĄ \n Legionów 87, 81-413, Gdynia, PL',
         'pallets_return': 'Zwrot palet 12.06.2024',
         'documents_return':'Zwrot dokumnetów do 21 w piątek',
         'conditions': 'Warunki zlecenia rfdShippingInstruction',
         'conditions_rfd_waybill': 'Warunki dla listu przewozowego',
         'branch':{
             'phone':'5671239876',
             'fax':'0048 123334512',
             'email':'test@nova-tracking.com',
             'full_name':'NOVA TRACKING SPÓŁKA Z OGRANICZONĄ ODPOWIEDZIALNOŚCIĄ /o. Warszawa',
             'street':'Aleje Jerozolimskie 33',
             'postal_code':'00-200',
             'city':'Warszawa'
         },
         'company_user':{
             'full_name':'Nova Tracking Sp. z o.o.',
             'phone':'5671239876',
             'fax':'0048 123334512',
             'nip': '9532641810' ,
             'regon':'34153695000000',
             'street':'ul Zagrodnicza 20',
             'postal_code':'61-654',
             'city':'Poznań'
             
         },
         'conditions': conditions,
         'conditions_rfd_waybill': conditions_rfd_waybill


}