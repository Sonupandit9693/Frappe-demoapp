// Copyright (c) 2023, sonu kumar and contributors
// For license information, please see license.txt

frappe.ui.form.on('Srever side scripting', {
	enable: function(frm){
		frappe.call({
			method: "demoapp.programming.doctype.client_side_server_doctype.client_side_server_doctype.frappe_call",
			args: {
				msg : "Hello"
			},
			freeze: true,
			freeze_message: 'calling frappe_call Method',
			callback: function(r){
				frappe.msgprint(r.message)
				frappe.msgprint("Server side calling Completed")
				frm.refresh_field('medication orders')
			}
		})
}
});
