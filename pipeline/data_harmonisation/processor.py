import os
import controller as ctr
from sqlalchemy import create_engine

# Configuration
data_dir = os.environ['DATA_DIR']
target_data_table = 'HarmonisedData'
engine = create_engine('sqlite:///{0}/the_reading_machine.db'.format(data_dir))

# Harmonise data
harmonised_article = (
    ctr.harmonise_article(pos_sentiment_col='positive_sentiment',
                          neg_sentiment_col='negative_sentiment',
                          id_col='id'))

# Save back to database
harmonised_article.to_sql(con=engine, name=target_data_table, index=False,
                          if_exists='replace')
