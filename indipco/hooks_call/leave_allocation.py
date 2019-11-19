from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import flt, getdate, rounded, date_diff, getdate

#@frappe.whitelist(allow_guest=True)
def calculate_days_to_allocate(self,method):
    self.from_date=frappe.defaults.get_user_default("year_start_date")
    self.to_date=frappe.defaults.get_user_default("year_end_date")
    if date_diff(self.from_date, self.ind_date_of_joining)<0:
        self.ind_days_to_allocate = date_diff(self.to_date, self.ind_date_of_joining)
        self.new_leaves_allocated = rounded(self.ind_days_to_allocate * self.ind_max_leaves_allowed / 365)
    else:
        self.new_leaves_allocated=self.ind_max_leaves_allowed