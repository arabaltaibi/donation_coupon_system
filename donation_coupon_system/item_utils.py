import frappe
#from erpnext.stock.utils import get_stock_balance

@frappe.whitelist()
def get_item_balance_qty(item_code):
    query = "SELECT SUM(actual_qty) as balance_qty FROM `tabBin` " + \
            "WHERE item_code = %s AND warehouse IS NOT NULL"
    result = frappe.db.sql(query, item_code)
    balance_qty = result[0][0] if result and result[0] and result[0][0] else 0
    return balance_qty

#Get Item Balance Quantity in Coupon#

from erpnext.stock.utils import get_stock_balance
@frappe.whitelist()
def get_item_balance_qty_uom(item_code):
    # get the balance quantity in base UOM
    balance_qty = get_stock_balance(item_code, warehouse)
    
    # convert the balance quantity to UOM "Coupon"
    uom_conversion_factor = frappe.db.get_value("Item", item_code, "uom_conversion_factor")
    if uom_conversion_factor:
        balance_qty = balance_qty / uom_conversion_factor
    
    return balance_qty
