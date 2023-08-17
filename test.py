import json
import helper
# Response used for testing purpose
response_data2 =  """{
  "success": true,
  "message": "Operation successful.",
  "data": {
    "search_query": {
      "route_type": "ONEWAY",
      "cabin_class": {
        "code": "Y",
        "label": "Economy"
      },
      "traveler_count": {
        "num_adult": 1,
        "num_child": 0,
        "num_infant": 0
      },
      "non_stop_flight": false,
      "legs": [
        {
          "origin": {
            "name": "Jinnah International Airport",
            "airport": "Jinnah International Airport",
            "city": "Karachi",
            "is_city": false,
            "city_airports": null,
            "iata_code": "KHI",
            "time_zone": "Asia/Karachi",
            "country": "Pakistan"
          },
          "destination": {
            "name": "Allama Iqbal International Airport",
            "airport": "Allama Iqbal International Airport",
            "city": "Lahore",
            "is_city": false,
            "city_airports": null,
            "iata_code": "LHE",
            "time_zone": "Asia/Karachi",
            "country": "Pakistan"
          },
          "departure_date": "2023-08-15"
        }
      ]
    },
    "cache_gaf_response": true,
    "provider_search_ids": {
      "AIRBLUE": "acc9266e-5290-469d-82c4-bdcd4683baf4",
      "PIAAPI": "d684e441-05d8-4231-b846-223e40558db2",
      "AIRSIAL": "d27a7cb1-3f8c-4152-b174-6b500338dffa",
      "SERENEAPI": "93cd0acb-bcbf-48e2-9b4f-d2f1f2e91d76",
      "FLYJINNAH": "18aba73b-5689-44cb-90c1-b7a686c6d569"
    },
    "is_international": false,
    "route_type": "ONEWAY",
    "flights": [
      [
        {
          "provider": "AIRSIAL",
          "is_refundable": true,
          "should_auto_ticket": true,
          "baggage_info": {
            "pieces": 1,
            "weight": 20.0,
            "unit": "KG",
            "max_weight_allowed_per_piece": null
          },
          "legs": [
            {
              "cabin_class": "Economy",
              "segments": [
                {
                  "origin": {
                    "name": "Jinnah International Airport",
                    "airport": "Jinnah International Airport",
                    "city": "Karachi",
                    "iata_code": "KHI",
                    "time_zone": "Asia/Karachi",
                    "country": "Pakistan"
                  },
                  "destination": {
                    "name": "Allama Iqbal International Airport",
                    "airport": "Allama Iqbal International Airport",
                    "city": "Lahore",
                    "iata_code": "LHE",
                    "time_zone": "Asia/Karachi",
                    "country": "Pakistan"
                  },
                  "departure_datetime": "2023-08-15T13:30:00",
                  "arrival_datetime": "2023-08-15T15:15:00",
                  "duration_minutes": 105,
                  "flight_number": [
                    "PF-143"
                  ],
                  "operating_airline": {
                    "name": "Airsial",
                    "code": "PF"
                  },
                  "marketing_airline": {
                    "name": "Airsial",
                    "code": "PF"
                  },
                  "rbd": "budget",
                  "meta": {
                    "class_code": "1036",
                    "journey_code": "330236"
                  },
                  "cabin_class": "Economy",
                  "is_stop": false,
                  "seats_remaining": null
                }
              ],
              "operating_airline": {
                "name": "Airsial",
                "code": "PF"
              },
              "is_refundable": true,
              "has_private_fare": false,
              "has_meal": true,
              "seats_remaining": null,
              "origin": "KHI",
              "destination": "LHE"
            }
          ],
          "position": 95,
          "rules": [
            225,
            551
          ],
          "hash": "399bb294ed7e7c4be3212a4bfb7205220690d112",
          "hash_rbd": "233e4aac8a9800ec044ebafb4c4d5ad5a27d8983",
          "fare_options": [
            {
              "itinerary_id": "CA68AC",
              "price": {
                "selling_fare": 15607,
                "published_fare": 14125.0,
                "gross_fare": 16270.0,
                "tax": 2145.0,
                "currency": "PKR",
                "breakdown": {
                  "adult": {
                    "base_fare": 14125.0,
                    "tax": 2145.0,
                    "total_fare": 15607,
                    "gross_fare": 16270.0
                  },
                  "child": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  },
                  "infant": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  }
                }
              },
              "related_itineraries": null,
              "hash_rbd": "233e4aac8a9800ec044ebafb4c4d5ad5a27d8983",
              "hash": "399bb294ed7e7c4be3212a4bfb7205220690d112",
              "combo": false,
              "offers": [
                {
                  "text": "1 piece(s) of 20kg total",
                  "icon": "standard_baggage"
                }
              ],
              "rbd": "budget",
              "cabin_class": "Economy",
              "has_meal": true,
              "baggage_info": {
                "pieces": 1,
                "weight": 20.0,
                "unit": "KG",
                "max_weight_allowed_per_piece": null
              },
              "is_refundable": true,
              "addons": [
                {
                  "code": "ADDON_FC",
                  "name": "Free Cancellation",
                  "description": "Free Cancellation on this booking.",
                  "enabled": true,
                  "options": [
                    {
                      "id": "624B21",
                      "cost": 750.0,
                      "description": "100% Refund Guarantee"
                    }
                  ],
                  "meta": {
                    "fc_premium_id": 10435443
                  }
                }
              ]
            },
            {
              "itinerary_id": "31C034",
              "price": {
                "selling_fare": 16357,
                "published_fare": 14125.0,
                "gross_fare": 16270.0,
                "tax": 2145.0,
                "currency": "PKR",
                "breakdown": {
                  "adult": {
                    "base_fare": 14125.0,
                    "tax": 2145.0,
                    "total_fare": 16357,
                    "gross_fare": 16270.0
                  },
                  "child": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  },
                  "infant": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  }
                }
              },
              "related_itineraries": null,
              "hash_rbd": "013f4c54f766615b59b7304a63fe76a7bdfcd428",
              "hash": "399bb294ed7e7c4be3212a4bfb7205220690d112",
              "combo": false,
              "offers": [
                {
                  "text": "1 piece(s) of 20kg total",
                  "icon": "standard_baggage"
                },
                {
                  "text": "Sasta Refund: Get a full refund of PKR 15,607/-. <a href='https://sastaticket.pk/pages/terms-and-conditions#free_cancellation' target='_blank'>T&C apply</a>",
                  "icon": "free_cancellation"
                }
              ],
              "rbd": "ST-FC",
              "cabin_class": "Economy",
              "has_meal": true,
              "baggage_info": {
                "pieces": 1,
                "weight": 20.0,
                "unit": "KG",
                "max_weight_allowed_per_piece": null
              },
              "is_refundable": true,
              "addons": []
            },
            {
              "itinerary_id": "B78126",
              "price": {
                "selling_fare": 16560,
                "published_fare": 15125.0,
                "gross_fare": 17270.0,
                "tax": 2145.0,
                "currency": "PKR",
                "breakdown": {
                  "adult": {
                    "base_fare": 15125.0,
                    "tax": 2145.0,
                    "total_fare": 16560,
                    "gross_fare": 17270.0
                  },
                  "child": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  },
                  "infant": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  }
                }
              },
              "related_itineraries": null,
              "hash_rbd": "cbbb1bf168bd9dc416a19df5c862bf6eecd2e54a",
              "hash": "399bb294ed7e7c4be3212a4bfb7205220690d112",
              "combo": false,
              "offers": [
                {
                  "text": "2 piece(s) of 40kg total",
                  "icon": "two_piece_bags"
                }
              ],
              "rbd": "extra bag",
              "cabin_class": "Economy",
              "has_meal": true,
              "baggage_info": {
                "pieces": 2,
                "weight": 40.0,
                "unit": "KG",
                "max_weight_allowed_per_piece": null
              },
              "is_refundable": true,
              "addons": [
                {
                  "code": "ADDON_FC",
                  "name": "Free Cancellation",
                  "description": "Free Cancellation on this booking.",
                  "enabled": true,
                  "options": [
                    {
                      "id": "359FD6",
                      "cost": 750.0,
                      "description": "100% Refund Guarantee"
                    }
                  ],
                  "meta": {
                    "fc_premium_id": 10435443
                  }
                }
              ]
            },
            {
              "itinerary_id": "E79F7B",
              "price": {
                "selling_fare": 17310,
                "published_fare": 15125.0,
                "gross_fare": 17270.0,
                "tax": 2145.0,
                "currency": "PKR",
                "breakdown": {
                  "adult": {
                    "base_fare": 15125.0,
                    "tax": 2145.0,
                    "total_fare": 17310,
                    "gross_fare": 17270.0
                  },
                  "child": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  },
                  "infant": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  }
                }
              },
              "related_itineraries": null,
              "hash_rbd": "423fa4d735c95d3838aa52b023552b3cd630271b",
              "hash": "399bb294ed7e7c4be3212a4bfb7205220690d112",
              "combo": false,
              "offers": [
                {
                  "text": "2 piece(s) of 40kg total",
                  "icon": "two_piece_bags"
                },
                {
                  "text": "Sasta Refund: Get a full refund of PKR 16,560/-. <a href='https://sastaticket.pk/pages/terms-and-conditions#free_cancellation' target='_blank'>T&C apply</a>",
                  "icon": "free_cancellation"
                }
              ],
              "rbd": "ST-FC",
              "cabin_class": "Economy",
              "has_meal": true,
              "baggage_info": {
                "pieces": 2,
                "weight": 40.0,
                "unit": "KG",
                "max_weight_allowed_per_piece": null
              },
              "is_refundable": true,
              "addons": []
            }
          ]
        },
        {
          "provider": "AIRSIAL",
          "is_refundable": true,
          "should_auto_ticket": true,
          "baggage_info": {
            "pieces": 1,
            "weight": 20.0,
            "unit": "KG",
            "max_weight_allowed_per_piece": null
          },
          "legs": [
            {
              "cabin_class": "Economy",
              "segments": [
                {
                  "origin": {
                    "name": "Jinnah International Airport",
                    "airport": "Jinnah International Airport",
                    "city": "Karachi",
                    "iata_code": "KHI",
                    "time_zone": "Asia/Karachi",
                    "country": "Pakistan"
                  },
                  "destination": {
                    "name": "Allama Iqbal International Airport",
                    "airport": "Allama Iqbal International Airport",
                    "city": "Lahore",
                    "iata_code": "LHE",
                    "time_zone": "Asia/Karachi",
                    "country": "Pakistan"
                  },
                  "departure_datetime": "2023-08-15T19:00:00",
                  "arrival_datetime": "2023-08-15T20:45:00",
                  "duration_minutes": 105,
                  "flight_number": [
                    "PF-145"
                  ],
                  "operating_airline": {
                    "name": "Airsial",
                    "code": "PF"
                  },
                  "marketing_airline": {
                    "name": "Airsial",
                    "code": "PF"
                  },
                  "rbd": "budget",
                  "meta": {
                    "class_code": "1036",
                    "journey_code": "330966"
                  },
                  "cabin_class": "Economy",
                  "is_stop": false,
                  "seats_remaining": null
                }
              ],
              "operating_airline": {
                "name": "Airsial",
                "code": "PF"
              },
              "is_refundable": true,
              "has_private_fare": false,
              "has_meal": true,
              "seats_remaining": null,
              "origin": "KHI",
              "destination": "LHE"
            }
          ],
          "position": 95,
          "rules": [
            225,
            551
          ],
          "hash": "1e28b9b02cc60c19ec5620b0c219507b27bce573",
          "hash_rbd": "c356991a66ace06cac114405a2e161b004757d14",
          "fare_options": [
            {
              "itinerary_id": "B2F540",
              "price": {
                "selling_fare": 15607,
                "published_fare": 14125.0,
                "gross_fare": 16270.0,
                "tax": 2145.0,
                "currency": "PKR",
                "breakdown": {
                  "adult": {
                    "base_fare": 14125.0,
                    "tax": 2145.0,
                    "total_fare": 15607,
                    "gross_fare": 16270.0
                  },
                  "child": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  },
                  "infant": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  }
                }
              },
              "related_itineraries": null,
              "hash_rbd": "c356991a66ace06cac114405a2e161b004757d14",
              "hash": "1e28b9b02cc60c19ec5620b0c219507b27bce573",
              "combo": false,
              "offers": [
                {
                  "text": "1 piece(s) of 20kg total",
                  "icon": "standard_baggage"
                }
              ],
              "rbd": "budget",
              "cabin_class": "Economy",
              "has_meal": true,
              "baggage_info": {
                "pieces": 1,
                "weight": 20.0,
                "unit": "KG",
                "max_weight_allowed_per_piece": null
              },
              "is_refundable": true,
              "addons": [
                {
                  "code": "ADDON_FC",
                  "name": "Free Cancellation",
                  "description": "Free Cancellation on this booking.",
                  "enabled": true,
                  "options": [
                    {
                      "id": "E01463",
                      "cost": 750.0,
                      "description": "100% Refund Guarantee"
                    }
                  ],
                  "meta": {
                    "fc_premium_id": 10435444
                  }
                }
              ]
            },
            {
              "itinerary_id": "98B83E",
              "price": {
                "selling_fare": 16357,
                "published_fare": 14125.0,
                "gross_fare": 16270.0,
                "tax": 2145.0,
                "currency": "PKR",
                "breakdown": {
                  "adult": {
                    "base_fare": 14125.0,
                    "tax": 2145.0,
                    "total_fare": 16357,
                    "gross_fare": 16270.0
                  },
                  "child": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  },
                  "infant": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  }
                }
              },
              "related_itineraries": null,
              "hash_rbd": "8a2b5bee771d808248e31adb7b7c6166c4213e4e",
              "hash": "1e28b9b02cc60c19ec5620b0c219507b27bce573",
              "combo": false,
              "offers": [
                {
                  "text": "1 piece(s) of 20kg total",
                  "icon": "standard_baggage"
                },
                {
                  "text": "Sasta Refund: Get a full refund of PKR 15,607/-. <a href='https://sastaticket.pk/pages/terms-and-conditions#free_cancellation' target='_blank'>T&C apply</a>",
                  "icon": "free_cancellation"
                }
              ],
              "rbd": "ST-FC",
              "cabin_class": "Economy",
              "has_meal": true,
              "baggage_info": {
                "pieces": 1,
                "weight": 20.0,
                "unit": "KG",
                "max_weight_allowed_per_piece": null
              },
              "is_refundable": true,
              "addons": []
            },
            {
              "itinerary_id": "138242",
              "price": {
                "selling_fare": 16560,
                "published_fare": 15125.0,
                "gross_fare": 17270.0,
                "tax": 2145.0,
                "currency": "PKR",
                "breakdown": {
                  "adult": {
                    "base_fare": 15125.0,
                    "tax": 2145.0,
                    "total_fare": 16560,
                    "gross_fare": 17270.0
                  },
                  "child": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  },
                  "infant": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  }
                }
              },
              "related_itineraries": null,
              "hash_rbd": "14249de516671c5462851981e60c2389a011b7d4",
              "hash": "1e28b9b02cc60c19ec5620b0c219507b27bce573",
              "combo": false,
              "offers": [
                {
                  "text": "2 piece(s) of 40kg total",
                  "icon": "two_piece_bags"
                }
              ],
              "rbd": "extra bag",
              "cabin_class": "Economy",
              "has_meal": true,
              "baggage_info": {
                "pieces": 2,
                "weight": 40.0,
                "unit": "KG",
                "max_weight_allowed_per_piece": null
              },
              "is_refundable": true,
              "addons": [
                {
                  "code": "ADDON_FC",
                  "name": "Free Cancellation",
                  "description": "Free Cancellation on this booking.",
                  "enabled": true,
                  "options": [
                    {
                      "id": "C9CF19",
                      "cost": 750.0,
                      "description": "100% Refund Guarantee"
                    }
                  ],
                  "meta": {
                    "fc_premium_id": 10435444
                  }
                }
              ]
            },
            {
              "itinerary_id": "583F96",
              "price": {
                "selling_fare": 17310,
                "published_fare": 15125.0,
                "gross_fare": 17270.0,
                "tax": 2145.0,
                "currency": "PKR",
                "breakdown": {
                  "adult": {
                    "base_fare": 15125.0,
                    "tax": 2145.0,
                    "total_fare": 17310,
                    "gross_fare": 17270.0
                  },
                  "child": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  },
                  "infant": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  }
                }
              },
              "related_itineraries": null,
              "hash_rbd": "7253c975ace02a91d3de1134b6352e87284258b3",
              "hash": "1e28b9b02cc60c19ec5620b0c219507b27bce573",
              "combo": false,
              "offers": [
                {
                  "text": "2 piece(s) of 40kg total",
                  "icon": "two_piece_bags"
                },
                {
                  "text": "Sasta Refund: Get a full refund of PKR 16,560/-. <a href='https://sastaticket.pk/pages/terms-and-conditions#free_cancellation' target='_blank'>T&C apply</a>",
                  "icon": "free_cancellation"
                }
              ],
              "rbd": "ST-FC",
              "cabin_class": "Economy",
              "has_meal": true,
              "baggage_info": {
                "pieces": 2,
                "weight": 40.0,
                "unit": "KG",
                "max_weight_allowed_per_piece": null
              },
              "is_refundable": true,
              "addons": []
            }
          ]
        },
        {
          "provider": "AIRSIAL",
          "is_refundable": true,
          "should_auto_ticket": true,
          "baggage_info": {
            "pieces": 1,
            "weight": 20.0,
            "unit": "KG",
            "max_weight_allowed_per_piece": null
          },
          "legs": [
            {
              "cabin_class": "Economy",
              "segments": [
                {
                  "origin": {
                    "name": "Jinnah International Airport",
                    "airport": "Jinnah International Airport",
                    "city": "Karachi",
                    "iata_code": "KHI",
                    "time_zone": "Asia/Karachi",
                    "country": "Pakistan"
                  },
                  "destination": {
                    "name": "Allama Iqbal International Airport",
                    "airport": "Allama Iqbal International Airport",
                    "city": "Lahore",
                    "iata_code": "LHE",
                    "time_zone": "Asia/Karachi",
                    "country": "Pakistan"
                  },
                  "departure_datetime": "2023-08-15T21:00:00",
                  "arrival_datetime": "2023-08-15T22:45:00",
                  "duration_minutes": 105,
                  "flight_number": [
                    "PF-147"
                  ],
                  "operating_airline": {
                    "name": "Airsial",
                    "code": "PF"
                  },
                  "marketing_airline": {
                    "name": "Airsial",
                    "code": "PF"
                  },
                  "rbd": "budget",
                  "meta": {
                    "class_code": "1041",
                    "journey_code": "442697"
                  },
                  "cabin_class": "Economy",
                  "is_stop": false,
                  "seats_remaining": null
                }
              ],
              "operating_airline": {
                "name": "Airsial",
                "code": "PF"
              },
              "is_refundable": true,
              "has_private_fare": false,
              "has_meal": true,
              "seats_remaining": null,
              "origin": "KHI",
              "destination": "LHE"
            }
          ],
          "position": 95,
          "rules": [
            225,
            551
          ],
          "hash": "241d9364d659e8f38c89b9d4f1671d590e15ae81",
          "hash_rbd": "5bfce3385f7fe63fe111cce9b6b4e9c39f200e22",
          "fare_options": [
            {
              "itinerary_id": "A07369",
              "price": {
                "selling_fare": 16775,
                "published_fare": 15350.0,
                "gross_fare": 17495.0,
                "tax": 2145.0,
                "currency": "PKR",
                "breakdown": {
                  "adult": {
                    "base_fare": 15350.0,
                    "tax": 2145.0,
                    "total_fare": 16775,
                    "gross_fare": 17495.0
                  },
                  "child": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  },
                  "infant": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  }
                }
              },
              "related_itineraries": null,
              "hash_rbd": "5bfce3385f7fe63fe111cce9b6b4e9c39f200e22",
              "hash": "241d9364d659e8f38c89b9d4f1671d590e15ae81",
              "combo": false,
              "offers": [
                {
                  "text": "1 piece(s) of 20kg total",
                  "icon": "standard_baggage"
                }
              ],
              "rbd": "budget",
              "cabin_class": "Economy",
              "has_meal": true,
              "baggage_info": {
                "pieces": 1,
                "weight": 20.0,
                "unit": "KG",
                "max_weight_allowed_per_piece": null
              },
              "is_refundable": true,
              "addons": [
                {
                  "code": "ADDON_FC",
                  "name": "Free Cancellation",
                  "description": "Free Cancellation on this booking.",
                  "enabled": true,
                  "options": [
                    {
                      "id": "074D96",
                      "cost": 750.0,
                      "description": "100% Refund Guarantee"
                    }
                  ],
                  "meta": {
                    "fc_premium_id": 10435445
                  }
                }
              ]
            },
            {
              "itinerary_id": "9A651A",
              "price": {
                "selling_fare": 17525,
                "published_fare": 15350.0,
                "gross_fare": 17495.0,
                "tax": 2145.0,
                "currency": "PKR",
                "breakdown": {
                  "adult": {
                    "base_fare": 15350.0,
                    "tax": 2145.0,
                    "total_fare": 17525,
                    "gross_fare": 17495.0
                  },
                  "child": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  },
                  "infant": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  }
                }
              },
              "related_itineraries": null,
              "hash_rbd": "d1d609c817897c67668325b1b9a5929bc9b774c9",
              "hash": "241d9364d659e8f38c89b9d4f1671d590e15ae81",
              "combo": false,
              "offers": [
                {
                  "text": "1 piece(s) of 20kg total",
                  "icon": "standard_baggage"
                },
                {
                  "text": "Sasta Refund: Get a full refund of PKR 16,775/-. <a href='https://sastaticket.pk/pages/terms-and-conditions#free_cancellation' target='_blank'>T&C apply</a>",
                  "icon": "free_cancellation"
                }
              ],
              "rbd": "ST-FC",
              "cabin_class": "Economy",
              "has_meal": true,
              "baggage_info": {
                "pieces": 1,
                "weight": 20.0,
                "unit": "KG",
                "max_weight_allowed_per_piece": null
              },
              "is_refundable": true,
              "addons": []
            },
            {
              "itinerary_id": "0263EB",
              "price": {
                "selling_fare": 17728,
                "published_fare": 16350.0,
                "gross_fare": 18495.0,
                "tax": 2145.0,
                "currency": "PKR",
                "breakdown": {
                  "adult": {
                    "base_fare": 16350.0,
                    "tax": 2145.0,
                    "total_fare": 17728,
                    "gross_fare": 18495.0
                  },
                  "child": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  },
                  "infant": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  }
                }
              },
              "related_itineraries": null,
              "hash_rbd": "14210cf73e7c282fd5f9c6cc7c071b6354bac21e",
              "hash": "241d9364d659e8f38c89b9d4f1671d590e15ae81",
              "combo": false,
              "offers": [
                {
                  "text": "2 piece(s) of 40kg total",
                  "icon": "two_piece_bags"
                }
              ],
              "rbd": "extra bag",
              "cabin_class": "Economy",
              "has_meal": true,
              "baggage_info": {
                "pieces": 2,
                "weight": 40.0,
                "unit": "KG",
                "max_weight_allowed_per_piece": null
              },
              "is_refundable": true,
              "addons": [
                {
                  "code": "ADDON_FC",
                  "name": "Free Cancellation",
                  "description": "Free Cancellation on this booking.",
                  "enabled": true,
                  "options": [
                    {
                      "id": "411D7F",
                      "cost": 750.0,
                      "description": "100% Refund Guarantee"
                    }
                  ],
                  "meta": {
                    "fc_premium_id": 10435445
                  }
                }
              ]
            },
            {
              "itinerary_id": "E1D960",
              "price": {
                "selling_fare": 18478,
                "published_fare": 16350.0,
                "gross_fare": 18495.0,
                "tax": 2145.0,
                "currency": "PKR",
                "breakdown": {
                  "adult": {
                    "base_fare": 16350.0,
                    "tax": 2145.0,
                    "total_fare": 18478,
                    "gross_fare": 18495.0
                  },
                  "child": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  },
                  "infant": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  }
                }
              },
              "related_itineraries": null,
              "hash_rbd": "a2bb9a103cef871472faec92cb6fb9154aa8c5c9",
              "hash": "241d9364d659e8f38c89b9d4f1671d590e15ae81",
              "combo": false,
              "offers": [
                {
                  "text": "2 piece(s) of 40kg total",
                  "icon": "two_piece_bags"
                },
                {
                  "text": "Sasta Refund: Get a full refund of PKR 17,728/-. <a href='https://sastaticket.pk/pages/terms-and-conditions#free_cancellation' target='_blank'>T&C apply</a>",
                  "icon": "free_cancellation"
                }
              ],
              "rbd": "ST-FC",
              "cabin_class": "Economy",
              "has_meal": true,
              "baggage_info": {
                "pieces": 2,
                "weight": 40.0,
                "unit": "KG",
                "max_weight_allowed_per_piece": null
              },
              "is_refundable": true,
              "addons": []
            }
          ]
        },
        {
          "provider": "SERENEAPI",
          "is_refundable": true,
          "should_auto_ticket": true,
          "baggage_info": {
            "pieces": 1,
            "weight": 20.0,
            "unit": "KG",
            "max_weight_allowed_per_piece": null
          },
          "legs": [
            {
              "cabin_class": "Economy",
              "segments": [
                {
                  "origin": {
                    "name": "Jinnah International Airport",
                    "airport": "Jinnah International Airport",
                    "city": "Karachi",
                    "iata_code": "KHI",
                    "time_zone": "Asia/Karachi",
                    "country": "Pakistan"
                  },
                  "destination": {
                    "name": "Allama Iqbal International Airport",
                    "airport": "Allama Iqbal International Airport",
                    "city": "Lahore",
                    "iata_code": "LHE",
                    "time_zone": "Asia/Karachi",
                    "country": "Pakistan"
                  },
                  "departure_datetime": "2023-08-15T15:00:00",
                  "arrival_datetime": "2023-08-15T16:45:00",
                  "duration_minutes": 105,
                  "flight_number": [
                    "ER-522"
                  ],
                  "operating_airline": {
                    "name": "Serene Air",
                    "code": "ER"
                  },
                  "marketing_airline": {
                    "name": "Serene Air",
                    "code": "ER"
                  },
                  "rbd": "LB",
                  "meta": {
                    "serene_rbd": "J",
                    "custom_rbd": "LB"
                  },
                  "cabin_class": "Economy",
                  "is_stop": false,
                  "seats_remaining": null
                }
              ],
              "operating_airline": {
                "name": "Serene Air",
                "code": "ER"
              },
              "is_refundable": true,
              "has_private_fare": false,
              "has_meal": true,
              "seats_remaining": null,
              "origin": "KHI",
              "destination": "LHE"
            }
          ],
          "position": 96,
          "rules": [
            255,
            548
          ],
          "hash": "4d929011713ecf21bada7e1b6104cf7cd4adc186",
          "hash_rbd": "2da9b72455c3d2b2df0f2faf44700294fe92dc57",
          "fare_options": [
            {
              "itinerary_id": "1DC707",
              "price": {
                "selling_fare": 18087,
                "published_fare": 15855.0,
                "gross_fare": 18000.0,
                "tax": 2145.0,
                "currency": "PKR",
                "breakdown": {
                  "adult": {
                    "base_fare": 15855.0,
                    "tax": 2145.0,
                    "total_fare": 18087,
                    "gross_fare": 18000.0
                  },
                  "child": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  },
                  "infant": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  }
                }
              },
              "related_itineraries": null,
              "hash_rbd": "2da9b72455c3d2b2df0f2faf44700294fe92dc57",
              "hash": "4d929011713ecf21bada7e1b6104cf7cd4adc186",
              "combo": false,
              "offers": [
                {
                  "text": "1 piece(s) of 20kg total",
                  "icon": "standard_baggage"
                }
              ],
              "rbd": "LB",
              "cabin_class": "Economy",
              "has_meal": true,
              "baggage_info": {
                "pieces": 1,
                "weight": 20.0,
                "unit": "KG",
                "max_weight_allowed_per_piece": null
              },
              "is_refundable": true,
              "addons": [
                {
                  "code": "ADDON_FC",
                  "name": "Free Cancellation",
                  "description": "Free Cancellation on this booking.",
                  "enabled": true,
                  "options": [
                    {
                      "id": "352C9C",
                      "cost": 750.0,
                      "description": "100% Refund Guarantee"
                    }
                  ],
                  "meta": {
                    "fc_premium_id": 10436965
                  }
                },
                {
                  "code": "ADDON_FDC",
                  "name": "Free Date Change",
                  "description": "Free Date Change on this booking.",
                  "enabled": true,
                  "options": [
                    {
                      "id": "FDF541",
                      "cost": 500.0,
                      "description": "Modify your trip anytime before your trip for free."
                    }
                  ],
                  "meta": {
                    "fdc_premium_id": 10436966
                  }
                }
              ]
            },
            {
              "itinerary_id": "0D3BF5",
              "price": {
                "selling_fare": 18837,
                "published_fare": 15855.0,
                "gross_fare": 18000.0,
                "tax": 2145.0,
                "currency": "PKR",
                "breakdown": {
                  "adult": {
                    "base_fare": 15855.0,
                    "tax": 2145.0,
                    "total_fare": 18837,
                    "gross_fare": 18000.0
                  },
                  "child": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  },
                  "infant": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  }
                }
              },
              "related_itineraries": null,
              "hash_rbd": "d5966bdd6082c6010ac34900a49864038202a741",
              "hash": "4d929011713ecf21bada7e1b6104cf7cd4adc186",
              "combo": false,
              "offers": [
                {
                  "text": "1 piece(s) of 20kg total",
                  "icon": "standard_baggage"
                },
                {
                  "text": "Sasta Refund: Get a full refund of PKR 18,087/-. <a href='https://sastaticket.pk/pages/terms-and-conditions#free_cancellation' target='_blank'>T&C apply</a>",
                  "icon": "free_cancellation"
                }
              ],
              "rbd": "ST-FC",
              "cabin_class": "Economy",
              "has_meal": true,
              "baggage_info": {
                "pieces": 1,
                "weight": 20.0,
                "unit": "KG",
                "max_weight_allowed_per_piece": null
              },
              "is_refundable": true,
              "addons": []
            },
            {
              "itinerary_id": "348237",
              "price": {
                "selling_fare": 19092,
                "published_fare": 16855.0,
                "gross_fare": 19000.0,
                "tax": 2145.0,
                "currency": "PKR",
                "breakdown": {
                  "adult": {
                    "base_fare": 16855.0,
                    "tax": 2145.0,
                    "total_fare": 19092,
                    "gross_fare": 19000.0
                  },
                  "child": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  },
                  "infant": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  }
                }
              },
              "related_itineraries": null,
              "hash_rbd": "5ff28aaca19769a97eec459ac2f08a1fe4a1e6a3",
              "hash": "4d929011713ecf21bada7e1b6104cf7cd4adc186",
              "combo": false,
              "offers": [
                {
                  "text": "2 piece(s) of 40kg total (maximum limit of 32kg in 1 piece)",
                  "icon": "two_piece_bags"
                }
              ],
              "rbd": "EB",
              "cabin_class": "Economy",
              "has_meal": true,
              "baggage_info": {
                "pieces": 2,
                "weight": 40.0,
                "unit": "KG",
                "max_weight_allowed_per_piece": 32.0
              },
              "is_refundable": true,
              "addons": [
                {
                  "code": "ADDON_FC",
                  "name": "Free Cancellation",
                  "description": "Free Cancellation on this booking.",
                  "enabled": true,
                  "options": [
                    {
                      "id": "084165",
                      "cost": 750.0,
                      "description": "100% Refund Guarantee"
                    }
                  ],
                  "meta": {
                    "fc_premium_id": 10436965
                  }
                },
                {
                  "code": "ADDON_FDC",
                  "name": "Free Date Change",
                  "description": "Free Date Change on this booking.",
                  "enabled": true,
                  "options": [
                    {
                      "id": "743353",
                      "cost": 500.0,
                      "description": "Modify your trip anytime before your trip for free."
                    }
                  ],
                  "meta": {
                    "fdc_premium_id": 10436966
                  }
                }
              ]
            },
            {
              "itinerary_id": "4A2E58",
              "price": {
                "selling_fare": 19842,
                "published_fare": 16855.0,
                "gross_fare": 19000.0,
                "tax": 2145.0,
                "currency": "PKR",
                "breakdown": {
                  "adult": {
                    "base_fare": 16855.0,
                    "tax": 2145.0,
                    "total_fare": 19842,
                    "gross_fare": 19000.0
                  },
                  "child": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  },
                  "infant": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  }
                }
              },
              "related_itineraries": null,
              "hash_rbd": "8bead693018968dfdcf8e53e316bfc1cb3c63c88",
              "hash": "4d929011713ecf21bada7e1b6104cf7cd4adc186",
              "combo": false,
              "offers": [
                {
                  "text": "2 piece(s) of 40kg total (maximum limit of 32kg in 1 piece)",
                  "icon": "two_piece_bags"
                },
                {
                  "text": "Sasta Refund: Get a full refund of PKR 19,092/-. <a href='https://sastaticket.pk/pages/terms-and-conditions#free_cancellation' target='_blank'>T&C apply</a>",
                  "icon": "free_cancellation"
                }
              ],
              "rbd": "ST-FC",
              "cabin_class": "Economy",
              "has_meal": true,
              "baggage_info": {
                "pieces": 2,
                "weight": 40.0,
                "unit": "KG",
                "max_weight_allowed_per_piece": 32.0
              },
              "is_refundable": true,
              "addons": []
            }
          ]
        },
        {
          "provider": "FLYJINNAH",
          "is_refundable": false,
          "should_auto_ticket": true,
          "baggage_info": {
            "pieces": 0,
            "weight": 0.0,
            "unit": "KG",
            "max_weight_allowed_per_piece": null
          },
          "legs": [
            {
              "cabin_class": "Economy",
              "segments": [
                {
                  "origin": {
                    "name": "Jinnah International Airport",
                    "airport": "Jinnah International Airport",
                    "city": "Karachi",
                    "iata_code": "KHI",
                    "time_zone": "Asia/Karachi",
                    "country": "Pakistan"
                  },
                  "destination": {
                    "name": "Allama Iqbal International Airport",
                    "airport": "Allama Iqbal International Airport",
                    "city": "Lahore",
                    "iata_code": "LHE",
                    "time_zone": "Asia/Karachi",
                    "country": "Pakistan"
                  },
                  "departure_datetime": "2023-08-15T12:45:00",
                  "arrival_datetime": "2023-08-15T14:25:00",
                  "duration_minutes": 100,
                  "flight_number": [
                    "9P-842"
                  ],
                  "operating_airline": {
                    "name": "Fly Jinnah",
                    "code": "9P"
                  },
                  "marketing_airline": {
                    "name": "Fly Jinnah",
                    "code": "9P"
                  },
                  "rbd": "AA_Basic",
                  "meta": {
                    "RPH": "9P$KHI/LHE$5274$20230815124500$20230815142500"
                  },
                  "cabin_class": "Economy",
                  "is_stop": false,
                  "seats_remaining": null
                }
              ],
              "operating_airline": {
                "name": "Fly Jinnah",
                "code": "9P"
              },
              "is_refundable": false,
              "has_private_fare": false,
              "has_meal": false,
              "seats_remaining": null,
              "origin": "KHI",
              "destination": "LHE"
            }
          ],
          "position": 97,
          "rules": [
            401,
            558
          ],
          "hash": "efe3430eade63b3a437e7c36366b1789b705b3a2",
          "hash_rbd": "04e7e8e942ca0dede99f0471b4c2c99d8954773f",
          "fare_options": [
            {
              "itinerary_id": "8133AC",
              "price": {
                "selling_fare": 15836,
                "published_fare": 12855.0,
                "gross_fare": 15000.0,
                "tax": 2145.0,
                "currency": "PKR",
                "breakdown": {
                  "adult": {
                    "base_fare": 12855.0,
                    "tax": 2145.0,
                    "total_fare": 15836,
                    "gross_fare": 15000.0
                  },
                  "child": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  },
                  "infant": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  }
                }
              },
              "related_itineraries": null,
              "hash_rbd": "04e7e8e942ca0dede99f0471b4c2c99d8954773f",
              "hash": "efe3430eade63b3a437e7c36366b1789b705b3a2",
              "combo": false,
              "offers": [
                {
                  "text": "No check-in baggage",
                  "icon": "no_baggage"
                },
                {
                  "text": "Baggage (Additional Charges)",
                  "icon": "standard_baggage"
                },
                {
                  "text": "Seat (Additional Charges)",
                  "icon": "seat"
                },
                {
                  "text": "Meal (Additional Charges)",
                  "icon": "meal"
                }
              ],
              "rbd": "AA_Basic",
              "cabin_class": "Economy",
              "has_meal": false,
              "baggage_info": {
                "pieces": 0,
                "weight": 0.0,
                "unit": "KG",
                "max_weight_allowed_per_piece": null
              },
              "is_refundable": false,
              "addons": []
            },
            {
              "itinerary_id": "086F4D",
              "price": {
                "selling_fare": 17434,
                "published_fare": 14355.0,
                "gross_fare": 16500.0,
                "tax": 2145.0,
                "currency": "PKR",
                "breakdown": {
                  "adult": {
                    "base_fare": 14355.0,
                    "tax": 2145.0,
                    "total_fare": 17434,
                    "gross_fare": 16500.0
                  },
                  "child": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  },
                  "infant": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  }
                }
              },
              "related_itineraries": null,
              "hash_rbd": "52aebc320a2b9d07038e2e8b77e92352524a26ce",
              "hash": "efe3430eade63b3a437e7c36366b1789b705b3a2",
              "combo": false,
              "offers": [
                {
                  "text": "23kg check-in baggage allowed",
                  "icon": "standard_baggage"
                },
                {
                  "text": "Meal: Sandwich and water",
                  "icon": "meal"
                },
                {
                  "text": "Seat: row 8 onwards",
                  "icon": "seat"
                },
                {
                  "text": "Modification: One modification, up to 8h",
                  "icon": "modification"
                },
                {
                  "text": "Cancellation: Up to 8h",
                  "icon": "cancellation"
                }
              ],
              "rbd": "AA_Value",
              "cabin_class": "Economy",
              "has_meal": true,
              "baggage_info": {
                "pieces": 0,
                "weight": 23.0,
                "unit": "KG",
                "max_weight_allowed_per_piece": null
              },
              "is_refundable": false,
              "addons": []
            },
            {
              "itinerary_id": "6C1CA3",
              "price": {
                "selling_fare": 18499,
                "published_fare": 15355.0,
                "gross_fare": 17500.0,
                "tax": 2145.0,
                "currency": "PKR",
                "breakdown": {
                  "adult": {
                    "base_fare": 15355.0,
                    "tax": 2145.0,
                    "total_fare": 18499,
                    "gross_fare": 17500.0
                  },
                  "child": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  },
                  "infant": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  }
                }
              },
              "related_itineraries": null,
              "hash_rbd": "878e1d3156439cadf4e5531179633c7683dd2c38",
              "hash": "efe3430eade63b3a437e7c36366b1789b705b3a2",
              "combo": false,
              "offers": [
                {
                  "text": "46kg total (maximum limit of 32kg in 1 piece)",
                  "icon": "standard_baggage"
                },
                {
                  "text": "Meal: Any Meal",
                  "icon": "meal"
                },
                {
                  "text": "Seat: Any Seat",
                  "icon": "seat"
                },
                {
                  "text": "Modification: One modification, up to 8h",
                  "icon": "modification"
                },
                {
                  "text": "Cancellation: Up to 8h",
                  "icon": "cancellation"
                }
              ],
              "rbd": "AA_Extra",
              "cabin_class": "Economy",
              "has_meal": true,
              "baggage_info": {
                "pieces": 0,
                "weight": 46.0,
                "unit": "KG",
                "max_weight_allowed_per_piece": null
              },
              "is_refundable": false,
              "addons": []
            }
          ]
        },
        {
          "provider": "FLYJINNAH",
          "is_refundable": false,
          "should_auto_ticket": true,
          "baggage_info": {
            "pieces": 0,
            "weight": 0.0,
            "unit": "KG",
            "max_weight_allowed_per_piece": null
          },
          "legs": [
            {
              "cabin_class": "Economy",
              "segments": [
                {
                  "origin": {
                    "name": "Jinnah International Airport",
                    "airport": "Jinnah International Airport",
                    "city": "Karachi",
                    "iata_code": "KHI",
                    "time_zone": "Asia/Karachi",
                    "country": "Pakistan"
                  },
                  "destination": {
                    "name": "Allama Iqbal International Airport",
                    "airport": "Allama Iqbal International Airport",
                    "city": "Lahore",
                    "iata_code": "LHE",
                    "time_zone": "Asia/Karachi",
                    "country": "Pakistan"
                  },
                  "departure_datetime": "2023-08-15T18:15:00",
                  "arrival_datetime": "2023-08-15T19:55:00",
                  "duration_minutes": 100,
                  "flight_number": [
                    "9P-846"
                  ],
                  "operating_airline": {
                    "name": "Fly Jinnah",
                    "code": "9P"
                  },
                  "marketing_airline": {
                    "name": "Fly Jinnah",
                    "code": "9P"
                  },
                  "rbd": "AA_Basic",
                  "meta": {
                    "RPH": "9P$KHI/LHE$2980$20230815181500$20230815195500"
                  },
                  "cabin_class": "Economy",
                  "is_stop": false,
                  "seats_remaining": null
                }
              ],
              "operating_airline": {
                "name": "Fly Jinnah",
                "code": "9P"
              },
              "is_refundable": false,
              "has_private_fare": false,
              "has_meal": false,
              "seats_remaining": null,
              "origin": "KHI",
              "destination": "LHE"
            }
          ],
          "position": 97,
          "rules": [
            401,
            558
          ],
          "hash": "13578e6b53b6c0a3009d997108753c2544a56630",
          "hash_rbd": "f845ae19ad52f5743fc7b3ec0c31f14cf4eb206c",
          "fare_options": [
            {
              "itinerary_id": "02EE51",
              "price": {
                "selling_fare": 15836,
                "published_fare": 12855.0,
                "gross_fare": 15000.0,
                "tax": 2145.0,
                "currency": "PKR",
                "breakdown": {
                  "adult": {
                    "base_fare": 12855.0,
                    "tax": 2145.0,
                    "total_fare": 15836,
                    "gross_fare": 15000.0
                  },
                  "child": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  },
                  "infant": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  }
                }
              },
              "related_itineraries": null,
              "hash_rbd": "f845ae19ad52f5743fc7b3ec0c31f14cf4eb206c",
              "hash": "13578e6b53b6c0a3009d997108753c2544a56630",
              "combo": false,
              "offers": [
                {
                  "text": "No check-in baggage",
                  "icon": "no_baggage"
                },
                {
                  "text": "Baggage (Additional Charges)",
                  "icon": "standard_baggage"
                },
                {
                  "text": "Seat (Additional Charges)",
                  "icon": "seat"
                },
                {
                  "text": "Meal (Additional Charges)",
                  "icon": "meal"
                }
              ],
              "rbd": "AA_Basic",
              "cabin_class": "Economy",
              "has_meal": false,
              "baggage_info": {
                "pieces": 0,
                "weight": 0.0,
                "unit": "KG",
                "max_weight_allowed_per_piece": null
              },
              "is_refundable": false,
              "addons": []
            },
            {
              "itinerary_id": "B9E0A3",
              "price": {
                "selling_fare": 17434,
                "published_fare": 14355.0,
                "gross_fare": 16500.0,
                "tax": 2145.0,
                "currency": "PKR",
                "breakdown": {
                  "adult": {
                    "base_fare": 14355.0,
                    "tax": 2145.0,
                    "total_fare": 17434,
                    "gross_fare": 16500.0
                  },
                  "child": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  },
                  "infant": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  }
                }
              },
              "related_itineraries": null,
              "hash_rbd": "6cb02f6266fcbdcc6b5eab58bfd073ba760ad6f5",
              "hash": "13578e6b53b6c0a3009d997108753c2544a56630",
              "combo": false,
              "offers": [
                {
                  "text": "23kg check-in baggage allowed",
                  "icon": "standard_baggage"
                },
                {
                  "text": "Meal: Sandwich and water",
                  "icon": "meal"
                },
                {
                  "text": "Seat: row 8 onwards",
                  "icon": "seat"
                },
                {
                  "text": "Modification: One modification, up to 8h",
                  "icon": "modification"
                },
                {
                  "text": "Cancellation: Up to 8h",
                  "icon": "cancellation"
                }
              ],
              "rbd": "AA_Value",
              "cabin_class": "Economy",
              "has_meal": true,
              "baggage_info": {
                "pieces": 0,
                "weight": 23.0,
                "unit": "KG",
                "max_weight_allowed_per_piece": null
              },
              "is_refundable": false,
              "addons": []
            },
            {
              "itinerary_id": "1D4C9E",
              "price": {
                "selling_fare": 18499,
                "published_fare": 15355.0,
                "gross_fare": 17500.0,
                "tax": 2145.0,
                "currency": "PKR",
                "breakdown": {
                  "adult": {
                    "base_fare": 15355.0,
                    "tax": 2145.0,
                    "total_fare": 18499,
                    "gross_fare": 17500.0
                  },
                  "child": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  },
                  "infant": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  }
                }
              },
              "related_itineraries": null,
              "hash_rbd": "b0ea41933222d9685c10660961d6db93827e31b1",
              "hash": "13578e6b53b6c0a3009d997108753c2544a56630",
              "combo": false,
              "offers": [
                {
                  "text": "46kg total (maximum limit of 32kg in 1 piece)",
                  "icon": "standard_baggage"
                },
                {
                  "text": "Meal: Any Meal",
                  "icon": "meal"
                },
                {
                  "text": "Seat: Any Seat",
                  "icon": "seat"
                },
                {
                  "text": "Modification: One modification, up to 8h",
                  "icon": "modification"
                },
                {
                  "text": "Cancellation: Up to 8h",
                  "icon": "cancellation"
                }
              ],
              "rbd": "AA_Extra",
              "cabin_class": "Economy",
              "has_meal": true,
              "baggage_info": {
                "pieces": 0,
                "weight": 46.0,
                "unit": "KG",
                "max_weight_allowed_per_piece": null
              },
              "is_refundable": false,
              "addons": []
            }
          ]
        },
        {
          "provider": "FLYJINNAH",
          "is_refundable": false,
          "should_auto_ticket": true,
          "baggage_info": {
            "pieces": 0,
            "weight": 0.0,
            "unit": "KG",
            "max_weight_allowed_per_piece": null
          },
          "legs": [
            {
              "cabin_class": "Economy",
              "segments": [
                {
                  "origin": {
                    "name": "Jinnah International Airport",
                    "airport": "Jinnah International Airport",
                    "city": "Karachi",
                    "iata_code": "KHI",
                    "time_zone": "Asia/Karachi",
                    "country": "Pakistan"
                  },
                  "destination": {
                    "name": "Allama Iqbal International Airport",
                    "airport": "Allama Iqbal International Airport",
                    "city": "Lahore",
                    "iata_code": "LHE",
                    "time_zone": "Asia/Karachi",
                    "country": "Pakistan"
                  },
                  "departure_datetime": "2023-08-15T07:30:00",
                  "arrival_datetime": "2023-08-15T09:10:00",
                  "duration_minutes": 100,
                  "flight_number": [
                    "9P-840"
                  ],
                  "operating_airline": {
                    "name": "Fly Jinnah",
                    "code": "9P"
                  },
                  "marketing_airline": {
                    "name": "Fly Jinnah",
                    "code": "9P"
                  },
                  "rbd": "AA_Basic",
                  "meta": {
                    "RPH": "9P$KHI/LHE$5057$20230815073000$20230815091000"
                  },
                  "cabin_class": "Economy",
                  "is_stop": false,
                  "seats_remaining": null
                }
              ],
              "operating_airline": {
                "name": "Fly Jinnah",
                "code": "9P"
              },
              "is_refundable": false,
              "has_private_fare": false,
              "has_meal": false,
              "seats_remaining": null,
              "origin": "KHI",
              "destination": "LHE"
            }
          ],
          "position": 97,
          "rules": [
            401,
            558
          ],
          "hash": "8ea158dac42e9580b3e08e759c92180ad46be570",
          "hash_rbd": "fddcd5f3b2d01ad64cd49d06ac2a1a7011fd2d2c",
          "fare_options": [
            {
              "itinerary_id": "62D84A",
              "price": {
                "selling_fare": 47257,
                "published_fare": 42355.0,
                "gross_fare": 44500.0,
                "tax": 2145.0,
                "currency": "PKR",
                "breakdown": {
                  "adult": {
                    "base_fare": 42355.0,
                    "tax": 2145.0,
                    "total_fare": 47257,
                    "gross_fare": 44500.0
                  },
                  "child": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  },
                  "infant": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  }
                }
              },
              "related_itineraries": null,
              "hash_rbd": "fddcd5f3b2d01ad64cd49d06ac2a1a7011fd2d2c",
              "hash": "8ea158dac42e9580b3e08e759c92180ad46be570",
              "combo": false,
              "offers": [
                {
                  "text": "No check-in baggage",
                  "icon": "no_baggage"
                },
                {
                  "text": "Baggage (Additional Charges)",
                  "icon": "standard_baggage"
                },
                {
                  "text": "Seat (Additional Charges)",
                  "icon": "seat"
                },
                {
                  "text": "Meal (Additional Charges)",
                  "icon": "meal"
                }
              ],
              "rbd": "AA_Basic",
              "cabin_class": "Economy",
              "has_meal": false,
              "baggage_info": {
                "pieces": 0,
                "weight": 0.0,
                "unit": "KG",
                "max_weight_allowed_per_piece": null
              },
              "is_refundable": false,
              "addons": []
            },
            {
              "itinerary_id": "DC68AB",
              "price": {
                "selling_fare": 49707,
                "published_fare": 44655.0,
                "gross_fare": 46800.0,
                "tax": 2145.0,
                "currency": "PKR",
                "breakdown": {
                  "adult": {
                    "base_fare": 44655.0,
                    "tax": 2145.0,
                    "total_fare": 49707,
                    "gross_fare": 46800.0
                  },
                  "child": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  },
                  "infant": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  }
                }
              },
              "related_itineraries": null,
              "hash_rbd": "702712b2f90135d9d2f0ba66b835cb4561befe54",
              "hash": "8ea158dac42e9580b3e08e759c92180ad46be570",
              "combo": false,
              "offers": [
                {
                  "text": "23kg check-in baggage allowed",
                  "icon": "standard_baggage"
                },
                {
                  "text": "Meal: Sandwich and water",
                  "icon": "meal"
                },
                {
                  "text": "Seat: row 8 onwards",
                  "icon": "seat"
                },
                {
                  "text": "Modification: One modification, up to 8h",
                  "icon": "modification"
                },
                {
                  "text": "Cancellation: Up to 8h",
                  "icon": "cancellation"
                }
              ],
              "rbd": "AA_Value",
              "cabin_class": "Economy",
              "has_meal": true,
              "baggage_info": {
                "pieces": 0,
                "weight": 23.0,
                "unit": "KG",
                "max_weight_allowed_per_piece": null
              },
              "is_refundable": false,
              "addons": []
            },
            {
              "itinerary_id": "C543DE",
              "price": {
                "selling_fare": 50452,
                "published_fare": 45355.0,
                "gross_fare": 47500.0,
                "tax": 2145.0,
                "currency": "PKR",
                "breakdown": {
                  "adult": {
                    "base_fare": 45355.0,
                    "tax": 2145.0,
                    "total_fare": 50452,
                    "gross_fare": 47500.0
                  },
                  "child": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  },
                  "infant": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  }
                }
              },
              "related_itineraries": null,
              "hash_rbd": "1d1a6030b28d1a1937f5526fb4468eca1b0b704c",
              "hash": "8ea158dac42e9580b3e08e759c92180ad46be570",
              "combo": false,
              "offers": [
                {
                  "text": "46kg total (maximum limit of 32kg in 1 piece)",
                  "icon": "standard_baggage"
                },
                {
                  "text": "Meal: Any Meal",
                  "icon": "meal"
                },
                {
                  "text": "Seat: Any Seat",
                  "icon": "seat"
                },
                {
                  "text": "Modification: One modification, up to 8h",
                  "icon": "modification"
                },
                {
                  "text": "Cancellation: Up to 8h",
                  "icon": "cancellation"
                }
              ],
              "rbd": "AA_Extra",
              "cabin_class": "Economy",
              "has_meal": true,
              "baggage_info": {
                "pieces": 0,
                "weight": 46.0,
                "unit": "KG",
                "max_weight_allowed_per_piece": null
              },
              "is_refundable": false,
              "addons": []
            }
          ]
        },
        {
          "provider": "PIAAPI",
          "is_refundable": true,
          "should_auto_ticket": true,
          "baggage_info": {
            "pieces": 0,
            "weight": 0.0,
            "unit": "KG",
            "max_weight_allowed_per_piece": null
          },
          "legs": [
            {
              "cabin_class": "Economy",
              "segments": [
                {
                  "origin": {
                    "name": "Jinnah International Airport",
                    "airport": "Jinnah International Airport",
                    "city": "Karachi",
                    "iata_code": "KHI",
                    "time_zone": "Asia/Karachi",
                    "country": "Pakistan"
                  },
                  "destination": {
                    "name": "Allama Iqbal International Airport",
                    "airport": "Allama Iqbal International Airport",
                    "city": "Lahore",
                    "iata_code": "LHE",
                    "time_zone": "Asia/Karachi",
                    "country": "Pakistan"
                  },
                  "departure_datetime": "2023-08-15T14:00:00",
                  "arrival_datetime": "2023-08-15T15:45:00",
                  "duration_minutes": 105,
                  "flight_number": [
                    "PK-304"
                  ],
                  "operating_airline": {
                    "name": "PIA",
                    "code": "PK"
                  },
                  "marketing_airline": {
                    "name": "PIA",
                    "code": "PK"
                  },
                  "rbd": "V",
                  "meta": {
                    "fare_group_name": "NILBAG",
                    "fare_ref_code": "VOWNIL",
                    "fare_ref_id": "1b52a273fb97b111305565dbe17681d53642bd9e7ba838789316998196567f2ef0bb631f7a1094e09919beb9ebf4a93072700f38a7f676d4741ba247682eb90ab956dd956370b8dbae62fb7858be8b1aebe230095d59d8940d3f35cac4ad724c",
                    "fare_ref_name": "VOWNIL",
                    "flight_segment_sequence": "1",
                    "res_book_design_code": "V",
                    "res_book_desig_quantity": "9",
                    "is_stop": false
                  },
                  "cabin_class": "Economy",
                  "is_stop": false,
                  "seats_remaining": 9
                }
              ],
              "operating_airline": {
                "name": "PIA",
                "code": "PK"
              },
              "is_refundable": true,
              "has_private_fare": false,
              "has_meal": true,
              "seats_remaining": 9,
              "origin": "KHI",
              "destination": "LHE"
            }
          ],
          "position": 98,
          "rules": [
            294,
            554
          ],
          "hash": "fc7a78269c548176816aa215cd8d2de3ad658c7d",
          "hash_rbd": "0a9b816da23ae93d7faa88398212ecdb7123da55",
          "fare_options": [
            {
              "itinerary_id": "4af3e010-bbb9-42ee-b8d5-f15bc70ea0a4#0",
              "price": {
                "selling_fare": 17578,
                "published_fare": 15290.0,
                "gross_fare": 17410.0,
                "tax": 2120.0,
                "currency": "PKR",
                "breakdown": {
                  "adult": {
                    "base_fare": 15290.0,
                    "tax": 2120.0,
                    "total_fare": 17578,
                    "gross_fare": 17410.0
                  },
                  "child": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  },
                  "infant": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  }
                }
              },
              "related_itineraries": null,
              "hash_rbd": "0a9b816da23ae93d7faa88398212ecdb7123da55",
              "hash": "fc7a78269c548176816aa215cd8d2de3ad658c7d",
              "combo": false,
              "offers": [
                {
                  "text": "No check in baggage",
                  "icon": "no_baggage"
                }
              ],
              "rbd": "V",
              "cabin_class": "Economy",
              "has_meal": true,
              "baggage_info": {
                "pieces": 0,
                "weight": 0.0,
                "unit": "KG",
                "max_weight_allowed_per_piece": null
              },
              "is_refundable": true,
              "addons": [
                {
                  "code": "ADDON_FC",
                  "name": "Free Cancellation",
                  "description": "Free Cancellation on this booking.",
                  "enabled": true,
                  "options": [
                    {
                      "id": "13B3CD",
                      "cost": 750.0,
                      "description": "100% Refund Guarantee"
                    }
                  ],
                  "meta": {
                    "fc_premium_id": 10436231
                  }
                },
                {
                  "code": "ADDON_FDC",
                  "name": "Free Date Change",
                  "description": "Free Date Change on this booking.",
                  "enabled": true,
                  "options": [
                    {
                      "id": "D8DAF9",
                      "cost": 500.0,
                      "description": "Modify your trip anytime before your trip for free."
                    }
                  ],
                  "meta": {
                    "fdc_premium_id": 10435738
                  }
                }
              ]
            },
            {
              "itinerary_id": "8B8139",
              "price": {
                "selling_fare": 18328,
                "published_fare": 15290.0,
                "gross_fare": 17410.0,
                "tax": 2120.0,
                "currency": "PKR",
                "breakdown": {
                  "adult": {
                    "base_fare": 15290.0,
                    "tax": 2120.0,
                    "total_fare": 18328,
                    "gross_fare": 17410.0
                  },
                  "child": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  },
                  "infant": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  }
                }
              },
              "related_itineraries": null,
              "hash_rbd": "c8352fd6e35524bfd2ed42470ab3b7ac7bec915f",
              "hash": "fc7a78269c548176816aa215cd8d2de3ad658c7d",
              "combo": false,
              "offers": [
                {
                  "text": "No check in baggage",
                  "icon": "no_baggage"
                },
                {
                  "text": "Sasta Refund: Get a full refund of PKR 17,578/-. <a href='https://sastaticket.pk/pages/terms-and-conditions#free_cancellation' target='_blank'>T&C apply</a>",
                  "icon": "free_cancellation"
                }
              ],
              "rbd": "ST-FC",
              "cabin_class": "Economy",
              "has_meal": true,
              "baggage_info": {
                "pieces": 0,
                "weight": 0.0,
                "unit": "KG",
                "max_weight_allowed_per_piece": null
              },
              "is_refundable": true,
              "addons": []
            },
            {
              "itinerary_id": "4af3e010-bbb9-42ee-b8d5-f15bc70ea0a4#1",
              "price": {
                "selling_fare": 18740,
                "published_fare": 16440.0,
                "gross_fare": 18560.0,
                "tax": 2120.0,
                "currency": "PKR",
                "breakdown": {
                  "adult": {
                    "base_fare": 16440.0,
                    "tax": 2120.0,
                    "total_fare": 18740,
                    "gross_fare": 18560.0
                  },
                  "child": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  },
                  "infant": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  }
                }
              },
              "related_itineraries": null,
              "hash_rbd": "07097b013661fb33ffd285cf2b56ae8a822e5471",
              "hash": "fc7a78269c548176816aa215cd8d2de3ad658c7d",
              "combo": false,
              "offers": [
                {
                  "text": "30kg check in baggage allowed",
                  "icon": "standard_baggage"
                }
              ],
              "rbd": "U",
              "cabin_class": "Economy",
              "has_meal": true,
              "baggage_info": {
                "pieces": 0,
                "weight": 30.0,
                "unit": "KG",
                "max_weight_allowed_per_piece": null
              },
              "is_refundable": true,
              "addons": [
                {
                  "code": "ADDON_FC",
                  "name": "Free Cancellation",
                  "description": "Free Cancellation on this booking.",
                  "enabled": true,
                  "options": [
                    {
                      "id": "C562EB",
                      "cost": 750.0,
                      "description": "100% Refund Guarantee"
                    }
                  ],
                  "meta": {
                    "fc_premium_id": 10436231
                  }
                },
                {
                  "code": "ADDON_FDC",
                  "name": "Free Date Change",
                  "description": "Free Date Change on this booking.",
                  "enabled": true,
                  "options": [
                    {
                      "id": "F3594B",
                      "cost": 500.0,
                      "description": "Modify your trip anytime before your trip for free."
                    }
                  ],
                  "meta": {
                    "fdc_premium_id": 10435738
                  }
                }
              ]
            },
            {
              "itinerary_id": "5124DF",
              "price": {
                "selling_fare": 19490,
                "published_fare": 16440.0,
                "gross_fare": 18560.0,
                "tax": 2120.0,
                "currency": "PKR",
                "breakdown": {
                  "adult": {
                    "base_fare": 16440.0,
                    "tax": 2120.0,
                    "total_fare": 19490,
                    "gross_fare": 18560.0
                  },
                  "child": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  },
                  "infant": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  }
                }
              },
              "related_itineraries": null,
              "hash_rbd": "b26508fd8664b46e9ff8c076ecd6046a2c2aa2bd",
              "hash": "fc7a78269c548176816aa215cd8d2de3ad658c7d",
              "combo": false,
              "offers": [
                {
                  "text": "30kg check in baggage allowed",
                  "icon": "standard_baggage"
                },
                {
                  "text": "Sasta Refund: Get a full refund of PKR 18,740/-. <a href='https://sastaticket.pk/pages/terms-and-conditions#free_cancellation' target='_blank'>T&C apply</a>",
                  "icon": "free_cancellation"
                }
              ],
              "rbd": "ST-FC",
              "cabin_class": "Economy",
              "has_meal": true,
              "baggage_info": {
                "pieces": 0,
                "weight": 30.0,
                "unit": "KG",
                "max_weight_allowed_per_piece": null
              },
              "is_refundable": true,
              "addons": []
            }
          ]
        },
        {
          "provider": "PIAAPI",
          "is_refundable": true,
          "should_auto_ticket": true,
          "baggage_info": {
            "pieces": 0,
            "weight": 0.0,
            "unit": "KG",
            "max_weight_allowed_per_piece": null
          },
          "legs": [
            {
              "cabin_class": "Economy",
              "segments": [
                {
                  "origin": {
                    "name": "Jinnah International Airport",
                    "airport": "Jinnah International Airport",
                    "city": "Karachi",
                    "iata_code": "KHI",
                    "time_zone": "Asia/Karachi",
                    "country": "Pakistan"
                  },
                  "destination": {
                    "name": "Allama Iqbal International Airport",
                    "airport": "Allama Iqbal International Airport",
                    "city": "Lahore",
                    "iata_code": "LHE",
                    "time_zone": "Asia/Karachi",
                    "country": "Pakistan"
                  },
                  "departure_datetime": "2023-08-15T21:30:00",
                  "arrival_datetime": "2023-08-15T23:15:00",
                  "duration_minutes": 105,
                  "flight_number": [
                    "PK-306"
                  ],
                  "operating_airline": {
                    "name": "PIA",
                    "code": "PK"
                  },
                  "marketing_airline": {
                    "name": "PIA",
                    "code": "PK"
                  },
                  "rbd": "V",
                  "meta": {
                    "fare_group_name": "NILBAG",
                    "fare_ref_code": "VOWNIL",
                    "fare_ref_id": "1b52a273fb97b111305565dbe17681d53642bd9e7ba838789316998196567f2edb5e44efdf67ae949f47644a1300abe6290d31090041aa30ebac2ea37d1b2de66e81523fde2b1f7d4a98cac379824e4329e195b4414f91fc8a3fb3d8ee5c761f",
                    "fare_ref_name": "VOWNIL",
                    "flight_segment_sequence": "1",
                    "res_book_design_code": "V",
                    "res_book_desig_quantity": "9",
                    "is_stop": false
                  },
                  "cabin_class": "Economy",
                  "is_stop": false,
                  "seats_remaining": 9
                }
              ],
              "operating_airline": {
                "name": "PIA",
                "code": "PK"
              },
              "is_refundable": true,
              "has_private_fare": false,
              "has_meal": true,
              "seats_remaining": 9,
              "origin": "KHI",
              "destination": "LHE"
            }
          ],
          "position": 98,
          "rules": [
            294,
            554
          ],
          "hash": "7d75cf25ff255d65ca900037180c90a4636b04cb",
          "hash_rbd": "8377760b6b12648f3aced0e59ca27d078dd2b113",
          "fare_options": [
            {
              "itinerary_id": "4af3e010-bbb9-42ee-b8d5-f15bc70ea0a4#2",
              "price": {
                "selling_fare": 17578,
                "published_fare": 15290.0,
                "gross_fare": 17410.0,
                "tax": 2120.0,
                "currency": "PKR",
                "breakdown": {
                  "adult": {
                    "base_fare": 15290.0,
                    "tax": 2120.0,
                    "total_fare": 17578,
                    "gross_fare": 17410.0
                  },
                  "child": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  },
                  "infant": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  }
                }
              },
              "related_itineraries": null,
              "hash_rbd": "8377760b6b12648f3aced0e59ca27d078dd2b113",
              "hash": "7d75cf25ff255d65ca900037180c90a4636b04cb",
              "combo": false,
              "offers": [
                {
                  "text": "No check in baggage",
                  "icon": "no_baggage"
                }
              ],
              "rbd": "V",
              "cabin_class": "Economy",
              "has_meal": true,
              "baggage_info": {
                "pieces": 0,
                "weight": 0.0,
                "unit": "KG",
                "max_weight_allowed_per_piece": null
              },
              "is_refundable": true,
              "addons": [
                {
                  "code": "ADDON_FC",
                  "name": "Free Cancellation",
                  "description": "Free Cancellation on this booking.",
                  "enabled": true,
                  "options": [
                    {
                      "id": "F7EA06",
                      "cost": 750.0,
                      "description": "100% Refund Guarantee"
                    }
                  ],
                  "meta": {
                    "fc_premium_id": 10436232
                  }
                },
                {
                  "code": "ADDON_FDC",
                  "name": "Free Date Change",
                  "description": "Free Date Change on this booking.",
                  "enabled": true,
                  "options": [
                    {
                      "id": "C42188",
                      "cost": 500.0,
                      "description": "Modify your trip anytime before your trip for free."
                    }
                  ],
                  "meta": {
                    "fdc_premium_id": 10435739
                  }
                }
              ]
            },
            {
              "itinerary_id": "83BD20",
              "price": {
                "selling_fare": 18328,
                "published_fare": 15290.0,
                "gross_fare": 17410.0,
                "tax": 2120.0,
                "currency": "PKR",
                "breakdown": {
                  "adult": {
                    "base_fare": 15290.0,
                    "tax": 2120.0,
                    "total_fare": 18328,
                    "gross_fare": 17410.0
                  },
                  "child": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  },
                  "infant": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  }
                }
              },
              "related_itineraries": null,
              "hash_rbd": "9bddb95c8ebb74023f66f16b750bed51a85c3557",
              "hash": "7d75cf25ff255d65ca900037180c90a4636b04cb",
              "combo": false,
              "offers": [
                {
                  "text": "No check in baggage",
                  "icon": "no_baggage"
                },
                {
                  "text": "Sasta Refund: Get a full refund of PKR 17,578/-. <a href='https://sastaticket.pk/pages/terms-and-conditions#free_cancellation' target='_blank'>T&C apply</a>",
                  "icon": "free_cancellation"
                }
              ],
              "rbd": "ST-FC",
              "cabin_class": "Economy",
              "has_meal": true,
              "baggage_info": {
                "pieces": 0,
                "weight": 0.0,
                "unit": "KG",
                "max_weight_allowed_per_piece": null
              },
              "is_refundable": true,
              "addons": []
            },
            {
              "itinerary_id": "4af3e010-bbb9-42ee-b8d5-f15bc70ea0a4#3",
              "price": {
                "selling_fare": 18740,
                "published_fare": 16440.0,
                "gross_fare": 18560.0,
                "tax": 2120.0,
                "currency": "PKR",
                "breakdown": {
                  "adult": {
                    "base_fare": 16440.0,
                    "tax": 2120.0,
                    "total_fare": 18740,
                    "gross_fare": 18560.0
                  },
                  "child": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  },
                  "infant": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  }
                }
              },
              "related_itineraries": null,
              "hash_rbd": "94794bf2c6839ef8a77defe4d78c98e4cba906d4",
              "hash": "7d75cf25ff255d65ca900037180c90a4636b04cb",
              "combo": false,
              "offers": [
                {
                  "text": "30kg check in baggage allowed",
                  "icon": "standard_baggage"
                }
              ],
              "rbd": "U",
              "cabin_class": "Economy",
              "has_meal": true,
              "baggage_info": {
                "pieces": 0,
                "weight": 30.0,
                "unit": "KG",
                "max_weight_allowed_per_piece": null
              },
              "is_refundable": true,
              "addons": [
                {
                  "code": "ADDON_FC",
                  "name": "Free Cancellation",
                  "description": "Free Cancellation on this booking.",
                  "enabled": true,
                  "options": [
                    {
                      "id": "FDAA96",
                      "cost": 750.0,
                      "description": "100% Refund Guarantee"
                    }
                  ],
                  "meta": {
                    "fc_premium_id": 10436232
                  }
                },
                {
                  "code": "ADDON_FDC",
                  "name": "Free Date Change",
                  "description": "Free Date Change on this booking.",
                  "enabled": true,
                  "options": [
                    {
                      "id": "EA7004",
                      "cost": 500.0,
                      "description": "Modify your trip anytime before your trip for free."
                    }
                  ],
                  "meta": {
                    "fdc_premium_id": 10435739
                  }
                }
              ]
            },
            {
              "itinerary_id": "6408EE",
              "price": {
                "selling_fare": 19490,
                "published_fare": 16440.0,
                "gross_fare": 18560.0,
                "tax": 2120.0,
                "currency": "PKR",
                "breakdown": {
                  "adult": {
                    "base_fare": 16440.0,
                    "tax": 2120.0,
                    "total_fare": 19490,
                    "gross_fare": 18560.0
                  },
                  "child": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  },
                  "infant": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  }
                }
              },
              "related_itineraries": null,
              "hash_rbd": "489f83d9ff1b8422215ceb82ea2557da05cf16db",
              "hash": "7d75cf25ff255d65ca900037180c90a4636b04cb",
              "combo": false,
              "offers": [
                {
                  "text": "30kg check in baggage allowed",
                  "icon": "standard_baggage"
                },
                {
                  "text": "Sasta Refund: Get a full refund of PKR 18,740/-. <a href='https://sastaticket.pk/pages/terms-and-conditions#free_cancellation' target='_blank'>T&C apply</a>",
                  "icon": "free_cancellation"
                }
              ],
              "rbd": "ST-FC",
              "cabin_class": "Economy",
              "has_meal": true,
              "baggage_info": {
                "pieces": 0,
                "weight": 30.0,
                "unit": "KG",
                "max_weight_allowed_per_piece": null
              },
              "is_refundable": true,
              "addons": []
            }
          ]
        },
        {
          "provider": "AIRBLUE",
          "is_refundable": true,
          "should_auto_ticket": true,
          "baggage_info": {
            "pieces": 1,
            "weight": 15.0,
            "unit": "KGS",
            "max_weight_allowed_per_piece": null
          },
          "legs": [
            {
              "cabin_class": "Economy",
              "segments": [
                {
                  "origin": {
                    "name": "Jinnah International Airport",
                    "airport": "Jinnah International Airport",
                    "city": "Karachi",
                    "iata_code": "KHI",
                    "time_zone": "Asia/Karachi",
                    "country": "Pakistan"
                  },
                  "destination": {
                    "name": "Allama Iqbal International Airport",
                    "airport": "Allama Iqbal International Airport",
                    "city": "Lahore",
                    "iata_code": "LHE",
                    "time_zone": "Asia/Karachi",
                    "country": "Pakistan"
                  },
                  "departure_datetime": "2023-08-15T12:00:00",
                  "arrival_datetime": "2023-08-15T13:50:00",
                  "duration_minutes": 110,
                  "flight_number": [
                    "PA-402"
                  ],
                  "operating_airline": {
                    "name": "Airblue",
                    "code": "PA"
                  },
                  "marketing_airline": {
                    "name": "Airblue",
                    "code": "PA"
                  },
                  "rbd": "value",
                  "meta": {},
                  "cabin_class": "Economy",
                  "is_stop": false,
                  "seats_remaining": null
                }
              ],
              "operating_airline": {
                "name": "Airblue",
                "code": "PA"
              },
              "is_refundable": true,
              "has_private_fare": false,
              "has_meal": true,
              "seats_remaining": null,
              "origin": "KHI",
              "destination": "LHE"
            }
          ],
          "position": 99,
          "rules": [
            223,
            561
          ],
          "hash": "a41718681f667480f90ec4f3728ceca3c8c8577c",
          "hash_rbd": "acc2a421d0a547348efd1737cfa8a2d2bb7beb5e",
          "fare_options": [
            {
              "itinerary_id": "DC8527",
              "price": {
                "selling_fare": 15822,
                "published_fare": 9345.0,
                "gross_fare": 15490.0,
                "tax": 6145.0,
                "currency": "PKR",
                "breakdown": {
                  "adult": {
                    "base_fare": 9345.0,
                    "tax": 6145.0,
                    "total_fare": 15822,
                    "gross_fare": 15490.0
                  },
                  "child": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  },
                  "infant": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  }
                }
              },
              "related_itineraries": null,
              "hash_rbd": "acc2a421d0a547348efd1737cfa8a2d2bb7beb5e",
              "hash": "a41718681f667480f90ec4f3728ceca3c8c8577c",
              "combo": false,
              "offers": [
                {
                  "text": "1 piece(s) of 15kgs total",
                  "icon": "standard_baggage"
                }
              ],
              "rbd": "value",
              "cabin_class": "Economy",
              "has_meal": true,
              "baggage_info": {
                "pieces": 1,
                "weight": 15.0,
                "unit": "KGS",
                "max_weight_allowed_per_piece": null
              },
              "is_refundable": true,
              "addons": [
                {
                  "code": "ADDON_FC",
                  "name": "Free Cancellation",
                  "description": "Free Cancellation on this booking.",
                  "enabled": true,
                  "options": [
                    {
                      "id": "4040F0",
                      "cost": 750.0,
                      "description": "100% Refund Guarantee"
                    }
                  ],
                  "meta": {
                    "fc_premium_id": 10435768
                  }
                },
                {
                  "code": "ADDON_FDC",
                  "name": "Free Date Change",
                  "description": "Free Date Change on this booking.",
                  "enabled": true,
                  "options": [
                    {
                      "id": "1A89EE",
                      "cost": 500.0,
                      "description": "Modify your trip anytime before your trip for free."
                    }
                  ],
                  "meta": {
                    "fdc_premium_id": 10436669
                  }
                }
              ]
            },
            {
              "itinerary_id": "3AE32F",
              "price": {
                "selling_fare": 16572,
                "published_fare": 9345.0,
                "gross_fare": 15490.0,
                "tax": 6145.0,
                "currency": "PKR",
                "breakdown": {
                  "adult": {
                    "base_fare": 9345.0,
                    "tax": 6145.0,
                    "total_fare": 16572,
                    "gross_fare": 15490.0
                  },
                  "child": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  },
                  "infant": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  }
                }
              },
              "related_itineraries": null,
              "hash_rbd": "2deb656c3998df34a25a3e3a898a1fd9ec8757cd",
              "hash": "a41718681f667480f90ec4f3728ceca3c8c8577c",
              "combo": false,
              "offers": [
                {
                  "text": "1 piece(s) of 15kgs total",
                  "icon": "standard_baggage"
                },
                {
                  "text": "Sasta Refund: Get a full refund of PKR 15,822/-. <a href='https://sastaticket.pk/pages/terms-and-conditions#free_cancellation' target='_blank'>T&C apply</a>",
                  "icon": "free_cancellation"
                }
              ],
              "rbd": "ST-FC",
              "cabin_class": "Economy",
              "has_meal": true,
              "baggage_info": {
                "pieces": 1,
                "weight": 15.0,
                "unit": "KGS",
                "max_weight_allowed_per_piece": null
              },
              "is_refundable": true,
              "addons": []
            },
            {
              "itinerary_id": "39FE2F",
              "price": {
                "selling_fare": 17075,
                "published_fare": 10555.0,
                "gross_fare": 16700.0,
                "tax": 6145.0,
                "currency": "PKR",
                "breakdown": {
                  "adult": {
                    "base_fare": 10555.0,
                    "tax": 6145.0,
                    "total_fare": 17075,
                    "gross_fare": 16700.0
                  },
                  "child": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  },
                  "infant": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  }
                }
              },
              "related_itineraries": null,
              "hash_rbd": "82b88c5467120481dff9388b97ae971d5b442eac",
              "hash": "a41718681f667480f90ec4f3728ceca3c8c8577c",
              "combo": false,
              "offers": [
                {
                  "text": "1 piece(s) of 20kgs total",
                  "icon": "standard_baggage"
                }
              ],
              "rbd": "flexi",
              "cabin_class": "Economy",
              "has_meal": true,
              "baggage_info": {
                "pieces": 1,
                "weight": 20.0,
                "unit": "KGS",
                "max_weight_allowed_per_piece": null
              },
              "is_refundable": true,
              "addons": [
                {
                  "code": "ADDON_FC",
                  "name": "Free Cancellation",
                  "description": "Free Cancellation on this booking.",
                  "enabled": true,
                  "options": [
                    {
                      "id": "74D2D6",
                      "cost": 750.0,
                      "description": "100% Refund Guarantee"
                    }
                  ],
                  "meta": {
                    "fc_premium_id": 10435768
                  }
                },
                {
                  "code": "ADDON_FDC",
                  "name": "Free Date Change",
                  "description": "Free Date Change on this booking.",
                  "enabled": true,
                  "options": [
                    {
                      "id": "097090",
                      "cost": 500.0,
                      "description": "Modify your trip anytime before your trip for free."
                    }
                  ],
                  "meta": {
                    "fdc_premium_id": 10436669
                  }
                }
              ]
            },
            {
              "itinerary_id": "7F86F5",
              "price": {
                "selling_fare": 17825,
                "published_fare": 10555.0,
                "gross_fare": 16700.0,
                "tax": 6145.0,
                "currency": "PKR",
                "breakdown": {
                  "adult": {
                    "base_fare": 10555.0,
                    "tax": 6145.0,
                    "total_fare": 17825,
                    "gross_fare": 16700.0
                  },
                  "child": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  },
                  "infant": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  }
                }
              },
              "related_itineraries": null,
              "hash_rbd": "84a54ccdf891d1c2dc5f20a5d9c5cfd682ae97bc",
              "hash": "a41718681f667480f90ec4f3728ceca3c8c8577c",
              "combo": false,
              "offers": [
                {
                  "text": "1 piece(s) of 20kgs total",
                  "icon": "standard_baggage"
                },
                {
                  "text": "Sasta Refund: Get a full refund of PKR 17,075/-. <a href='https://sastaticket.pk/pages/terms-and-conditions#free_cancellation' target='_blank'>T&C apply</a>",
                  "icon": "free_cancellation"
                }
              ],
              "rbd": "ST-FC",
              "cabin_class": "Economy",
              "has_meal": true,
              "baggage_info": {
                "pieces": 1,
                "weight": 20.0,
                "unit": "KGS",
                "max_weight_allowed_per_piece": null
              },
              "is_refundable": true,
              "addons": []
            },
            {
              "itinerary_id": "CFF63E",
              "price": {
                "selling_fare": 18779,
                "published_fare": 12200.0,
                "gross_fare": 18345.0,
                "tax": 6145.0,
                "currency": "PKR",
                "breakdown": {
                  "adult": {
                    "base_fare": 12200.0,
                    "tax": 6145.0,
                    "total_fare": 18779,
                    "gross_fare": 18345.0
                  },
                  "child": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  },
                  "infant": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  }
                }
              },
              "related_itineraries": null,
              "hash_rbd": "8b8f7b88c3f1b3f0ac1cde92b1b6db66945fca67",
              "hash": "a41718681f667480f90ec4f3728ceca3c8c8577c",
              "combo": false,
              "offers": [
                {
                  "text": "2 piece(s) of 40kgs total",
                  "icon": "two_piece_bags"
                }
              ],
              "rbd": "xtra",
              "cabin_class": "Economy",
              "has_meal": true,
              "baggage_info": {
                "pieces": 2,
                "weight": 40.0,
                "unit": "KGS",
                "max_weight_allowed_per_piece": null
              },
              "is_refundable": true,
              "addons": [
                {
                  "code": "ADDON_FC",
                  "name": "Free Cancellation",
                  "description": "Free Cancellation on this booking.",
                  "enabled": true,
                  "options": [
                    {
                      "id": "C009FF",
                      "cost": 750.0,
                      "description": "100% Refund Guarantee"
                    }
                  ],
                  "meta": {
                    "fc_premium_id": 10435768
                  }
                },
                {
                  "code": "ADDON_FDC",
                  "name": "Free Date Change",
                  "description": "Free Date Change on this booking.",
                  "enabled": true,
                  "options": [
                    {
                      "id": "935324",
                      "cost": 500.0,
                      "description": "Modify your trip anytime before your trip for free."
                    }
                  ],
                  "meta": {
                    "fdc_premium_id": 10436669
                  }
                }
              ]
            },
            {
              "itinerary_id": "ADB5BE",
              "price": {
                "selling_fare": 19529,
                "published_fare": 12200.0,
                "gross_fare": 18345.0,
                "tax": 6145.0,
                "currency": "PKR",
                "breakdown": {
                  "adult": {
                    "base_fare": 12200.0,
                    "tax": 6145.0,
                    "total_fare": 19529,
                    "gross_fare": 18345.0
                  },
                  "child": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  },
                  "infant": {
                    "base_fare": 0.0,
                    "tax": 0.0,
                    "total_fare": 0,
                    "gross_fare": 0.0
                  }
                }
              },
              "related_itineraries": null,
              "hash_rbd": "93fb6bd25e27b9a05dbf4051b511a517c285d769",
              "hash": "a41718681f667480f90ec4f3728ceca3c8c8577c",
              "combo": false,
              "offers": [
                {
                  "text": "2 piece(s) of 40kgs total",
                  "icon": "two_piece_bags"
                },
                {
                  "text": "Sasta Refund: Get a full refund of PKR 18,779/-. <a href='https://sastaticket.pk/pages/terms-and-conditions#free_cancellation' target='_blank'>T&C apply</a>",
                  "icon": "free_cancellation"
                }
              ],
              "rbd": "ST-FC",
              "cabin_class": "Economy",
              "has_meal": true,
              "baggage_info": {
                "pieces": 2,
                "weight": 40.0,
                "unit": "KGS",
                "max_weight_allowed_per_piece": null
              },
              "is_refundable": true,
              "addons": []
            }
          ]
        }
      ]
    ],
    "gaf_key": "BOOKING_KHI+LHE+2023-08-15_1_0_0_Y_ONEWAY_0::ds_main_pricing_experiment=2::_1692021457.8174546",
    "calendar_fares": [
      {
        "departure_date": "2023-08-14",
        "travel_duration": null,
        "airline_code": null,
        "selling_fare": null,
        "leg_index": 0,
        "provider": null
      },
      {
        "departure_date": "2023-08-15",
        "airline_code": "PK",
        "selling_fare": 17410.0,
        "leg_index": 0,
        "provider": "PIAAPI",
        "travel_duration": null
      },
      {
        "departure_date": "2023-08-16",
        "airline_code": "PK",
        "selling_fare": 17410.0,
        "leg_index": 0,
        "provider": "PIAAPI",
        "travel_duration": null
      },
      {
        "departure_date": "2023-08-17",
        "airline_code": "PK",
        "selling_fare": 17410.0,
        "leg_index": 0,
        "provider": "PIAAPI",
        "travel_duration": null
      },
      {
        "departure_date": "2023-08-18",
        "airline_code": "PK",
        "selling_fare": 17410.0,
        "leg_index": 0,
        "provider": "PIAAPI",
        "travel_duration": null
      },
      {
        "departure_date": "2023-08-19",
        "airline_code": "PK",
        "selling_fare": 22020.0,
        "leg_index": 0,
        "provider": "PIAAPI",
        "travel_duration": null
      },
      {
        "departure_date": "2023-08-20",
        "airline_code": "PK",
        "selling_fare": 17410.0,
        "leg_index": 0,
        "provider": "PIAAPI",
        "travel_duration": null
      }
    ],
    "calendar_poll": false,
    "transfers": {
      "legs": [
        {
          "id": "6c151fd9-c1ff-48f0-8e02-95168bdeddc5",
          "origin": {
            "airport": "Jinnah International Airport",
            "city": "Karachi",
            "iata_code": "KHI",
            "time_stamp": null,
            "time_zone": "Asia/Karachi"
          },
          "destination": {
            "airport": "Allama Iqbal International Airport",
            "city": "Lahore",
            "iata_code": "LHE",
            "time_stamp": null,
            "time_zone": "Asia/Karachi"
          },
          "date": "2023-08-15",
          "options": [
            {
              "start_address": null,
              "end_address": "Airport",
              "iata_code": "KHI",
              "is_to_airport": true,
              "fares": []
            },
            {
              "start_address": "Airport",
              "end_address": null,
              "iata_code": "LHE",
              "is_to_airport": false,
              "fares": []
            }
          ]
        }
      ]
    }
  }
}"""



