# invoice_generator
Before going this you have to istall docker and GTK3

Installation and Setup
Install Docker Desktop:

Download and install Docker Desktop from Docker's website.
Clone the Repository:

Clone your project repository or place your project files in a directory
Create Dockerfile and requirements.txt:

Ensure Dockerfile and requirements.txt are present in the project directory.
Running the Script
Open a terminal in your project directory.

Build the Docker Image:

powershell
Copy code
docker build -t invoice-generator .
Run the Docker Container:

powershell
Copy code
docker run -v D:\invoice_generator:/app invoice-generator
Check the Output:

The generated invoice PDF will be available in your project directory.
Input Parameters
Seller Details: Name, Address, (City, State, Pincode), PAN No., GST Registration No.
Place of Supply
Billing Details: Name, Address, (City, State, Pincode), State/UT Code
Shipping Details: Name, Address, (City, State, Pincode), State/UT Code
Place of Delivery
Order Details: Order No., Order Date
Invoice Details: Invoice No., Invoice Details, Invoice Date
Reverse Charge: Yes/No
Item Details:
Description
Unit Price
Quantity
Discount
Net Amount
Tax Rate
Signature Image
Sample Input and Output
Sample Input:

Example input parameters in a JSON file or a script.
Sample Output:

The generated PDF file.
