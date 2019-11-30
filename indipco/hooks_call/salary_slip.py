from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document
from datetime import datetime
from datetime import timedelta

#@frappe.whitelist(allow_guest=True)
def validate_calculate_end_date(self,method):
    self.total_working_days=30
#    self.end_date=self.start_date+datetime.timedelta(days=30)
#            frappe.throw(_("test"))
