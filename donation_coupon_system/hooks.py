from . import __version__ as app_version

app_name = "donation_coupon_system"
app_title = "Donation Coupon System"
app_publisher = "Venture Force Global Inc"
app_description = "Donation Coupon System Allows to collect donations via Coupon books from diffrent collection areas."
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "shahrukh@telniasoft.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/donation_coupon_system/css/donation_coupon_system.css"
# app_include_js = "/assets/donation_coupon_system/js/donation_coupon_system.js"

# include js, css files in header of web template
# web_include_css = "/assets/donation_coupon_system/css/donation_coupon_system.css"
# web_include_js = "/assets/donation_coupon_system/js/donation_coupon_system.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "donation_coupon_system/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "donation_coupon_system.install.before_install"
# after_install = "donation_coupon_system.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "donation_coupon_system.uninstall.before_uninstall"
# after_uninstall = "donation_coupon_system.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "donation_coupon_system.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"donation_coupon_system.tasks.all"
# 	],
# 	"daily": [
# 		"donation_coupon_system.tasks.daily"
# 	],
# 	"hourly": [
# 		"donation_coupon_system.tasks.hourly"
# 	],
# 	"weekly": [
# 		"donation_coupon_system.tasks.weekly"
# 	]
# 	"monthly": [
# 		"donation_coupon_system.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "donation_coupon_system.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "donation_coupon_system.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "donation_coupon_system.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"donation_coupon_system.auth.validate"
# ]

# Translation
# --------------------------------

# Make link fields search translated document names for these DocTypes
# Recommended only for DocTypes which have limited documents with untranslated names
# For example: Role, Gender, etc.
# translated_search_doctypes = []

doc_events = {
    "Coupon Issued Item": {
        "validate": "donation_coupon_system.donation_coupon_system.item_utils.get_item_balance_qty"
    }
}
# donation_coupon_system/hooks.py

app_include_files = ["assets/js/custom.js", "assets/css/custom.css", "hooks/custom_fields.py", "config/my_module.py"]
# donation_coupon_system/hooks.py

app_include_hooks = [
    "donation_coupon_system.donation_coupon_system.doctype.coupon_issued.coupon_issued.get_data"
    "donation_coupon_system.donation_coupon_system.doctype.coupon_settings.coupon_settings.get_data"
]