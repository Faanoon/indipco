# Copyright (c) 2013, Taazur and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import flt, getdate

def execute(filters=None):
	columns, data = [], []
	columns=get_columns()
	data=get_data(filters)
	return columns, data
	
def get_columns():
	return [
        _("Employee") + ":Data:100",
        _("Employee Name") + ":Data:250",
        _("Absent") + ":Float:100",
        _("Present") + ":Float:100",
        _("On Leave") + ":Float:100",
        _("Work From Home") + ":Float:140",
        _("Total Working Days-WO") + ":Float:180",
        _("Deductible Hours") + ":Float:140"
	]

def get_data(filters):
	from_date=filters.get("from_date")
	to_date=filters.get("to_date")
#	employee=filters.get("employee")
#	absent1=filters.get("absent1")
	return frappe.db.sql("""
		select
		A.employee,
		B.employee_name,
        sum(if(A.status="Absent",1,0)),
        sum(if(A.status="Present",1,0)),
        sum(if(A.status="On Leave",1,0)),
        sum(if(A.status="Work From Home",1,0)),

        sum(if(A.status="Absent",1,0))+sum(if(A.status!="Absent",1,0)),
        sum(A.ind_deductible_hours)
					
		FROM
		`tabAttendance` as A,
        `tabEmployee` as B
				
		WHERE
        A.employee=B.name
		&&A.attendance_date>='%s'
		&&A.attendance_date<='%s'

        
		GROUP BY A.employee
		ORDER BY A.employee ASC 
        """ %(from_date,to_date), as_list=1)
