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
#        _("Attendance") + ":Link/Attendance:180",
        _("Employee") + ":Link/Employee:100",
#        _("Employee Name") + ":Data:1",
#        _("Attendance Date") + ":Data:140",
        _("Status") + ":Data:140",
#        _("Total Absent Days") + ":Int:140",
#        _("Total Present Days") + ":Int:160",
        _("Total Working Days") + ":Int:160",
        _("Working Hours") + ":Data:140",
        _("Deductible Hours") + ":Data:140"
	]

def get_data(filters):
	from_date=filters.get("from_date")
	to_date=filters.get("to_date")
	employee=filters.get("employee")
	return frappe.db.sql("""
		select
#		A.name,
		A.employee,
#        A.employee_name,
#        A.attendance_date,
        A.status,
#        sum(if(A.status="Absent",1,0)),
#        sum(if(A.status!="Absent",1,0)),
        sum(if(A.status="Absent",1,0))+sum(if(A.status!="Absent",1,0)),
		sum(A.working_hours),
        sum(A.ind_deductible_hours)
					
		FROM
		`tabAttendance` as A
				
		WHERE
		A.attendance_date>='%s'
		&&A.attendance_date<='%s'
		&&A.employee='%s'
        
		GROUP BY A.status
		ORDER BY A.status ASC """ %(from_date,to_date,employee), as_list=1)
