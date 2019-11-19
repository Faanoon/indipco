from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

#@frappe.whitelist(allow_guest=True)
def duplicate_loan(self, method):
        last_transaction = frappe.get_list("Loan",
            fields=["loan_type", "status","applicant","name"],
            filters = {
                "applicant": self.applicant,
                "posting_date": ("<=", self.posting_date),
                "loan_type" : "Personal Loan",
                "name": ("!=", self.name)
            })
#       if self.loan_type=="Personal Loan":
#            for d in self.repayment_schedule:
#                if d.payment<=get_today():
#                    if d.balance_loan_amount=="0":
#                        frappe.throw(("You have not cleared previous loan"))
#                        frappe.throw(("You have not cleared previous loan", self.posting_date))

