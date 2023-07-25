// Copyright (c) 2023, sonu kumar and contributors
// For license information, please see license.txt

frappe.ui.form.on('client side server Doctype', {
	/*****************Client side scripting 'Events' *************/

	// refresh: function(frm) {
	// 	// frappe.msgprint("Hello from client side scripting");
	// 	frappe.throw("This is occured an error");
	// }

	// onload: function(frm){
	// 	frappe.msgprint("Hello from client side scripting / onloading event")
	// }


	// validate: function(frm){
	// 	frappe.throw("hello from client side 'validate' event");
	// }

	// before_save: function(frm){
	// 	frappe.throw("Hello fro clien side 'before_save' event");
	// }

	// after_save: function(frm){
	// 	frappe.throw("Hello from clien side 'after-save' event");
	// }

	// enable: function(frm){  
	// 	frappe.msgprint("Hello from Client side 'enable' fieldname event"); 
	// },

	// age: function(frm){
	// 	frappe.msgprint("Hello from client side 'age' fieldname event");
	// }

	// family_members_on_form_rendered: function(frm){
	// 	frappe.msgprint("Hello from client side from 'fimaly_members' child table rendered event");
	// }

	// before_submit: function(frm){
	// 	frappe.throw("Hello  from client side 'before_submit' event")
	// }

	// on_submit: function(frm){
	// 	frappe.msgprint("Hello from client side 'on_submit' event");
	// }

	// before_cancel: function(frm){
	// 	frappe.throw("Hello from client side 'on_cancel' event");
	// }

	// after_cancel: function(frm){
	// 	frappe.msgprint("Hello from client side 'after_cancel' event");
	// }


	/*************************Value fetching *****************************/
	// frm.doc.first_name
	// after_save: function(frm){
	// 	frappe.msgprint(`The full name is :${frm.doc.first_name} ${frm.doc.middle_name} ${frm.doc.last_name}`)
	// 	/*************************fetching value from child table*************************/
	// 	for(let row of frm.doc.family_members) {
	// 		frappe.msgprint(`${row.idx}. The family members is ${row.name1} and relation is ${row.relation} `)
	// 	}
	// }

	/**********************set intro event**********************************/
	// refresh: function(frm){
	// 	// frm.set_intro('Now you can create a new Client Side scripting doctype');

	// 	if(frm.is_new()){
	// 		frm.set_intro('Now you can create a new Client Side scripting doctype');
	// 	}
	// }


	/*********************set the value in client scripting********************/
	// validate: function(frm){
	// 	// frm.set_value('full_name', frm.doc.first_name +" "+ frm.doc.middle_name +" "+ frm.doc.last_name);

	// 	let row = frm.add_child('family_members',{
	// 		name1: 'sonu kumar',
	// 		relation: 'Father',
	// 		age: 56,
	// 	})
	// }


	/****************set Doc field property*******************/
	// enable: function(frm){
	// 	frm.set_df_property('first_name','reqd',1)

	// 	frm.set_df_property('middle_name','read_only',1)

	// 	frm.toggle_reqd('age', true)
	// }


	/*******************Button Event*********************/
	// refresh: function(frm){
	// 	frm.add_custom_button('Click Me Button', ()=>{
	// 		frappe.msgprint('You Clicked me !!')
	// 	})

	// 	frm.add_custom_button('Click Me1',()=>{
	// 		frappe.msgprint('You Clicked 1 !!!')
	// 	},'click me')

	// 	frm.add_custom_button('Click Me2',()=>{
	// 		frappe.msgprint('You CLicked 2!!');
	// 	},'click me');	
	// }


	// enable: function(frm){
	// 	frm.call({
	// 		doc: frm.doc,
	// 		method: "demoapp.programming.doctype.client_side_server_doctype.client_side_server_doctype.frappe_call",
	// 		args: {
	// 			msg : "Hello"
	// 		},
	// 		freeze: true,
	// 		freeze_message: 'calling frm_call Method',
	// 		callback: function(r){
	// 			frappe.msgprint(r.message)
	// 			frappe.msgprint("Server side calling Completed")
	// 			frm.refresh_field('medication orders')
	// 		}
	// 	})
	// }
});

/************************child table evnt****************/

frappe.ui.form.on("Family Members",{

	// name1: function(frm){
	// 	frappe.msgprint("Hello from Fimaly members 'name1' fieldname event");
	// }

	// age: function(frm){
	// 	frappe.msgprint("Hell from Familay members child table 'age' fieldname event");
	// }



	
})