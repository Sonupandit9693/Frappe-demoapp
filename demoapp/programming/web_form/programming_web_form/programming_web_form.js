frappe.ready(function() {
	// bind events here


	console.log(frappe.web_form.is_new);
	frappe.web_form.on('enable', (field, value)=> {
		frappe.msgprint("Hii user")
		console.log("Hii user");
	})

	frappe.web_form.on('dob', (field, value)=>{
		if(value){
			dob = new Date(value)
			var today = new Date()
			var age = Math.floor((today-dob) / 365.25 * 24 * 60 * 60 * 1000)
			frappe.web_form.set_value("age", [age])
		}
	})

	frappe.web_form.after_load = () => {
		// init script here
		// frappe.msgprint("Please fill the all value carefully");
		// console.log("Please fill the all value carefully");
	}
	
})