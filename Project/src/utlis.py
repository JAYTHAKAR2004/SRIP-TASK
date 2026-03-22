import re
import pyarrow.parquet as pq

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-zA-Z ]', '', text)
    return text

def load_data_in_batches(file_path, batch_size=100000):
    pf = pq.ParquetFile(file_path)

    for batch in pf.iter_batches(batch_size=batch_size):
        df = batch.to_pandas()
        df['DATA'] = df['DATA'].apply(clean_text)
        yield df