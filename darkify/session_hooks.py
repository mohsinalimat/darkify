import frappe


def make_it_dark():
	"""Switch to dark theme for all users"""
	for user in frappe.get_all("User", pluck="name"):
		frappe.db.set_value("User", user, "desk_theme", "Dark")
