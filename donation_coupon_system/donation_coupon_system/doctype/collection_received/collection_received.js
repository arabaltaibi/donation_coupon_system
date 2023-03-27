// Copyright (c) 2023, Venture Force Global Inc and contributors
// For license information, please see license.txt

frappe.ui.form.on('Collection Received', {
setup: function(frm) {
		/*frm.set_query("donation", function() {
			return{
				filters:[
					['Item Group', 'parent_item_group', '=', 'Coupon']
				]
			};
		});*/
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


frappe.ui.form.on('Collection Received', {
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
        frm.set_query('bank_cd', function() {
            return {
                filters: [
                    ['account_type', '=', "Bank"]
                ]
            };
        });
        frm.set_query('credit_to', function() {
            return {
                filters: [
                    ['account_type', '=', "Bank"]
                ]
            };
        });
    }
});
frappe.ui.form.on('Collection Received Item', {
    item: function(frm, cdt, cdn) {
        var child = locals[cdt][cdn];
        frappe.call({
            method: 'donation_coupon_system.item_utils.get_item_balance_qty',
            args: { item_code: child.item },
            callback: function(response) {
                var balance_qty = response.message;
                frappe.model.set_value(cdt, cdn, 'balance_coupons', balance_qty);
                frappe.model.set_value(cdt, cdn, 'balance_amount', child.book_value*balance_qty);
            }
        });
    },
    coupons: function(frm, cdt, cdn){
        var child = locals[cdt][cdn];
        frappe.model.set_value(cdt, cdn, 'amount', child.coupons*child.book_value);
        frappe.model.set_value(cdt, cdn, 'balance_coupons_after_receipt', child.balance_coupons-child.coupons);
        frappe.model.set_value(cdt, cdn, 'balance_amount_after_receipt', child.balance_coupons_after_receipt*child.book_value);
    }
});
