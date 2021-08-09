import frappe


def make_it_dark():
	"""Switch to dark theme for all users"""
	all_users = frappe.get_all("User", pluck="name")
	for user in all_users:
		frappe.db.set_value("User", user, "desk_theme", "Dark")
