from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

#@frappe.whitelist(allow_guest=True)
def validate_absent_days(self,method):
    if self.ind_absent_days!=0:
        self.payment_days=self.ind_absent_days
#            frappe.throw(_("Purpose should be 1.Manufacture 2.Material Transfer for Manufacture"))
