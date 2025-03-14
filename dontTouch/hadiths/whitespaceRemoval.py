import csv
import re

def clean_whitespace(text):
    """Remove extra whitespace from the text."""
    return re.sub(r'\s+', ' ', text).strip()

def clean_csv_whitespace(input_filename, output_filename):
    with open(input_filename, 'r', encoding='utf-8') as infile, open(output_filename, 'w', encoding='utf-8', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        headers = next(reader)
        writer.writerow([clean_whitespace(header) for header in headers])
        
        for row in reader:
            cleaned_row = [clean_whitespace(cell) for cell in row]
            writer.writerow(cleaned_row)

# Run the function
clean_csv_whitespace('sahih_hadiths.csv', 'sahih_hadiths_wsr.csv') # wsr = white space removerd
