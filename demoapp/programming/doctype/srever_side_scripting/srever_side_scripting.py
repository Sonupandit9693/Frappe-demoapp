# Copyright (c) 2023, sonu kumar and contributors
# For license information, please see license.txt

import frappe
from frappe import _ 
from frappe.model.document import Document

class Sreversidescripting(Document):
	############Server side Event #################################
	# def validate(self):
	# 	frappe.msgprint("Hello Frappe from 'validate' event")


	# def before_insert(self):
	# 	frappe.throw("Hello Frappe from 'Before_Save' Event")

	# def after_insert(self):
	# 	frappe.throw("Hello Frappe from 'After_Save' Event")

	# def on_update(self):
	# 	frappe.msgprint("Hello Frappe from 'on_update' Event")

	# def before_submit(self):
	# 	frappe.msgprint("Hello Frappe from 'before_submit' event")

	# def on_submit(self):
	# 	frappe.msgprint("Hello frappe from 'on_submit' event")
	
	# def on_cancel(self):
	# 	frappe.msgprint("Hello Frappe from 'On_Cancel' Event")
	
	# def on_trash(self):
	# 	frappe.msgprint("Hello frappe from 'On Trash' Event")

	# def after_delete(self):
	# 	frappe.msgprint("Hello frappe from 'After delete' Event")

	################# Value Fecthing ######################

	# def validate(self):
	# 	frappe.msgprint(f"Hello my full name is {self.first_name} {self.middle_name} {self.last_name} ")

	# def validate(self):
	# 	for row in self.get("family_members"):
	# 		frappe.msgprint(f"{row.idx} The family member is {row.name1} and relation is {row.relation}") 

	#################frappe.get_doc(doctype, name) ##################
	#Return a document object of the record identified by doctype and name

	# frappe.get_doc(doctype, name)

	# def validate(self):
	# 	self.get_document()

	# def get_document(self):
	# 	doc = frappe.get_doc('client side server Doctype', self.client_side_doc)
	# 	frappe.msgprint(f'The first Name is {doc.first_name} and Age is {doc.age}')

	############## create a new document ################
	# frappe.new doc(doctype)

	# def validate(self):
	# 	self.new_document()

	# def new_document(self):
	# 	doc = frappe.new_doc('client side server Doctype')
	# 	doc.first_name = "Ajit"
	# 	doc.last_name = "Pandit"
	# 	doc.age = 67
	# 	doc.append("family_members", { "name1": "jain","relation": "Father","age": 14})
	# 	doc.insert()

	################ Delete a Doctype ############################
	# frappe.delete_doc(doctype, name)

	# def validate(self):
	# 	frappe.delete_doc('client side server Doctype', 'PR-0013')	

	#################### Document Methods ###############

	###### db.insert() ###############################################################

	# def validate(self):
	# 	self.new_document()

	# def new_document(self):
	# 	doc = frappe.new_doc('client side server Doctype')
	# 	doc.first_name = "ganguly"
	# 	doc.age = 14
	# 	doc.insert()

	############## some escape hatches that can be used to skip certain checks 

	# doc.insert(
	# 	ignore_permissions = True #	ignore write permission diring insert
	# 	ignore_links = True # ignore link validation in the document
	# 	ignore_if_duplicate = True # dont't insert if DuplicateEntryError is thrown
	# 	ignore_mandatroy=True # insert even if mandatory fields are not set
	# )


	####### doc.save() ##############

	# def validate(self):
	# 	self.save_document()

	# def save_document(self):
	# 	doc = frappe.new_doc('client side server Doctype')
	# 	doc.first_name = "Dany"
	# 	doc.last_name = "rahor"
	# 	doc.age = 30
	# 	doc.save()

	# 	doc.save(
	# 		ignore_permissions = True # ignore write permission during insert
	# 		ignore_versions = True # do naot create version record
	# 	)


	############# doc.delete() ##################

	# def validate(self):
	# 	self.delete_document()

	# def delete_document(self):
	# 	doc = frappe.get_doc('client side server Doctype', 'PR-0010')
	# 	doc.delete()

	############### doc.db.set() #############

	# def validate(self):
	# 	self.db_set_document()

	# def db_set_document(self):
	# 	doc = frappe.get_doc('client side server Doctype','PR-0002')
	# 	doc.db_set('age' , 80)

	


	######################################################################################
	##################### Datbase APIs ################################################

################ frappe.db_get_list(doctype, filters, or_filters, fields, order_by, group_by, start, page_length)###################

		# def validate(self):
		# 	self.get_list()

		# def get_list(self):
		# 	doc = frappe.db.get_list('client side server Doctype',
		# 	    filters={
		# 		    'enable': 1
		# 		},
		# 		fields=['first_name', 'age']
		# 		)
			
		# 	for d in doc:
		# 		frappe.msgprint(f"The parent first name is {d.first_name} and age is {d.age}")

########## Frappe.db.get_value(doctype,name,fieldname) or frappe.db.get_value(doctype,filters,fieldsname)

	# def validate(self):
	# 	self.get_value()

	# def get_value(self):
	# 	first_name, age = frappe.db.get_value('client side server Doctype', 'PR-0011', ['first_name', 'age']) 
	# 	frappe.msgprint(f"The parent name is {first_name} and age is {age}")

############ frappe.db.set_value(doctype, name, fieldname, value)
	# def validate(self):
	# 	self.set_value()

	# def set_value(self):
	# 	frappe.db.set_value('client side server Doctype', 'PR-0010', 'age', 25)
	# 	first_name, age = frappe.db.get_value('client side server Doctype', 'PR-0019', ['first_name', 'age'])
	# 	frappe.msgprint(f"The parent first Name is {first_name} and age is {age}")

############ frappe.db.exists(doctye,name) #####################

	# def validate(self):
	# 	if frappe.db.exists('client side server Doctype', 'PR-0045'):
	# 		frappe.msgprint(f"The Document is Exists in Database")
	# 	else:
	# 		frappe.msgprint(f"The Document in not Exist in Database !!!")


############# frappe.db.count(doctype, filter) ##################

	# def validate(self):
	# 	doc_count = frappe.db.count('client side server Doctype', {'enable': 1})  #True
	# 	frappe.msgprint(f"The Enable document count is {doc_count}")



##################### frappe.db.sql(query, filter, as_dict) ##################

	# def validate(self):
	# 	self.sql()

	# def sql(self):
	# 	data = frappe.db.sql(""" SELECT first_name, age from `tabclient side server Doctype` where enable = 1  """, 
	# 	       as_dict=1)
	
	# 	for d in data:
	# 		frappe.msgprint(f"The parent name is {d.first_name} and age is {d.age}")


#########################################################################################################
####################### Server side call ############################################################3
############## js
### Include this code in server_side_scripting.js    file !!!!!!!!!!!!!!!#############
	# enable: function(frm){
	# 		frm.call({
	# 			doc: frm.doc,
	# 			method: "frm_call",
	# 			args: {
	# 				msg : "Hello"
	# 			},
	# 			freeze: True,
	# 			freeze_message: _('calling frm_call Method'),
	# 			callback: function(r){
	# 				frappe.msgprint(r.message)
	# 				// frappe.msgprint("Server side calling Completed")
	# 				// frm.refresh field('medication orders')
	# 			}
	# 		})
	# }

	# @frappe.whitelist()
	# def frm_call(self,msg):
	# 	# import time
	# 	# time.sleep(2)
	# 	# frappe.msgprint(msg)
	# 	# self.mob_no= 545854646584
	# 	return "Hi This message from frm_call"
	pass