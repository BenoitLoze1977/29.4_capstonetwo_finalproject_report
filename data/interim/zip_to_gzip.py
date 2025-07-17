import gzip
import shutil

input_file = r'C:\Users\Benoit Loze\Desktop\sf_df_encoded.csv'
output_file = r'C:\Users\Benoit Loze\Desktop\sf_df_encoded.csv.gz'

with open(input_file, 'rb') as f_in:
    with gzip.open(output_file, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

print("✅ CSV file compressed successfully as .gz")