import frappe

@frappe.whitelist()
def get_item_balance_qty(item_code):
    query = "SELECT SUM(actual_qty) as balance_qty FROM `tabBin` " + \
            "WHERE item_code = %s AND warehouse IS NOT NULL"
    result = frappe.db.sql(query, item_code)
    balance_qty = result[0][0] if result and result[0] and result[0][0] else 0
    return balance_qty
