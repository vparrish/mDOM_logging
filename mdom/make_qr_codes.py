import csv
import os
import qrcode

def generate_qr_code(data, output_folder, count):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    
    # Generate a unique filename based on the count
    filename = f"half_A_{count}.png"
    
    # Save the QR code image to the specified folder
    img.save(os.path.join(output_folder, filename))

def convert_csv_to_qrcodes(csv_file, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Read the CSV file and generate QR codes for each entry
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for count, row in enumerate(reader, start=1):
            for entry in row:
                generate_qr_code(entry, output_folder, count)

if __name__ == "__main__":
    # Specify the input CSV file and output folder
    input_csv_file = 'qr_links.csv'  # Change this to your CSV file
    output_folder = 'output_qrcodes'  # Change this to your desired output folder

    convert_csv_to_qrcodes(input_csv_file, output_folder)
    print("QR codes generated and saved successfully.")
