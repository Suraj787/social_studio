# Copyright (c) 2023, techwizards and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import json

class TeleCallingReport(Document):
	pass
	
	
@frappe.whitelist()	
def Phone_Number_validation(doc):
    doc = json.loads(doc)
    Number_valid=frappe.db.get_value('Tele Calling Report', {'to': doc.get('to')}, ['name'])
    if Number_valid:
       phone=doc.get('to')
       frappe.throw(f"Number {phone} is alrady Present in '{Number_valid}' ")

    	
