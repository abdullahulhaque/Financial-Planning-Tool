federal_tax_brackets = {
    'SINGLE': [
        (0, 11600, 0.10),
        (11601, 47150, 0.12),
        (47151, 100525, 0.22),
        (100526, 191950, 0.24),
        (191951, 243725, 0.32),
        (243726, 609350, 0.35),
        (609351, float('inf'), 0.37)
    ],
    'MARRIED FILING JOINTLY': [
        (0, 23200, 0.10),
        (23201, 94300, 0.12),
        (94301, 201050, 0.22),
        (201051, 383900, 0.24),
        (383901, 487450, 0.32),
        (487451, 731200, 0.35),
        (731201, float('inf'), 0.37)
    ],
    'MARRIED FILING SEPARATELY': [
        (0, 11600, 0.10),
        (11601, 47150, 0.12),
        (47151, 100525, 0.22),
        (100526, 191950, 0.24),
        (191951, 243725, 0.32),
        (243726, 365600, 0.35),
        (365601, float('inf'), 0.37)
    ],
    'HEAD OF HOUSEHOLD': [
        (0, 16550, 0.10),
        (16551, 63100, 0.12),
        (63101, 100500, 0.22),
        (100501, 191950, 0.24),
        (191951, 243700, 0.32),
        (243701, 609350, 0.35),
        (609351, float('inf'), 0.37)
    ]
}


#----------------------------------------------------------------

state_tax_brackets = {
    
    "Alabama": [
        {"income_up_to": 500, "rate": 0.02},
        {"income_up_to": 3000, "rate": 0.05}
    ],
    "Alaska": None,  # Indicates no state income tax
    "Arizona": {"flat_rate": 0.025},  # Flat tax rate state
    "Arkansas": [
        {"income_up_to": 5100, "rate": 0.00},
        {"income_up_to": 87000, "rate": 0.047}
    ],
    "California": [
        {"income_up_to": 10099, "rate": 0.01},
        {"income_up_to": 677275, "rate": 0.123}
    ],
    "Colorado": {"flat_rate": 0.044},
    "Connecticut": [
        {"income_up_to": 10000, "rate": 0.03},
        {"income_up_to": 500000, "rate": 0.0699}
    ],
    "Delaware": [
        {"income_up_to": 2000, "rate": 0.00},
        {"income_up_to": 60001, "rate": 0.066}
    ],
    "District of Columbia": [
        {"income_up_to": 10000, "rate": 0.04},
        {"income_up_to": 1000000, "rate": 0.1075}
    ],
    "Florida": None,
    "Georgia": [
        {"income_up_to": 750, "rate": 0.01},
        {"income_up_to": 7001, "rate": 0.0575}
    ],
    "Hawaii": [
        {"income_up_to": 2400, "rate": 0.014},
        {"income_up_to": 200000, "rate": 0.11}
    ],
    "Idaho": {"flat_rate": 0.058},
    "Illinois": {"flat_rate": 0.0495},
    "Indiana": {"flat_rate": 0.0315},
    "Iowa": [
        {"income_up_to": 6000, "rate": 0.044},
        {"income_up_to": 75000, "rate": 0.06}
    ],
    "Kansas": [
        {"income_up_to": 15000, "rate": 0.031},
        {"income_up_to": 30000, "rate": 0.057}
    ],
    "Kentucky": {"flat_rate": 0.045},
    "Louisiana": [
        {"income_up_to": 12500, "rate": 0.0185},
        {"income_up_to": 50001, "rate": 0.0425}
    ],
    "Maine": [
        {"income_up_to": 24500, "rate": 0.058},
        {"income_up_to": 58050, "rate": 0.0715}
    ],
    "Maryland": [
        {"income_up_to": 1000, "rate": 0.02},
        {"income_up_to": 250000, "rate": 0.0575}
    ],
    "Massachusetts": [
        {"income_up_to": 8000, "rate": 0.05},
        {"income_up_to": 1000000, "rate": 0.09}
    ],
    "Michigan": {"flat_rate": 0.0405},
    "Minnesota": [
        {"income_up_to": 30070, "rate": 0.0535},
        {"income_up_to": 183341, "rate": 0.0985}
    ],
    "Mississippi": [
        {"income_up_to": 10000, "rate": 0.00},  # Assuming first $10,000 is tax-free
        {"income_up_to": 10001, "rate": 0.05}  # Flat rate for income over $10,001
    ],
    "Missouri": [
        {"income_up_to": 1207, "rate": 0.00},
        {"income_up_to": 8449, "rate": 0.0495}
    ],
    "Montana": [
        {"income_up_to": 3600, "rate": 0.01},
        {"income_up_to": 21600, "rate": 0.0675}
    ],
    "Nebraska": [
        {"income_up_to": 3700, "rate": 0.0246},
        {"income_up_to": 35730, "rate": 0.0664}
    ],
    "Nevada": None,
    "New Hampshire": {"interest_and_dividends": 0.04},  # Special case for interest and dividends
    "New Jersey": [
        {"income_up_to": 20000, "rate": 0.014},
        {"income_up_to": 1000000, "rate": 0.1075}
    ],
    "New Mexico": [
        {"income_up_to": 5500, "rate": 0.017},
        {"income_up_to": 210000, "rate": 0.059}
    ],
    "New York": [
        {"income_up_to": 8500, "rate": 0.04},
        {"income_up_to": 25000000, "rate": 0.109}
    ],
    "North Carolina": {"flat_rate": 0.0475},
    "North Dakota": [
        {"income_up_to": 44775, "rate": 0.00},
        {"income_up_to": 225975, "rate": 0.025}
    ],
    "Ohio": [
        {"income_up_to": 26050, "rate": 0.00},
        {"income_up_to": 115300, "rate": 0.0375}
    ],
    "Oklahoma": [
        {"income_up_to": 1000, "rate": 0.0025},
        {"income_up_to": 7200, "rate": 0.0475}
    ],
    "Oregon": [
        {"income_up_to": 4050, "rate": 0.0475},
        {"income_up_to": 125000, "rate": 0.099}
    ],
    "Pennsylvania": {"flat_rate": 0.0307},
    "Rhode Island": [
        {"income_up_to": 73450, "rate": 0.0375},
        {"income_up_to": 166950, "rate": 0.0599}
    ],
    "South Carolina": [
        {"income_up_to": 3200, "rate": 0.00},
        {"income_up_to": 16040, "rate": 0.064}
    ],
    "South Dakota": None,
    "Tennessee": None,
    "Texas": None,
    "Utah": {"flat_rate": 0.0465},
    "Vermont": [
        {"income_up_to": 45400, "rate": 0.0335},
        {"income_up_to": 229500, "rate": 0.0875}
    ],
    "Virginia": [
        {"income_up_to": 3000, "rate": 0.02},
        {"income_up_to": 17001, "rate": 0.0575}
    ],
    "Washington": None,  # While Washington does not have a traditional income tax, it does have a capital gains tax.
    "West Virginia": [
        {"income_up_to": 10000, "rate": 0.0236},
        {"income_up_to": 60000, "rate": 0.0512}
    ],
    "Wisconsin": [
        {"income_up_to": 13810, "rate": 0.035},
        {"income_up_to": 304170, "rate": 0.0765}
    ],
    "Wyoming": None  # Indicates no state income tax
}

