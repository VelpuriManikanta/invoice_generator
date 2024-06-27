import os
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
from num2words import num2words

def generate_invoice(
    company_logo, seller_details, place_of_supply, billing_details, shipping_details, 
    place_of_delivery, order_details, invoice_details, reverse_charge, items, signature_image
):
    # Compute derived parameters
    for item in items:
        item['net_amount'] = item['unit_price'] * item['quantity'] - item['discount']
        if place_of_supply == place_of_delivery:
            item['tax_type'] = 'CGST/SGST'
            item['tax_amount'] = item['net_amount'] * item['tax_rate'] / 100 / 2
            item['tax_amount_cgst'] = item['tax_amount']
            item['tax_amount_sgst'] = item['tax_amount']
        else:
            item['tax_type'] = 'IGST'
            item['tax_amount'] = item['net_amount'] * item['tax_rate'] / 100
        item['total_amount'] = item['net_amount'] + item['tax_amount']

    total_amount = sum(item['total_amount'] for item in items)
    amount_in_words = num2words(total_amount, to='currency', lang='en_IN')

    # Prepare context for HTML template
    context = {
        'company_logo': company_logo,
        'seller_name': seller_details['name'],
        'seller_address': seller_details['address'],
        'seller_city': seller_details['city'],
        'seller_state': seller_details['state'],
        'seller_pincode': seller_details['pincode'],
        'seller_country': seller_details.get('country', 'IN'),
        'seller_pan': seller_details['pan'],
        'seller_gst': seller_details['gst'],
        'place_of_supply': place_of_supply,
        'billing_name': billing_details['name'],
        'billing_address': billing_details['address'],
        'billing_city': billing_details['city'],
        'billing_state': billing_details['state'],
        'billing_pincode': billing_details['pincode'],
        'billing_country': billing_details.get('country', 'IN'),
        'billing_state_code': billing_details['state_code'],
        'shipping_name': shipping_details['name'],
        'shipping_address': shipping_details['address'],
        'shipping_city': shipping_details['city'],
        'shipping_state': shipping_details['state'],
        'shipping_pincode': shipping_details['pincode'],
        'shipping_country': shipping_details.get('country', 'IN'),
        'shipping_state_code': shipping_details['state_code'],
        'place_of_delivery': place_of_delivery,
        'order_no': order_details['order_no'],
        'order_date': order_details['order_date'],
        'invoice_no': invoice_details['invoice_no'],
        'invoice_date': invoice_details['invoice_date'],
        'reverse_charge': reverse_charge,
        'items': items,
        'total_amount': total_amount,
        'amount_in_words': amount_in_words,
        'signature_image': signature_image
    }

    # Load HTML template
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('invoice_template.html')

    # Render HTML with context
    html_out = template.render(context)

    # Convert HTML to PDF
    pdf_out = HTML(string=html_out).write_pdf()

    # Save PDF to file
    with open('invoice.pdf', 'wb') as f:
        f.write(pdf_out)

# Example usage
if __name__ == "__main__":
    company_logo = 'D:\Invoice\sign.png'
    signature_image = 'D:\Invoice\logo.png'
    seller_details = {
        'name': 'Varasiddhi Silk Exports',
        'address': '* 75, 3rd Cross, Lalbagh Road',
        'city': 'BENGALURU',
        'state': 'KARNATAKA',
        'pincode': '560027',
        'pan': 'AACFV3325K',
        'gst': '29AACFV3325K1ZY'
    }
    place_of_supply = 'Bihar'
    billing_details = {
        'name': 'Madhu B',
        'address': 'Eurofins IT Solutions India Pvt Ltd., 1st Floor, Maruti Platinum, Lakshminarayana Pura, AECS Layou',
        'city': 'BENGALURU',
        'state': 'KARNATAKA',
        'pincode': '560037',
        'state_code': '29'
    }
    shipping_details = {
        'name': 'Madhu B',
        'address': 'Eurofins IT Solutions India Pvt Ltd., 1st Floor, Maruti Platinum, Lakshminarayana Pura, AECS Layou',
        'city': 'BENGALURU',
        'state': 'KARNATAKA',
        'pincode': '560037',
        'state_code': '29'
    }
    place_of_delivery = 'KARNATAKA'
    order_details = {
        'order_no': '403-3225714-7676307',
        'order_date': '28.10.2019'
    }
    invoice_details = {
        'invoice_no': 'KA-310565025-1920',
        'invoice_date': '28.10.2019'
    }
    reverse_charge = 'No'
    items = [
        {
            'description': 'Varasiddhi Silks Men\'s Formal Shirt (SH-05-42, Navy Blue, 42)',
            'unit_price': 338.10,
            'quantity': 1,
            'discount': 0,
            'tax_rate': 5.0
        },
        {
            'description': 'Shipping Charges',
            'unit_price': 30.96,
            'quantity': 1,
            'discount': 0,
            'tax_rate': 5.0
        }
    ]

    generate_invoice(
        company_logo, seller_details, place_of_supply, billing_details, shipping_details, 
        place_of_delivery, order_details, invoice_details, reverse_charge, items, signature_image
    )
