# !pip install datasets_sql
from datasets_sql import query

dataset = load_dataset("imdb", split="train")

# If you dont have an id column just add one by enumerating
dataset=dataset.map(lambda x,i: {"id":i}, with_indices=True)

id_column='id'
unique_column='text'

# always selects min id
unique_dataset = query(f"SELECT dataset.* FROM dataset JOIN (SELECT MIN({id_column}) as unique_id FROM dataset group by {unique_column}) ON unique_id=dataset.{id_column}")
