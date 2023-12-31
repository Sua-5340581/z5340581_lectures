""" lec_pd_dataframes.py

Companion codes for the lecture on Dataframes
"""

import pandas as pd


# ----------------------------------------------------------------------------
#   The dates and prices lists
# ----------------------------------------------------------------------------
dates = [
  '2020-01-02',
  '2020-01-03',
  '2020-01-06',
  '2020-01-07',
  '2020-01-08',
  '2020-01-09',
  '2020-01-10',
  '2020-01-13',
  '2020-01-14',
  '2020-01-15',
  ]

# Close prices
prices = [
  7.1600,
  7.1900,
  7.0000,
  7.1000,
  6.8600,
  6.9500,
  7.0000,
  7.0200,
  7.1100,
  7.0400,
  ]

# Business (trading) day counter
bday = [
  1,
  2,
  3,
  4,
  5,
  6,
  7,
  8,
  9,
  10]

# ----------------------------------------------------------------------------
#   Create two series
# ----------------------------------------------------------------------------

# Series with prices
prc_ser = pd.Series(data=prices, index=dates)

# Series with trading day
bday_ser = pd.Series(data=bday, index=dates)

# ----------------------------------------------------------------------------
#   Create a dataframe
# ----------------------------------------------------------------------------
# Using the series we created above...

# Data Frame with close and Bday columns
df = pd.DataFrame({'Close': prc_ser, 'Bday': bday_ser})

print(df)

dataframe = pd.DataFrame({'a': [1, 2, 3 ], 'b' : [4, 5, 6]}, index = ['c', 'd', 'e'] )
index = ['c', 'd', 'e']
#print(dataframe)

other_dates = [
  '2020-01-06',
  '2020-01-07',
  '2020-01-08',
  '2020-01-09',
  '2020-01-10',
  '2020-01-13',
  '2020-01-14',
  '2020-01-15',
  '2020-01-16',
  '2020-01-17',
  ]
other_bday = [
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        ]
new_bday_ser = pd.Series(data=other_bday, index=other_dates)
new_df = pd.DataFrame({'Close': prc_ser, 'Bday': new_bday_ser})
print(new_df)

#print(df['Close'])