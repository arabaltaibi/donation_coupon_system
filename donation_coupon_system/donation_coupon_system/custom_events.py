import frappe

def update_serial_number(self,method):
    frappe.msgprint("ok")
    for item in self.items:
        item_doc = frappe.get_doc("Item",item.item_code)
        if item_doc.current_serial_no == 0:
            item_doc.db_set("current_serial_no",item_doc.serial_start_from + item.qty)
        else:
           item_doc.db_set("current_serial_no",item_doc.current_serial_no + item.qty) 
@frappe.whitelist()
def get_serial_data(item_code,parent):
    last_value = frappe.db.get_value("Coupon Issued Item",{"docstatus":1,"parent":["!=",parent],"item":item_code},"to")
    if last_value:
        return last_value
    else:
        return 0
