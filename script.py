import csv

# File paths
input_file = 'domain_names.csv'
output_file = 'unique_companies.csv'

# Read the domain names from domain_names.csv
try:
    with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        locations_domains = [(row['Location Name'], row['Email_Domain']) for row in reader]
except FileNotFoundError as e:
    print(f"Error: File not found. {e.filename}")
    exit()
except KeyError as e:
    print(f"Error: Missing expected column in the input CSV file. {e}")
    exit()
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    exit()

# Read the existing unique_companies.csv into a dictionary
existing_data = {}
try:
    with open(output_file, mode='r', newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            existing_data[row['name']] = row
except FileNotFoundError:
    # If the file doesn't exist, we will create it
    pass
except Exception as e:
    print(f"An unexpected error occurred while reading {output_file}: {e}")
    exit()

# Update existing entries or add new ones
for location_name, email_domain in locations_domains:
    if location_name in existing_data:
        existing_data[location_name]['default'] = email_domain
    else:
        existing_data[location_name] = {
            'name': location_name,
            'external_id': '',
            'notes': '',
            'details': '',
            'default': email_domain,
            'shared': '',
            'shared_comments': '',
            'group': '',
            'tags': '',
            'custom_fields.<fieldkey>': ''
        }

# Define the header for the output CSV
output_header = [
    'name', 'external_id', 'notes', 'details', 'default',
    'shared', 'shared_comments', 'group', 'tags', 'custom_fields.<fieldkey>'
]

# Write the updated data back to unique_companies.csv
try:
    with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=output_header)
        writer.writeheader()
        for row in existing_data.values():
            writer.writerow(row)
except IOError as e:
    print(f"Error: An I/O error occurred. {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

print(f"Location names and email domains have been written to {output_file}")
