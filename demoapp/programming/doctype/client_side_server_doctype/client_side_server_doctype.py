# Copyright (c) 2023, sonu kumar and contributors
# For license information, please see license.txt

import frappe
from frappe import _ 
from frappe.model.document import Document

class clientsideserverDoctype(Document):
	pass


@frappe.whitelist()
def frappe_call(msg):
		import time
		time.sleep(2)
		frappe.msgprint(msg)
		return "Hi This message from frappe_call"


