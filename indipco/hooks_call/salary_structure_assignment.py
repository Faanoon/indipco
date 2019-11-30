from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document
from datetime import datetime
from datetime import timedelta

#@frappe.whitelist(allow_guest=True)
def calculate_service_days(self,method):
    if self.ind_end_of_service=="Yes":
        self.ind_service_days=10
#        frappe.throw(_("Test"))
