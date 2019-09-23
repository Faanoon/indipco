from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

@frappe.whitelist(allow_guest=True)
def duplicate_loan(self, method):
        last_transaction = frappe.get_list("Loan",
            fields=["applicant_type", "status"],
            filters = {
                "applicant": self.applicant,
                "posting_date": ("<=", self.posting_date),
                "name": ("!=", self.name)
            })
        if self.applicant_type=="Employee":
            frappe.throw(_("Cannot return article not issued"))
