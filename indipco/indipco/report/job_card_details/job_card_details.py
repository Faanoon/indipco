# Copyright (c) 2013, Taazur and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import flt, getdate

def execute(filters=None):
	columns, data = [], []
	columns=get_columns()
	data=get_data()
	return columns, data

def get_columns():
	return [
		_("Wok Order") + ":Link/Work Order:130",
		_("Job Card") + ":Link/Job Card:100",
		_("Operation") + ":Data:130",
		_("Workstation") + ":Data:130",
		_("For Quantity") + ":Float:100",
		_("Completed Qty") + ":Float:110",
		_("Rejection") + ":Float:80",
		_("Time Takes(min)") + ":Float:60",
		_("JC Status") + ":Data:80",
		_("WO Status") + ":Data:80"
	]

def get_data():
	return frappe.db.sql("""
	select
	A.work_order,
	A.name,
	A.operation,
	A.workstation,
	A.for_Quantity,
	A.total_completed_qty,
	(A.for_quantity-A.total_completed_qty),
	A.total_time_in_mins,
	A.status,
	B.status

	FROM
	`tabJob Card` as A,
	`tabWork Order` as B

	WHERE
	A.work_order=B.name

	ORDER BY A.name ASC

	""")