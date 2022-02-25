import pandas as pd

milk = ['one','two','three']
tea = ['five','six','seven']

final = pd.DataFrame(milk,tea)
final.to_csv('/root/arvin/scraper/catherine_scraper/test_df.csv')
