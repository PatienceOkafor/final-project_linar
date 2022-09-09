import pandas as pd
df = pd.DataFrame({"Item": ["sweet","Books","Biscuits","shoes","bags","Polos","foot_wears"],
                    "Demand": [20,30,31,33,30,33,35],
                    "Price" : [2000, 1800,1850,1700,1900,2000,2500]
                    })
                    
print(df)

df["% Change in Demand"] = df["Demand"].pct_change()
df["% Change in Price"] = df["Price"].pct_change()
print(df["% Change in Demand"])
print(df["% Change in Price"])

df["Price Elasticity"] = df["% Change in Demand"] / df["% Change in Price"]
print(df["Price Elasticity"])
