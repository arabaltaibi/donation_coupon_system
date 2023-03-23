# donation_coupon_system/hooks/custom_fields.py

from __future__ import unicode_literals
import frappe

def add_custom_fields():
    # Define your custom fields here
    custom_fields = [
        {
            "fieldname": "coupon_details",
            "label": "Coupon Details",
            "fieldtype": "Section Break",
            "insert_after": "image"
        },
        {
            "fieldname": "book_size",
            "label": "Book Size",
            "fieldtype": "Int",
            "default": 0,
            "insert_after": "coupon_details"
        },
        {
            "fieldname": "cb1",
            "label": "",
            "fieldtype": "Column Break",
            "insert_after": "book_size"
        },
        {
            "fieldname": "coupon_value",
            "label": "Coupon Value",
            "fieldtype": "Currency",
            "insert_after": "cb1"
        },
        {
            "fieldname": "cb2",
            "label": "",
            "fieldtype": "Column Break",
            "insert_after": "coupon_value"
        },
        {
            "fieldname": "book_value",
            "label": "Book Value",
            "fieldtype": "Currency",
            "insert_after": "cb2"
        }
    ]

    # Loop over the custom fields and add them to the Item doctype
    for field in custom_fields:
        if not frappe.db.exists("Custom Field", {"fieldname": field["fieldname"]}):
            frappe.get_doc({
                "doctype": "Custom Field",
                "dt": "Item",
                "fieldname": field["fieldname"],
                "label": field["label"],
                "fieldtype": field["fieldtype"],
                "default": field["default"],
                "insert_after": field["insert_after"]
            }).insert(ignore_permissions=True)

# Call the add_custom_fields function when the app is installed
def after_install():
    add_custom_fields()
