from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document
from datetime import datetime
from datetime import timedelta

#@frappe.whitelist(allow_guest=True)
def validate_calculate_end_date(self,method):
#    self.total_working_days=30
#    self.payment_days=self.total_working_days-self.leave_without_pay
    if (self.ind_leave_without_pay_25_percent>self.leave_without_pay):
        frappe.throw(_("Leave without Pay 25 percent should be less than Leave Without Pay"))
#    self.end_date=self.start_date+datetime.timedelta(days=30)
#            frappe.throw(_("test"))
