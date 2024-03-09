import pandas as pd
import matplotlib.pyplot as plt

codebook_df = pd.read_csv('/Users/superdev/Downloads/food_coded.csv')

relevant_features = ['cook', 'eating_out', 'employment', 'ethnic_food', 'exercise', 'fruit_day', 'income', 'on_off_campus', 'pay_meal_out', 'sports', 'veggies_day']

relevant_df = codebook_df[relevant_features]
print(relevant_df.head())

relevant_df.boxplot()
plt.title('Boxplot of Relevant Features')
plt.xlabel('Features')
plt.ylabel('Values')
plt.show()
