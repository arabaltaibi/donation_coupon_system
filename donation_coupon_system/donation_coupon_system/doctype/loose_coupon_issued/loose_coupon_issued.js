// Copyright (c) 2023, Venture Force Global Inc and contributors
// For license information, please see license.txt

frappe.ui.form.on('Loose Coupon Issued', {
	// refresh: function(frm) {

	// }
});
// Copyright (c) 2023, Venture Force Global Inc and contributors
// For license information, please see license.txt

frappe.ui.form.on('Loose Coupon Issued', {
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


frappe.ui.form.on('Loose Coupon Issued', {
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
frappe.ui.form.on('Loose Coupon Issued Items', {
    item: function(frm, cdt, cdn) {
        var child = locals[cdt][cdn];
        frappe.call({
            method: 'donation_coupon_system.item_utils.get_item_balance_qty',
            args: { item_code: child.item },
            callback: function(response) {
                var balance_qty = response.message;
                frappe.model.set_value(cdt, cdn, 'coupons_balance', balance_qty);
                frappe.model.set_value(cdt, cdn, 'value_balance', child.book_value*balance_qty);
            }
        });
    },
    coupons_issue: function(frm, cdt, cdn){
        var child = locals[cdt][cdn];
        frappe.model.set_value(cdt, cdn, 'value_issue', child.coupons_issue*child.book_value);
    }
});


frappe.ui.form.on('Loose Coupon Issued Items', {
coupons_balance: function(frm, cdt, cdn){
var d = locals[cdt][cdn];
var coupons_balance= 0;
frm.doc.items.forEach(function (d){ 
coupons_balance += d.coupons_balance; 
});
frm.set_value('total_coupons_balance', coupons_balance);
refresh_field('total_coupons_balance');
   }, 


items_remove: function(frm, cdt, cdn){
var d = locals[cdt][cdn];
var coupons_balance = 0;
frm.doc.items.forEach(function (d) {coupons_balance += d.coupons_balance;});
frm.set_value('total_coupons_balance', coupons_balance);
refresh_field('total_coupons_balance');
    },
value_balance: function(frm, cdt, cdn){
var d = locals[cdt][cdn];
var value_balance= 0;
frm.doc.items.forEach(function (d){ 
value_balance += d.value_balance; 
});
frm.set_value('total_value_balance', value_balance);
refresh_field('total_value_balance');
   }, 


items_remove: function(frm, cdt, cdn){
var d = locals[cdt][cdn];
var value_balance = 0;
frm.doc.items.forEach(function (d) {value_balance += d.value_balance;});
frm.set_value('total_value_balance', value_balance);
refresh_field('total_value_balance');
    },


coupons_issue: function(frm, cdt, cdn){
var d = locals[cdt][cdn];
var coupons_issue= 0;
frm.doc.items.forEach(function (d){ 
coupons_issue += d.coupons_issue; 
});
frm.set_value('total_coupons_issue', coupons_issue);
refresh_field('total_coupons_issue');
   }, 
items_remove: function(frm, cdt, cdn){
var d = locals[cdt][cdn];
var coupons_issue = 0;
frm.doc.items.forEach(function (d) {coupons_issue += d.coupons_issue;});
frm.set_value('total_coupons_issue', coupons_issue);
refresh_field('total_coupons_issue');
    },


value_issue: function(frm, cdt, cdn){
var d = locals[cdt][cdn];
var value_issue= 0;
frm.doc.items.forEach(function (d){ 
value_issue += d.value_issue; 
});
frm.set_value('total_value_issue', value_issue);
refresh_field('total_value_issue');
   }, 
items_remove: function(frm, cdt, cdn){
var d = locals[cdt][cdn];
var value_issue = 0;
frm.doc.items.forEach(function (d) {value_issue += d.value_issue;});
frm.set_value('total_value_issue', value_issue);
refresh_field('total_value_issue');
    },
}); 