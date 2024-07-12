import pandas as pd

def split_csv(file_path='updated.csv', chunk_size=500, output_prefix='updated_output'):
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # Define the column schema
    columns = ["id", "url", "name", "email", "created_at", "updated_at", "time_zone", "iana_time_zone", 
               "phone", "shared_phone_number", "photo", "locale_id", "locale", "role", "verified", 
               "external_id", "tags", "alias", "active", "shared", "shared_agent", "last_login_at", 
               "two_factor_auth_enabled", "signature", "details", "notes", "role_type", "custom_role_id", 
               "moderator", "ticket_restriction", "only_private_comments", "restricted_agent", "suspended", 
               "default_group_id", "report_csv", "user_fields", "abilities", "organization"] + ["" for _ in range(960)]

    # Calculate the number of chunks
    num_chunks = (len(df) // chunk_size) + 1
    
    for i in range(num_chunks):
        # Define the start and end of the chunk
        start = i * chunk_size
        end = (i + 1) * chunk_size
        
        # Extract the chunk
        chunk_df = df.iloc[start:end]
        
        # Ensure the chunk has the specified columns
        chunk_df = chunk_df.reindex(columns=columns)
        
        # Define the output file name
        output_file = f"{output_prefix}_{i+1}.csv"
        
        # Save the chunk to a new CSV file
        chunk_df.to_csv(output_file, index=False)
        print(f'Saved {output_file}')

# Example usage
split_csv()
