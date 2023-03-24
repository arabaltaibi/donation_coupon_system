frappe.ui.form.on("Item", {
book_size(frm)
   {
set(frm); 
   },
coupon_value(frm)
   {
set(frm);
   }
});

function set(frm) {
frm.set_value('book_value',frm.doc.book_size*frm.doc.coupon_value);
   }