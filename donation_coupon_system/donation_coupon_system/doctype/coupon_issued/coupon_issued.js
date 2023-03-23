// Copyright (c) 2023, Venture Force Global Inc and contributors
// For license information, please see license.txt
/*
frappe.ui.form.on("Coupon Issued", {
	setup: function(frm) {
		frm.set_query("donation", function() {
			return{
				filters:[
					['Item Group', 'parent_item_group', '=', 'Coupon']
				]
			};
		});
		frm.set_query("item", "items", function(doc, cdt, cdn) {
			var d = locals[cdt][cdn];
			return {
				//query: "erpnext.manufacturing.doctype.bom.bom.item_query",
				filters: {
					"item_group": frm.doc.donation 
				}
			};
		});


	}





});
*/

frappe.ui.form.on('Coupon Issued', {
    setup: function(frm) {
        var coupons_item_group = '';
        frappe.call({
            method: 'frappe.client.get_value',
            args: {
                doctype: 'Coupon Settings',
                fieldname: 'coupons_item_group',
                filters: {
                    name: 'Coupon Settings'
                }
            },
            async: false,
            callback: function(response) {
                coupons_item_group = response.message.coupons_item_group;
            }
        });
        frm.set_query('donation', function() {
            return {
                filters: [
                    ['parent_item_group', '=', coupons_item_group],
                    ['is_group', '=', 0]
                ]
            };
        });
    }
});


frappe.ui.form.on('Coupon Issued Item', {
    item: function(frm, cdt, cdn) {
        var child = locals[cdt][cdn];
        frappe.call({
            method: 'donation_coupon_system.item_utils.get_item_balance_qty',
            args: { item_code: child.item },
            callback: function(response) {
                var balance_qty = response.message;
                frappe.model.set_value(cdt, cdn, 'available_books', balance_qty);
                frappe.model.set_value(cdt, cdn, 'balance_book_value', child.book_value*balance_qty);
            }
        });
    }
});





