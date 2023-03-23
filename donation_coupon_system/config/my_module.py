# donation_coupon_system/config/my_module.py

from __future__ import unicode_literals

def get_data():
    return {
        "label": "Donation Coupon System",
        "icon": "octicon octicon-gift",
        "color": "#3498db",
        "type": "module",
        "description": "Manage donation coupons for your organization",
        "doctype": {
            "Coupon Issued": "donation_coupon_system.donation_coupon_system.doctype.coupon_issued.coupon_issued",
            "Coupon Settings": "donation_coupon_system.donation_coupon_system.doctype.coupon_settings.coupon_settings"
        }
    }
