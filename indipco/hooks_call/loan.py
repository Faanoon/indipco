from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

#@frappe.whitelist(allow_guest=True)
def duplicate_loan(self, method):
        last_transaction = frappe.get_list("Loan",
            fields=["applicant", "status"],
            filters = {
                "applicant": self.applicant,
                "posting_date": ("<=", self.posting_date),
                "name": ("!=", self.name)
            })
#        if last_transaction and last_transaction[0].applicant=="1":
        if self.applicant=="1":
            frappe.throw(_("You have pending loan"))
#            msg = _("Article {0} {1} You have pending loan {2}")
