# Copyright (c) 2023, Venture Force Global Inc and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class CouponIssued(Document):
	pass
	@frappe.whitelist()
	def get_item_balance_qty(item_code):
	    query = """
	        SELECT SUM(actual_qty) FROM `tabStock Ledger Entry`
	        WHERE item_code = %(item_code)s
	        GROUP BY item_code
	    """
	    qty = frappe.db.sql(query, {"item_code": item_code})
	    return qty[0][0]