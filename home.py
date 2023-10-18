import random
import pandas as pd
lst = ['robot'] * 10 + ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
one_hot_encoded = pd.get_dummies(data['whoAmI'], prefix='whoAmI')
data = pd.concat([data, one_hot_encoded], axis=1)
data = data.drop(columns=['whoAmI'])
data.head()