from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

#@frappe.whitelist(allow_guest=True)
def sales_user_validation(self,method):
    if (self.ind_department!="Sales - INDIPCO"):
        for d in self.get("items"):
            if (d.item_code=="IND-RM-001"):
                frappe.throw(_("Cannot return article not issued"))
#            if (self.material_request_type=="Material Transfer"):      
#        if (frappe.get_roles(frappe.session.user)!="Sales User"):
               