# response_json = json.loads(response_data2)
# # print(response_json['data']['flights'][0][0]["provider"])



# def flight_data():
#     flights = response_json['data']['flights'][0]
#     # print(len(flights))
#     flight_details = ['sastaticket.pk']
#     for i in range(len(flights)):
#         flight_name=flights[i]['provider']
#         flight_timing_d = flights[i]['legs'][0]['segments'][0]["departure_datetime"]
#         flight_timing_a  = flights[i]['legs'][0]['segments'][0]["arrival_datetime"]
#         extract_time_d = helper.convert_to_12_hour_format(flight_timing_d)
#         extract_time_a = helper.convert_to_12_hour_format(flight_timing_a)
#         fare_actual =  flights[i]['fare_options'][0]['price']["gross_fare"]
#         fare_discounted =  flights[i]['fare_options'][0]['price']["selling_fare"]
#         if fare_discounted:
#             fare_discounted=fare_discounted
#         else: 
#             fare_discounted=None
        
#         flight_details.append({'flight_name':flight_name,'flight_timing':{'departure_timing':extract_time_d,'arrival_timing':extract_time_a,'fare':{'fare_actual':fare_actual,'fare_discounted':fare_discounted}},})
    
#     return flight_details

# flight_data()
# # Given timestamp



response_data_gozoyaan = """{
    "error": {
        "message": null,
        "code": null
    },
    "result": {
        "search_params": {
            "adult": 1,
            "child": 0,
            "infant": 0,
            "trips": [
                {
                    "origin": "KHI",
                    "destination": "ISB",
                    "preferred_time": "20-08-2023",
                    "origin_details": {
                        "name": "Jinnah International Airport",
                        "iata_code": "KHI",
                        "city": "Karachi",
                        "country": "Pakistan",
                        "code": "PK"
                    },
                    "destination_details": {
                        "name": "New Islamabad International Airport",
                        "iata_code": "ISB",
                        "city": "Islamabad",
                        "country": "Pakistan",
                        "code": "PK"
                    }
                }
            ],
            "child_age": [],
            "cabin_class": "Economy",
            "flight_type": "DOM",
            "currency_code": "PKR"
        },
        "id": "mYZyhuEpiYAW",
        "results": [
            {
                "id": 1332255043,
                "key": "TID$16921148571761548079-de2811191",
                "total_flight_time": 120,
                "total_base_price": "16518.55",
                "total_taxes": 2145.0,
                "total_price": "18663.55",
                "source_currency_code": "PKR",
                "refundable": true,
                "cancel_penalty": null,
                "change_penalty": null,
                "passengers": [
                    {
                        "code": "ADT",
                        "count": 1,
                        "total_base_price": "16518.55",
                        "total_taxes": 2145.0,
                        "total_price": "18663.55"
                    }
                ],
                "flights": [
                    {
                        "key": null,
                        "origin": "KHI",
                        "destination": "ISB",
                        "plating_carrier": {
                            "id": 412,
                            "code": "9P",
                            "name": "Fly Jinnah",
                            "logo": "https://storage.googleapis.com/gz-flight-prod-booking-data/carrier/logo/6dc9b713-a851-4356-a6e8-3671974999b1.png"
                        },
                        "options": [
                            {
                                "id": 2161367597,
                                "total_stop": 0,
                                "total_flight_time": 120,
                                "total_layover_time": 0,
                                "stoppage_location": [],
                                "stoppage_locations": null,
                                "departure_time": "2023-08-20 07:05:00",
                                "arrival_time": "2023-08-20 09:05:00",
                                "segments": [
                                    {
                                        "key": "9P$KHI/ISB$4287$20230820070500$20230820090500",
                                        "origin": "KHI",
                                        "destination": "ISB",
                                        "group": "",
                                        "departure_time": "2023-08-20 07:05:00",
                                        "arrival_time": "2023-08-20 09:05:00",
                                        "original_departure_time": "2023-08-20 07:05:00",
                                        "original_arrival_time": "2023-08-20 09:05:00",
                                        "original_departure_time_tz_data": null,
                                        "original_arrival_time_tz_data": null,
                                        "carrier": {
                                            "id": 412,
                                            "code": "9P",
                                            "name": "Fly Jinnah",
                                            "logo": "https://storage.googleapis.com/gz-flight-prod-booking-data/carrier/logo/6dc9b713-a851-4356-a6e8-3671974999b1.png"
                                        },
                                        "equipment": "320-200",
                                        "operating_carrier": null,
                                        "equipment_display_name": "Airbus 320-200",
                                        "e_ticket_ability": "",
                                        "link_availability": null,
                                        "polled_availability_option": null,
                                        "availability_source": null,
                                        "flight_number": "670",
                                        "flight_time": 120,
                                        "cabin_class": "Economy",
                                        "booking_code": "Basic",
                                        "booking_count": null,
                                        "baggage_allowance": [
                                            {
                                                "Type": "ADT",
                                                "CarryOn": true,
                                                "CheckIn": true,
                                                "Metrics": "Kg",
                                                "CarryOnBaggageWeight": 10,
                                                "CheckInBaggageWeight": 0,
                                                "CarryOnBaggageQuantity": 1,
                                                "CheckInBaggageQuantity": 0
                                            }
                                        ],
                                        "flight_details": {
                                            "flight_time": "PT2H0M0.000S",
                                            "origin_terminal": "TerminalX",
                                            "destination_terminal": ""
                                        },
                                        "origin_terminal": "TerminalX",
                                        "destination_terminal": null
                                    }
                                ]
                            }
                        ]
                    }
                ],
                "trip_type": "One Way",
                "converted_currency_code": "PKR",
                "total_layover_time": 0,
                "discount": null,
                "commission_percentage": "0"
            },
            {
                "id": 1332255044,
                "key": "TID$16921148571761548079-de2811191",
                "total_flight_time": 120,
                "total_base_price": "16518.55",
                "total_taxes": 2945.0,
                "total_price": "19463.55",
                "source_currency_code": "PKR",
                "refundable": true,
                "cancel_penalty": null,
                "change_penalty": null,
                "passengers": [
                    {
                        "code": "ADT",
                        "count": 1,
                        "total_base_price": "16518.55",
                        "total_taxes": 2945.0,
                        "total_price": "19463.55"
                    }
                ],
                "flights": [
                    {
                        "key": null,
                        "origin": "KHI",
                        "destination": "ISB",
                        "plating_carrier": {
                            "id": 412,
                            "code": "9P",
                            "name": "Fly Jinnah",
                            "logo": "https://storage.googleapis.com/gz-flight-prod-booking-data/carrier/logo/6dc9b713-a851-4356-a6e8-3671974999b1.png"
                        },
                        "options": [
                            {
                                "id": 2161367598,
                                "total_stop": 0,
                                "total_flight_time": 120,
                                "total_layover_time": 0,
                                "stoppage_location": [],
                                "stoppage_locations": null,
                                "departure_time": "2023-08-20 07:05:00",
                                "arrival_time": "2023-08-20 09:05:00",
                                "segments": [
                                    {
                                        "key": "9P$KHI/ISB$4287$20230820070500$20230820090500",
                                        "origin": "KHI",
                                        "destination": "ISB",
                                        "group": "",
                                        "departure_time": "2023-08-20 07:05:00",
                                        "arrival_time": "2023-08-20 09:05:00",
                                        "original_departure_time": "2023-08-20 07:05:00",
                                        "original_arrival_time": "2023-08-20 09:05:00",
                                        "original_departure_time_tz_data": null,
                                        "original_arrival_time_tz_data": null,
                                        "carrier": {
                                            "id": 412,
                                            "code": "9P",
                                            "name": "Fly Jinnah",
                                            "logo": "https://storage.googleapis.com/gz-flight-prod-booking-data/carrier/logo/6dc9b713-a851-4356-a6e8-3671974999b1.png"
                                        },
                                        "equipment": "320-200",
                                        "operating_carrier": null,
                                        "equipment_display_name": "Airbus 320-200",
                                        "e_ticket_ability": "",
                                        "link_availability": null,
                                        "polled_availability_option": null,
                                        "availability_source": null,
                                        "flight_number": "670",
                                        "flight_time": 120,
                                        "cabin_class": "Economy",
                                        "booking_code": "Basic",
                                        "booking_count": null,
                                        "baggage_allowance": [
                                            {
                                                "Type": "ADT",
                                                "CarryOn": true,
                                                "CheckIn": true,
                                                "Metrics": "Kg",
                                                "CarryOnBaggageWeight": 10,
                                                "CheckInBaggageWeight": "23",
                                                "CarryOnBaggageQuantity": 1,
                                                "CheckInBaggageQuantity": "1 "
                                            }
                                        ],
                                        "flight_details": {
                                            "flight_time": "PT2H0M0.000S",
                                            "origin_terminal": "TerminalX",
                                            "destination_terminal": ""
                                        },
                                        "origin_terminal": "TerminalX",
                                        "destination_terminal": null
                                    }
                                ]
                            }
                        ]
                    }
                ],
                "trip_type": "One Way",
                "converted_currency_code": "PKR",
                "total_layover_time": 0,
                "discount": null,
                "commission_percentage": "0"
            },
            {
                "id": 1332255045,
                "key": "TID$16921148571761548079-de2811191",
                "total_flight_time": 120,
                "total_base_price": "16518.55",
                "total_taxes": 3345.0,
                "total_price": "19863.55",
                "source_currency_code": "PKR",
                "refundable": true,
                "cancel_penalty": null,
                "change_penalty": null,
                "passengers": [
                    {
                        "code": "ADT",
                        "count": 1,
                        "total_base_price": "16518.55",
                        "total_taxes": 3345.0,
                        "total_price": "19863.55"
                    }
                ],
                "flights": [
                    {
                        "key": null,
                        "origin": "KHI",
                        "destination": "ISB",
                        "plating_carrier": {
                            "id": 412,
                            "code": "9P",
                            "name": "Fly Jinnah",
                            "logo": "https://storage.googleapis.com/gz-flight-prod-booking-data/carrier/logo/6dc9b713-a851-4356-a6e8-3671974999b1.png"
                        },
                        "options": [
                            {
                                "id": 2161367599,
                                "total_stop": 0,
                                "total_flight_time": 120,
                                "total_layover_time": 0,
                                "stoppage_location": [],
                                "stoppage_locations": null,
                                "departure_time": "2023-08-20 07:05:00",
                                "arrival_time": "2023-08-20 09:05:00",
                                "segments": [
                                    {
                                        "key": "9P$KHI/ISB$4287$20230820070500$20230820090500",
                                        "origin": "KHI",
                                        "destination": "ISB",
                                        "group": "",
                                        "departure_time": "2023-08-20 07:05:00",
                                        "arrival_time": "2023-08-20 09:05:00",
                                        "original_departure_time": "2023-08-20 07:05:00",
                                        "original_arrival_time": "2023-08-20 09:05:00",
                                        "original_departure_time_tz_data": null,
                                        "original_arrival_time_tz_data": null,
                                        "carrier": {
                                            "id": 412,
                                            "code": "9P",
                                            "name": "Fly Jinnah",
                                            "logo": "https://storage.googleapis.com/gz-flight-prod-booking-data/carrier/logo/6dc9b713-a851-4356-a6e8-3671974999b1.png"
                                        },
                                        "equipment": "320-200",
                                        "operating_carrier": null,
                                        "equipment_display_name": "Airbus 320-200",
                                        "e_ticket_ability": "",
                                        "link_availability": null,
                                        "polled_availability_option": null,
                                        "availability_source": null,
                                        "flight_number": "670",
                                        "flight_time": 120,
                                        "cabin_class": "Economy",
                                        "booking_code": "Basic",
                                        "booking_count": null,
                                        "baggage_allowance": [
                                            {
                                                "Type": "ADT",
                                                "CarryOn": true,
                                                "CheckIn": true,
                                                "Metrics": "Kg",
                                                "CarryOnBaggageWeight": 10,
                                                "CheckInBaggageWeight": "30",
                                                "CarryOnBaggageQuantity": 1,
                                                "CheckInBaggageQuantity": "2 "
                                            }
                                        ],
                                        "flight_details": {
                                            "flight_time": "PT2H0M0.000S",
                                            "origin_terminal": "TerminalX",
                                            "destination_terminal": ""
                                        },
                                        "origin_terminal": "TerminalX",
                                        "destination_terminal": null
                                    }
                                ]
                            }
                        ]
                    }
                ],
                "trip_type": "One Way",
                "converted_currency_code": "PKR",
                "total_layover_time": 0,
                "discount": null,
                "commission_percentage": "0"
            },
            {
                "id": 1332255047,
                "key": "TID$16921148571761548079-de2811191",
                "total_flight_time": 120,
                "total_base_price": "16518.55",
                "total_taxes": 3645.0,
                "total_price": "20163.55",
                "source_currency_code": "PKR",
                "refundable": true,
                "cancel_penalty": null,
                "change_penalty": null,
                "passengers": [
                    {
                        "code": "ADT",
                        "count": 1,
                        "total_base_price": "16518.55",
                        "total_taxes": 3645.0,
                        "total_price": "20163.55"
                    }
                ],
                "flights": [
                    {
                        "key": null,
                        "origin": "KHI",
                        "destination": "ISB",
                        "plating_carrier": {
                            "id": 412,
                            "code": "9P",
                            "name": "Fly Jinnah",
                            "logo": "https://storage.googleapis.com/gz-flight-prod-booking-data/carrier/logo/6dc9b713-a851-4356-a6e8-3671974999b1.png"
                        },
                        "options": [
                            {
                                "id": 2161367601,
                                "total_stop": 0,
                                "total_flight_time": 120,
                                "total_layover_time": 0,
                                "stoppage_location": [],
                                "stoppage_locations": null,
                                "departure_time": "2023-08-20 07:05:00",
                                "arrival_time": "2023-08-20 09:05:00",
                                "segments": [
                                    {
                                        "key": "9P$KHI/ISB$4287$20230820070500$20230820090500",
                                        "origin": "KHI",
                                        "destination": "ISB",
                                        "group": "",
                                        "departure_time": "2023-08-20 07:05:00",
                                        "arrival_time": "2023-08-20 09:05:00",
                                        "original_departure_time": "2023-08-20 07:05:00",
                                        "original_arrival_time": "2023-08-20 09:05:00",
                                        "original_departure_time_tz_data": null,
                                        "original_arrival_time_tz_data": null,
                                        "carrier": {
                                            "id": 412,
                                            "code": "9P",
                                            "name": "Fly Jinnah",
                                            "logo": "https://storage.googleapis.com/gz-flight-prod-booking-data/carrier/logo/6dc9b713-a851-4356-a6e8-3671974999b1.png"
                                        },
                                        "equipment": "320-200",
                                        "operating_carrier": null,
                                        "equipment_display_name": "Airbus 320-200",
                                        "e_ticket_ability": "",
                                        "link_availability": null,
                                        "polled_availability_option": null,
                                        "availability_source": null,
                                        "flight_number": "670",
                                        "flight_time": 120,
                                        "cabin_class": "Economy",
                                        "booking_code": "Basic",
                                        "booking_count": null,
                                        "baggage_allowance": [
                                            {
                                                "Type": "ADT",
                                                "CarryOn": true,
                                                "CheckIn": true,
                                                "Metrics": "Kg",
                                                "CarryOnBaggageWeight": 10,
                                                "CheckInBaggageWeight": "46",
                                                "CarryOnBaggageQuantity": 1,
                                                "CheckInBaggageQuantity": "2 "
                                            }
                                        ],
                                        "flight_details": {
                                            "flight_time": "PT2H0M0.000S",
                                            "origin_terminal": "TerminalX",
                                            "destination_terminal": ""
                                        },
                                        "origin_terminal": "TerminalX",
                                        "destination_terminal": null
                                    }
                                ]
                            }
                        ]
                    }
                ],
                "trip_type": "One Way",
                "converted_currency_code": "PKR",
                "total_layover_time": 0,
                "discount": null,
                "commission_percentage": "0"
            },
            {
                "id": 1332255053,
                "key": "TID$16921148571761548079-de2811191",
                "total_flight_time": 120,
                "total_base_price": "18033.55",
                "total_taxes": 2145.0,
                "total_price": "20178.55",
                "source_currency_code": "PKR",
                "refundable": true,
                "cancel_penalty": null,
                "change_penalty": null,
                "passengers": [
                    {
                        "code": "ADT",
                        "count": 1,
                        "total_base_price": "18033.55",
                        "total_taxes": 2145.0,
                        "total_price": "20178.55"
                    }
                ],
                "flights": [
                    {
                        "key": null,
                        "origin": "KHI",
                        "destination": "ISB",
                        "plating_carrier": {
                            "id": 412,
                            "code": "9P",
                            "name": "Fly Jinnah",
                            "logo": "https://storage.googleapis.com/gz-flight-prod-booking-data/carrier/logo/6dc9b713-a851-4356-a6e8-3671974999b1.png"
                        },
                        "options": [
                            {
                                "id": 2161367609,
                                "total_stop": 0,
                                "total_flight_time": 120,
                                "total_layover_time": 0,
                                "stoppage_location": [],
                                "stoppage_locations": null,
                                "departure_time": "2023-08-20 18:50:00",
                                "arrival_time": "2023-08-20 20:50:00",
                                "segments": [
                                    {
                                        "key": "9P$KHI/ISB$3636$20230820185000$20230820205000",
                                        "origin": "KHI",
                                        "destination": "ISB",
                                        "group": "",
                                        "departure_time": "2023-08-20 18:50:00",
                                        "arrival_time": "2023-08-20 20:50:00",
                                        "original_departure_time": "2023-08-20 18:50:00",
                                        "original_arrival_time": "2023-08-20 20:50:00",
                                        "original_departure_time_tz_data": null,
                                        "original_arrival_time_tz_data": null,
                                        "carrier": {
                                            "id": 412,
                                            "code": "9P",
                                            "name": "Fly Jinnah",
                                            "logo": "https://storage.googleapis.com/gz-flight-prod-booking-data/carrier/logo/6dc9b713-a851-4356-a6e8-3671974999b1.png"
                                        },
                                        "equipment": "320-200",
                                        "operating_carrier": null,
                                        "equipment_display_name": "Airbus 320-200",
                                        "e_ticket_ability": "",
                                        "link_availability": null,
                                        "polled_availability_option": null,
                                        "availability_source": null,
                                        "flight_number": "674",
                                        "flight_time": 120,
                                        "cabin_class": "Economy",
                                        "booking_code": "Basic",
                                        "booking_count": null,
                                        "baggage_allowance": [
                                            {
                                                "Type": "ADT",
                                                "CarryOn": true,
                                                "CheckIn": true,
                                                "Metrics": "Kg",
                                                "CarryOnBaggageWeight": 10,
                                                "CheckInBaggageWeight": 0,
                                                "CarryOnBaggageQuantity": 1,
                                                "CheckInBaggageQuantity": 0
                                            }
                                        ],
                                        "flight_details": {
                                            "flight_time": "PT2H0M0.000S",
                                            "origin_terminal": "TerminalX",
                                            "destination_terminal": ""
                                        },
                                        "origin_terminal": "TerminalX",
                                        "destination_terminal": null
                                    }
                                ]
                            }
                        ]
                    }
                ],
                "trip_type": "One Way",
                "converted_currency_code": "PKR",
                "total_layover_time": 0,
                "discount": null,
                "commission_percentage": "0"
            },
            {
                "id": 1332255055,
                "key": "TID$16921148571761548079-de2811191",
                "total_flight_time": 120,
                "total_base_price": "18033.55",
                "total_taxes": 3145.0,
                "total_price": "21178.55",
                "source_currency_code": "PKR",
                "refundable": true,
                "cancel_penalty": null,
                "change_penalty": null,
                "passengers": [
                    {
                        "code": "ADT",
                        "count": 1,
                        "total_base_price": "18033.55",
                        "total_taxes": 3145.0,
                        "total_price": "21178.55"
                    }
                ],
                "flights": [
                    {
                        "key": null,
                        "origin": "KHI",
                        "destination": "ISB",
                        "plating_carrier": {
                            "id": 412,
                            "code": "9P",
                            "name": "Fly Jinnah",
                            "logo": "https://storage.googleapis.com/gz-flight-prod-booking-data/carrier/logo/6dc9b713-a851-4356-a6e8-3671974999b1.png"
                        },
                        "options": [
                            {
                                "id": 2161367611,
                                "total_stop": 0,
                                "total_flight_time": 120,
                                "total_layover_time": 0,
                                "stoppage_location": [],
                                "stoppage_locations": null,
                                "departure_time": "2023-08-20 18:50:00",
                                "arrival_time": "2023-08-20 20:50:00",
                                "segments": [
                                    {
                                        "key": "9P$KHI/ISB$3636$20230820185000$20230820205000",
                                        "origin": "KHI",
                                        "destination": "ISB",
                                        "group": "",
                                        "departure_time": "2023-08-20 18:50:00",
                                        "arrival_time": "2023-08-20 20:50:00",
                                        "original_departure_time": "2023-08-20 18:50:00",
                                        "original_arrival_time": "2023-08-20 20:50:00",
                                        "original_departure_time_tz_data": null,
                                        "original_arrival_time_tz_data": null,
                                        "carrier": {
                                            "id": 412,
                                            "code": "9P",
                                            "name": "Fly Jinnah",
                                            "logo": "https://storage.googleapis.com/gz-flight-prod-booking-data/carrier/logo/6dc9b713-a851-4356-a6e8-3671974999b1.png"
                                        },
                                        "equipment": "320-200",
                                        "operating_carrier": null,
                                        "equipment_display_name": "Airbus 320-200",
                                        "e_ticket_ability": "",
                                        "link_availability": null,
                                        "polled_availability_option": null,
                                        "availability_source": null,
                                        "flight_number": "674",
                                        "flight_time": 120,
                                        "cabin_class": "Economy",
                                        "booking_code": "Basic",
                                        "booking_count": null,
                                        "baggage_allowance": [
                                            {
                                                "Type": "ADT",
                                                "CarryOn": true,
                                                "CheckIn": true,
                                                "Metrics": "Kg",
                                                "CarryOnBaggageWeight": 10,
                                                "CheckInBaggageWeight": "23",
                                                "CarryOnBaggageQuantity": 1,
                                                "CheckInBaggageQuantity": "1 "
                                            }
                                        ],
                                        "flight_details": {
                                            "flight_time": "PT2H0M0.000S",
                                            "origin_terminal": "TerminalX",
                                            "destination_terminal": ""
                                        },
                                        "origin_terminal": "TerminalX",
                                        "destination_terminal": null
                                    }
                                ]
                            }
                        ]
                    }
                ],
                "trip_type": "One Way",
                "converted_currency_code": "PKR",
                "total_layover_time": 0,
                "discount": null,
                "commission_percentage": "0"
            },
            {
                "id": 1332255057,
                "key": "TID$16921148571761548079-de2811191",
                "total_flight_time": 120,
                "total_base_price": "18033.55",
                "total_taxes": 3545.0,
                "total_price": "21578.55",
                "source_currency_code": "PKR",
                "refundable": true,
                "cancel_penalty": null,
                "change_penalty": null,
                "passengers": [
                    {
                        "code": "ADT",
                        "count": 1,
                        "total_base_price": "18033.55",
                        "total_taxes": 3545.0,
                        "total_price": "21578.55"
                    }
                ],
                "flights": [
                    {
                        "key": null,
                        "origin": "KHI",
                        "destination": "ISB",
                        "plating_carrier": {
                            "id": 412,
                            "code": "9P",
                            "name": "Fly Jinnah",
                            "logo": "https://storage.googleapis.com/gz-flight-prod-booking-data/carrier/logo/6dc9b713-a851-4356-a6e8-3671974999b1.png"
                        },
                        "options": [
                            {
                                "id": 2161367613,
                                "total_stop": 0,
                                "total_flight_time": 120,
                                "total_layover_time": 0,
                                "stoppage_location": [],
                                "stoppage_locations": null,
                                "departure_time": "2023-08-20 18:50:00",
                                "arrival_time": "2023-08-20 20:50:00",
                                "segments": [
                                    {
                                        "key": "9P$KHI/ISB$3636$20230820185000$20230820205000",
                                        "origin": "KHI",
                                        "destination": "ISB",
                                        "group": "",
                                        "departure_time": "2023-08-20 18:50:00",
                                        "arrival_time": "2023-08-20 20:50:00",
                                        "original_departure_time": "2023-08-20 18:50:00",
                                        "original_arrival_time": "2023-08-20 20:50:00",
                                        "original_departure_time_tz_data": null,
                                        "original_arrival_time_tz_data": null,
                                        "carrier": {
                                            "id": 412,
                                            "code": "9P",
                                            "name": "Fly Jinnah",
                                            "logo": "https://storage.googleapis.com/gz-flight-prod-booking-data/carrier/logo/6dc9b713-a851-4356-a6e8-3671974999b1.png"
                                        },
                                        "equipment": "320-200",
                                        "operating_carrier": null,
                                        "equipment_display_name": "Airbus 320-200",
                                        "e_ticket_ability": "",
                                        "link_availability": null,
                                        "polled_availability_option": null,
                                        "availability_source": null,
                                        "flight_number": "674",
                                        "flight_time": 120,
                                        "cabin_class": "Economy",
                                        "booking_code": "Basic",
                                        "booking_count": null,
                                        "baggage_allowance": [
                                            {
                                                "Type": "ADT",
                                                "CarryOn": true,
                                                "CheckIn": true,
                                                "Metrics": "Kg",
                                                "CarryOnBaggageWeight": 10,
                                                "CheckInBaggageWeight": "30",
                                                "CarryOnBaggageQuantity": 1,
                                                "CheckInBaggageQuantity": "2 "
                                            }
                                        ],
                                        "flight_details": {
                                            "flight_time": "PT2H0M0.000S",
                                            "origin_terminal": "TerminalX",
                                            "destination_terminal": ""
                                        },
                                        "origin_terminal": "TerminalX",
                                        "destination_terminal": null
                                    }
                                ]
                            }
                        ]
                    }
                ],
                "trip_type": "One Way",
                "converted_currency_code": "PKR",
                "total_layover_time": 0,
                "discount": null,
                "commission_percentage": "0"
            },
            {
                "id": 1332255058,
                "key": "TID$16921148571761548079-de2811191",
                "total_flight_time": 120,
                "total_base_price": "18033.55",
                "total_taxes": 3845.0,
                "total_price": "21878.55",
                "source_currency_code": "PKR",
                "refundable": true,
                "cancel_penalty": null,
                "change_penalty": null,
                "passengers": [
                    {
                        "code": "ADT",
                        "count": 1,
                        "total_base_price": "18033.55",
                        "total_taxes": 3845.0,
                        "total_price": "21878.55"
                    }
                ],
                "flights": [
                    {
                        "key": null,
                        "origin": "KHI",
                        "destination": "ISB",
                        "plating_carrier": {
                            "id": 412,
                            "code": "9P",
                            "name": "Fly Jinnah",
                            "logo": "https://storage.googleapis.com/gz-flight-prod-booking-data/carrier/logo/6dc9b713-a851-4356-a6e8-3671974999b1.png"
                        },
                        "options": [
                            {
                                "id": 2161367614,
                                "total_stop": 0,
                                "total_flight_time": 120,
                                "total_layover_time": 0,
                                "stoppage_location": [],
                                "stoppage_locations": null,
                                "departure_time": "2023-08-20 18:50:00",
                                "arrival_time": "2023-08-20 20:50:00",
                                "segments": [
                                    {
                                        "key": "9P$KHI/ISB$3636$20230820185000$20230820205000",
                                        "origin": "KHI",
                                        "destination": "ISB",
                                        "group": "",
                                        "departure_time": "2023-08-20 18:50:00",
                                        "arrival_time": "2023-08-20 20:50:00",
                                        "original_departure_time": "2023-08-20 18:50:00",
                                        "original_arrival_time": "2023-08-20 20:50:00",
                                        "original_departure_time_tz_data": null,
                                        "original_arrival_time_tz_data": null,
                                        "carrier": {
                                            "id": 412,
                                            "code": "9P",
                                            "name": "Fly Jinnah",
                                            "logo": "https://storage.googleapis.com/gz-flight-prod-booking-data/carrier/logo/6dc9b713-a851-4356-a6e8-3671974999b1.png"
                                        },
                                        "equipment": "320-200",
                                        "operating_carrier": null,
                                        "equipment_display_name": "Airbus 320-200",
                                        "e_ticket_ability": "",
                                        "link_availability": null,
                                        "polled_availability_option": null,
                                        "availability_source": null,
                                        "flight_number": "674",
                                        "flight_time": 120,
                                        "cabin_class": "Economy",
                                        "booking_code": "Basic",
                                        "booking_count": null,
                                        "baggage_allowance": [
                                            {
                                                "Type": "ADT",
                                                "CarryOn": true,
                                                "CheckIn": true,
                                                "Metrics": "Kg",
                                                "CarryOnBaggageWeight": 10,
                                                "CheckInBaggageWeight": "46",
                                                "CarryOnBaggageQuantity": 1,
                                                "CheckInBaggageQuantity": "2 "
                                            }
                                        ],
                                        "flight_details": {
                                            "flight_time": "PT2H0M0.000S",
                                            "origin_terminal": "TerminalX",
                                            "destination_terminal": ""
                                        },
                                        "origin_terminal": "TerminalX",
                                        "destination_terminal": null
                                    }
                                ]
                            }
                        ]
                    }
                ],
                "trip_type": "One Way",
                "converted_currency_code": "PKR",
                "total_layover_time": 0,
                "discount": null,
                "commission_percentage": "0"
            },
            {
                "id": 1332255049,
                "key": "TID$16921148571761548079-de2811191",
                "total_flight_time": 120,
                "total_base_price": "20053.55",
                "total_taxes": 2145.0,
                "total_price": "22198.55",
                "source_currency_code": "PKR",
                "refundable": true,
                "cancel_penalty": null,
                "change_penalty": null,
                "passengers": [
                    {
                        "code": "ADT",
                        "count": 1,
                        "total_base_price": "20053.55",
                        "total_taxes": 2145.0,
                        "total_price": "22198.55"
                    }
                ],
                "flights": [
                    {
                        "key": null,
                        "origin": "KHI",
                        "destination": "ISB",
                        "plating_carrier": {
                            "id": 412,
                            "code": "9P",
                            "name": "Fly Jinnah",
                            "logo": "https://storage.googleapis.com/gz-flight-prod-booking-data/carrier/logo/6dc9b713-a851-4356-a6e8-3671974999b1.png"
                        },
                        "options": [
                            {
                                "id": 2161367603,
                                "total_stop": 0,
                                "total_flight_time": 120,
                                "total_layover_time": 0,
                                "stoppage_location": [],
                                "stoppage_locations": null,
                                "departure_time": "2023-08-20 13:00:00",
                                "arrival_time": "2023-08-20 15:00:00",
                                "segments": [
                                    {
                                        "key": "9P$KHI/ISB$5806$20230820130000$20230820150000",
                                        "origin": "KHI",
                                        "destination": "ISB",
                                        "group": "",
                                        "departure_time": "2023-08-20 13:00:00",
                                        "arrival_time": "2023-08-20 15:00:00",
                                        "original_departure_time": "2023-08-20 13:00:00",
                                        "original_arrival_time": "2023-08-20 15:00:00",
                                        "original_departure_time_tz_data": null,
                                        "original_arrival_time_tz_data": null,
                                        "carrier": {
                                            "id": 412,
                                            "code": "9P",
                                            "name": "Fly Jinnah",
                                            "logo": "https://storage.googleapis.com/gz-flight-prod-booking-data/carrier/logo/6dc9b713-a851-4356-a6e8-3671974999b1.png"
                                        },
                                        "equipment": "320-200",
                                        "operating_carrier": null,
                                        "equipment_display_name": "Airbus 320-200",
                                        "e_ticket_ability": "",
                                        "link_availability": null,
                                        "polled_availability_option": null,
                                        "availability_source": null,
                                        "flight_number": "672",
                                        "flight_time": 120,
                                        "cabin_class": "Economy",
                                        "booking_code": "Basic",
                                        "booking_count": null,
                                        "baggage_allowance": [
                                            {
                                                "Type": "ADT",
                                                "CarryOn": true,
                                                "CheckIn": true,
                                                "Metrics": "Kg",
                                                "CarryOnBaggageWeight": 10,
                                                "CheckInBaggageWeight": 0,
                                                "CarryOnBaggageQuantity": 1,
                                                "CheckInBaggageQuantity": 0
                                            }
                                        ],
                                        "flight_details": {
                                            "flight_time": "PT2H0M0.000S",
                                            "origin_terminal": "TerminalX",
                                            "destination_terminal": ""
                                        },
                                        "origin_terminal": "TerminalX",
                                        "destination_terminal": null
                                    }
                                ]
                            }
                        ]
                    }
                ],
                "trip_type": "One Way",
                "converted_currency_code": "PKR",
                "total_layover_time": 0,
                "discount": null,
                "commission_percentage": "0"
            },
            {
                "id": 1332255050,
                "key": "TID$16921148571761548079-de2811191",
                "total_flight_time": 120,
                "total_base_price": "20053.55",
                "total_taxes": 3145.0,
                "total_price": "23198.55",
                "source_currency_code": "PKR",
                "refundable": true,
                "cancel_penalty": null,
                "change_penalty": null,
                "passengers": [
                    {
                        "code": "ADT",
                        "count": 1,
                        "total_base_price": "20053.55",
                        "total_taxes": 3145.0,
                        "total_price": "23198.55"
                    }
                ],
                "flights": [
                    {
                        "key": null,
                        "origin": "KHI",
                        "destination": "ISB",
                        "plating_carrier": {
                            "id": 412,
                            "code": "9P",
                            "name": "Fly Jinnah",
                            "logo": "https://storage.googleapis.com/gz-flight-prod-booking-data/carrier/logo/6dc9b713-a851-4356-a6e8-3671974999b1.png"
                        },
                        "options": [
                            {
                                "id": 2161367604,
                                "total_stop": 0,
                                "total_flight_time": 120,
                                "total_layover_time": 0,
                                "stoppage_location": [],
                                "stoppage_locations": null,
                                "departure_time": "2023-08-20 13:00:00",
                                "arrival_time": "2023-08-20 15:00:00",
                                "segments": [
                                    {
                                        "key": "9P$KHI/ISB$5806$20230820130000$20230820150000",
                                        "origin": "KHI",
                                        "destination": "ISB",
                                        "group": "",
                                        "departure_time": "2023-08-20 13:00:00",
                                        "arrival_time": "2023-08-20 15:00:00",
                                        "original_departure_time": "2023-08-20 13:00:00",
                                        "original_arrival_time": "2023-08-20 15:00:00",
                                        "original_departure_time_tz_data": null,
                                        "original_arrival_time_tz_data": null,
                                        "carrier": {
                                            "id": 412,
                                            "code": "9P",
                                            "name": "Fly Jinnah",
                                            "logo": "https://storage.googleapis.com/gz-flight-prod-booking-data/carrier/logo/6dc9b713-a851-4356-a6e8-3671974999b1.png"
                                        },
                                        "equipment": "320-200",
                                        "operating_carrier": null,
                                        "equipment_display_name": "Airbus 320-200",
                                        "e_ticket_ability": "",
                                        "link_availability": null,
                                        "polled_availability_option": null,
                                        "availability_source": null,
                                        "flight_number": "672",
                                        "flight_time": 120,
                                        "cabin_class": "Economy",
                                        "booking_code": "Basic",
                                        "booking_count": null,
                                        "baggage_allowance": [
                                            {
                                                "Type": "ADT",
                                                "CarryOn": true,
                                                "CheckIn": true,
                                                "Metrics": "Kg",
                                                "CarryOnBaggageWeight": 10,
                                                "CheckInBaggageWeight": "23",
                                                "CarryOnBaggageQuantity": 1,
                                                "CheckInBaggageQuantity": "1 "
                                            }
                                        ],
                                        "flight_details": {
                                            "flight_time": "PT2H0M0.000S",
                                            "origin_terminal": "TerminalX",
                                            "destination_terminal": ""
                                        },
                                        "origin_terminal": "TerminalX",
                                        "destination_terminal": null
                                    }
                                ]
                            }
                        ]
                    }
                ],
                "trip_type": "One Way",
                "converted_currency_code": "PKR",
                "total_layover_time": 0,
                "discount": null,
                "commission_percentage": "0"
            },
            {
                "id": 1332255051,
                "key": "TID$16921148571761548079-de2811191",
                "total_flight_time": 120,
                "total_base_price": "20053.55",
                "total_taxes": 3545.0,
                "total_price": "23598.55",
                "source_currency_code": "PKR",
                "refundable": true,
                "cancel_penalty": null,
                "change_penalty": null,
                "passengers": [
                    {
                        "code": "ADT",
                        "count": 1,
                        "total_base_price": "20053.55",
                        "total_taxes": 3545.0,
                        "total_price": "23598.55"
                    }
                ],
                "flights": [
                    {
                        "key": null,
                        "origin": "KHI",
                        "destination": "ISB",
                        "plating_carrier": {
                            "id": 412,
                            "code": "9P",
                            "name": "Fly Jinnah",
                            "logo": "https://storage.googleapis.com/gz-flight-prod-booking-data/carrier/logo/6dc9b713-a851-4356-a6e8-3671974999b1.png"
                        },
                        "options": [
                            {
                                "id": 2161367606,
                                "total_stop": 0,
                                "total_flight_time": 120,
                                "total_layover_time": 0,
                                "stoppage_location": [],
                                "stoppage_locations": null,
                                "departure_time": "2023-08-20 13:00:00",
                                "arrival_time": "2023-08-20 15:00:00",
                                "segments": [
                                    {
                                        "key": "9P$KHI/ISB$5806$20230820130000$20230820150000",
                                        "origin": "KHI",
                                        "destination": "ISB",
                                        "group": "",
                                        "departure_time": "2023-08-20 13:00:00",
                                        "arrival_time": "2023-08-20 15:00:00",
                                        "original_departure_time": "2023-08-20 13:00:00",
                                        "original_arrival_time": "2023-08-20 15:00:00",
                                        "original_departure_time_tz_data": null,
                                        "original_arrival_time_tz_data": null,
                                        "carrier": {
                                            "id": 412,
                                            "code": "9P",
                                            "name": "Fly Jinnah",
                                            "logo": "https://storage.googleapis.com/gz-flight-prod-booking-data/carrier/logo/6dc9b713-a851-4356-a6e8-3671974999b1.png"
                                        },
                                        "equipment": "320-200",
                                        "operating_carrier": null,
                                        "equipment_display_name": "Airbus 320-200",
                                        "e_ticket_ability": "",
                                        "link_availability": null,
                                        "polled_availability_option": null,
                                        "availability_source": null,
                                        "flight_number": "672",
                                        "flight_time": 120,
                                        "cabin_class": "Economy",
                                        "booking_code": "Basic",
                                        "booking_count": null,
                                        "baggage_allowance": [
                                            {
                                                "Type": "ADT",
                                                "CarryOn": true,
                                                "CheckIn": true,
                                                "Metrics": "Kg",
                                                "CarryOnBaggageWeight": 10,
                                                "CheckInBaggageWeight": "30",
                                                "CarryOnBaggageQuantity": 1,
                                                "CheckInBaggageQuantity": "2 "
                                            }
                                        ],
                                        "flight_details": {
                                            "flight_time": "PT2H0M0.000S",
                                            "origin_terminal": "TerminalX",
                                            "destination_terminal": ""
                                        },
                                        "origin_terminal": "TerminalX",
                                        "destination_terminal": null
                                    }
                                ]
                            }
                        ]
                    }
                ],
                "trip_type": "One Way",
                "converted_currency_code": "PKR",
                "total_layover_time": 0,
                "discount": null,
                "commission_percentage": "0"
            },
            {
                "id": 1332255052,
                "key": "TID$16921148571761548079-de2811191",
                "total_flight_time": 120,
                "total_base_price": "20053.55",
                "total_taxes": 3845.0,
                "total_price": "23898.55",
                "source_currency_code": "PKR",
                "refundable": true,
                "cancel_penalty": null,
                "change_penalty": null,
                "passengers": [
                    {
                        "code": "ADT",
                        "count": 1,
                        "total_base_price": "20053.55",
                        "total_taxes": 3845.0,
                        "total_price": "23898.55"
                    }
                ],
                "flights": [
                    {
                        "key": null,
                        "origin": "KHI",
                        "destination": "ISB",
                        "plating_carrier": {
                            "id": 412,
                            "code": "9P",
                            "name": "Fly Jinnah",
                            "logo": "https://storage.googleapis.com/gz-flight-prod-booking-data/carrier/logo/6dc9b713-a851-4356-a6e8-3671974999b1.png"
                        },
                        "options": [
                            {
                                "id": 2161367608,
                                "total_stop": 0,
                                "total_flight_time": 120,
                                "total_layover_time": 0,
                                "stoppage_location": [],
                                "stoppage_locations": null,
                                "departure_time": "2023-08-20 13:00:00",
                                "arrival_time": "2023-08-20 15:00:00",
                                "segments": [
                                    {
                                        "key": "9P$KHI/ISB$5806$20230820130000$20230820150000",
                                        "origin": "KHI",
                                        "destination": "ISB",
                                        "group": "",
                                        "departure_time": "2023-08-20 13:00:00",
                                        "arrival_time": "2023-08-20 15:00:00",
                                        "original_departure_time": "2023-08-20 13:00:00",
                                        "original_arrival_time": "2023-08-20 15:00:00",
                                        "original_departure_time_tz_data": null,
                                        "original_arrival_time_tz_data": null,
                                        "carrier": {
                                            "id": 412,
                                            "code": "9P",
                                            "name": "Fly Jinnah",
                                            "logo": "https://storage.googleapis.com/gz-flight-prod-booking-data/carrier/logo/6dc9b713-a851-4356-a6e8-3671974999b1.png"
                                        },
                                        "equipment": "320-200",
                                        "operating_carrier": null,
                                        "equipment_display_name": "Airbus 320-200",
                                        "e_ticket_ability": "",
                                        "link_availability": null,
                                        "polled_availability_option": null,
                                        "availability_source": null,
                                        "flight_number": "672",
                                        "flight_time": 120,
                                        "cabin_class": "Economy",
                                        "booking_code": "Basic",
                                        "booking_count": null,
                                        "baggage_allowance": [
                                            {
                                                "Type": "ADT",
                                                "CarryOn": true,
                                                "CheckIn": true,
                                                "Metrics": "Kg",
                                                "CarryOnBaggageWeight": 10,
                                                "CheckInBaggageWeight": "46",
                                                "CarryOnBaggageQuantity": 1,
                                                "CheckInBaggageQuantity": "2 "
                                            }
                                        ],
                                        "flight_details": {
                                            "flight_time": "PT2H0M0.000S",
                                            "origin_terminal": "TerminalX",
                                            "destination_terminal": ""
                                        },
                                        "origin_terminal": "TerminalX",
                                        "destination_terminal": null
                                    }
                                ]
                            }
                        ]
                    }
                ],
                "trip_type": "One Way",
                "converted_currency_code": "PKR",
                "total_layover_time": 0,
                "discount": null,
                "commission_percentage": "0"
            }
        ],
        "trip_type": "One Way",
        "created_at": "2023-08-15 21:54:16",
        "progress": 3,
        "status": "PROCESSING",
        "expected_progress": 4,
        "server_now": "2023-08-15 15:54:24.936938+00:00",
        "search_ttl": "2023-08-15 15:54:56.359690+00:00",
        "filter_queries": {
            "airlines": {
                "1332255043": "9P",
                "1332255044": "9P",
                "1332255045": "9P",
                "1332255047": "9P",
                "1332255053": "9P",
                "1332255055": "9P",
                "1332255057": "9P",
                "1332255058": "9P",
                "1332255049": "9P",
                "1332255050": "9P",
                "1332255051": "9P",
                "1332255052": "9P"
            },
            "onward_departure": {
                "1332255043": 1,
                "1332255044": 1,
                "1332255045": 1,
                "1332255047": 1,
                "1332255053": 3,
                "1332255055": 3,
                "1332255057": 3,
                "1332255058": 3,
                "1332255049": 2,
                "1332255050": 2,
                "1332255051": 2,
                "1332255052": 2
            },
            "return_departure": {},
            "layover_airport": {
                "1332255043": [],
                "1332255044": [],
                "1332255045": [],
                "1332255047": [],
                "1332255053": [],
                "1332255055": [],
                "1332255057": [],
                "1332255058": [],
                "1332255049": [],
                "1332255050": [],
                "1332255051": [],
                "1332255052": []
            },
            "aircraft": {
                "1332255043": [
                    "320-200"
                ],
                "1332255044": [
                    "320-200"
                ],
                "1332255045": [
                    "320-200"
                ],
                "1332255047": [
                    "320-200"
                ],
                "1332255053": [
                    "320-200"
                ],
                "1332255055": [
                    "320-200"
                ],
                "1332255057": [
                    "320-200"
                ],
                "1332255058": [
                    "320-200"
                ],
                "1332255049": [
                    "320-200"
                ],
                "1332255050": [
                    "320-200"
                ],
                "1332255051": [
                    "320-200"
                ],
                "1332255052": [
                    "320-200"
                ]
            },
            "layover_time": {
                "1332255043": [
                    0
                ],
                "1332255044": [
                    0
                ],
                "1332255045": [
                    0
                ],
                "1332255047": [
                    0
                ],
                "1332255053": [
                    0
                ],
                "1332255055": [
                    0
                ],
                "1332255057": [
                    0
                ],
                "1332255058": [
                    0
                ],
                "1332255049": [
                    0
                ],
                "1332255050": [
                    0
                ],
                "1332255051": [
                    0
                ],
                "1332255052": [
                    0
                ]
            },
            "stoppages": {
                "1332255043": [
                    0
                ],
                "1332255044": [
                    0
                ],
                "1332255045": [
                    0
                ],
                "1332255047": [
                    0
                ],
                "1332255053": [
                    0
                ],
                "1332255055": [
                    0
                ],
                "1332255057": [
                    0
                ],
                "1332255058": [
                    0
                ],
                "1332255049": [
                    0
                ],
                "1332255050": [
                    0
                ],
                "1332255051": [
                    0
                ],
                "1332255052": [
                    0
                ]
            }
        },
        "filter_params": {
            "order_by": [
                "total_price"
            ],
            "stops": [
                0,
                1,
                2
            ],
            "price_range": {
                "min": 17295.0,
                "max": 60240.0
            },
            "aircraft": [
                "320",
                "320-200",
                "32A",
                "A320",
                "ATR"
            ],
            "airlines": [
                {
                    "id": 412,
                    "code": "9P",
                    "logo": "carrier/logo/6dc9b713-a851-4356-a6e8-3671974999b1.png",
                    "name": "Fly Jinnah"
                },
                {
                    "id": 346,
                    "code": "PA",
                    "logo": "carrier/logo/1b71e17e-6675-4935-893f-2887dd32854e.png",
                    "name": "Air Blue"
                },
                {
                    "id": 126,
                    "code": "PK",
                    "logo": "carrier/logo/a0c4b6ea-aecb-4c48-baab-e888784ed380.png",
                    "name": "Pakistan International Airlines"
                }
            ],
            "layover_airport": [
                {
                    "iata_code": "LHE",
                    "name": "Alama Iqbal International Airport"
                },
                {
                    "iata_code": "SKZ",
                    "name": "Sukkur Airport"
                },
                {
                    "iata_code": "UET",
                    "name": "Quetta International Airport"
                }
            ]
        }
    },
    "status": true
}"""

to_json  = json.loads(response_data_gozoyaan)

# print(to_json)


# def flight_details_goZayaan():
#     result = to_json['result']['results']
#     flight_details= ['GoZayaan']
#     for i in range(len(result)):
#         flight_name = result[i]['flights'][0]['plating_carrier']['name']
#         flight_timing_d = result[i]['flights'][0]['options'][0]['departure_time']
#         flight_timing_a = result[i]['flights'][0]['options'][0]['arrival_time']
#         extract_time_d = helper.convert_to_12_hour_format_for_zayaan(flight_timing_d)
#         extract_time_a = helper.convert_to_12_hour_format_for_zayaan(flight_timing_a)
#         fare_actual = result[i]['total_price']
#         fare_discount = result[i]['discount']
#         if fare_discount:
#           fare_discount = fare_discount
#         else:
#           fare_discount= None
        
#         flight_details.append({'flight_name':flight_name,'flight_timing':{'departure_timing':extract_time_d,'arrival_timing':extract_time_a,'fare':{'fare_actual':fare_actual,'fare_discounted':fare_discount}},})
        
#     return flight_details
#     # print(flights)

# print(flight_details_goZayaan())


