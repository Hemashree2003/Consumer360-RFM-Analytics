import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

print("Running Market Basket Analysis...")

df = pd.read_csv("Data/sales.csv")

# Create Basket Matrix
basket = df.groupby(['order_id','product_id'])['quantity'] \
           .sum().unstack().fillna(0)

basket = basket.applymap(lambda x: 1 if x > 0 else 0)

# Generate Frequent Itemsets
frequent_items = apriori(basket, min_support=0.1, use_colnames=True)

# Generate Rules
rules = association_rules(frequent_items, metric="lift", min_threshold=1)

print(rules)

rules.to_csv("Output/basket_output.csv", index=False)

print("Market Basket Analysis Completed")