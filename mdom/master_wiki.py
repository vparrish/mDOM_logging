import csv

# Function to format the entry text with the given number
def format_entry(number):
    return f"= mDOM {number} =\nPut COMMON mDOM links here! So anything having to do with gel pour\n== half A ==\nPut links to the lab notes here!\n== half B ==\nPut links to the lab notes here!\n"

# Number of entries
num_entries = 202

# File path to save the text file
file_path = "master_wiki.txt"

# Open the file in write mode
with open(file_path, "w") as file:
    # Open CSV file for writing links
    csv_file_path = "qr_links.csv"
    with open(csv_file_path, "w", newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        # Write header to CSV file
        csv_writer.writerow(["Link Number", "Link"])

        # Iterate through numbers from 1 to 202 for entries and links
        for entry_number in range(1, num_entries + 1):
            # Format the entry text with the current number
            entry_text = format_entry(str(entry_number).zfill(3))
            
            # Write the formatted entry to the text file
            file.write(entry_text)

            # Generate and write the link to the CSV file
            link_number = str(entry_number)
            link = f"https://wiki.icecube.wisc.edu/index.php/Upgrade_Device_Assembly#half_A_{link_number}"
            csv_writer.writerow([link_number, link])

print(f"Files '{file_path}' and '{csv_file_path}' have been created with {num_entries} entries and links.")
