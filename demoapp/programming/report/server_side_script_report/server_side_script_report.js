// Copyright (c) 2023, sonu kumar and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Server Side Script Report"] = {
	"filters": [
		{
			"fieldname": "name",
			"label": __("Srever side scripting"),
			"fieldtype": "Link",
			"options": "Srever side scripting"
		},
		{
			"fieldname": "dob",
			"label": __("DOB"),
			"fieldtype": "Date",
			// "default": frappe.datetime.now_date(),
		},
		{
			"fieldname": "age",
			"label": __("Age"),
			"fieldtype": "Data",
		}
	]
};
