from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import flt, getdate, rounded, date_diff, getdate

#@frappe.whitelist(allow_guest=True)
def calculate_days_to_allocate(self,method):
    if self.from_date and self.to_date:
        self.ind_days_to_allocate = date_diff(self.to_date, self.from_date) + 1
        self.new_leaves_allocated = rounded(self.ind_days_to_allocate * self.ind_max_leaves_allowed / 365)
#            frappe.throw(_("Purpose should be 1.Manufacture 2.Material Transfer for Manufacture"))