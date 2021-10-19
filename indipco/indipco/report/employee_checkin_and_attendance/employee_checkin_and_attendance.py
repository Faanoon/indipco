# Copyright (c) 2013, Taazur and contributors
# For license information, please see license.txt

# import frappe
from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import flt, getdate

def execute(filters=None):
	columns, data = [], []
	columns=get_columns(filters)
	data=get_data(filters)
	return columns, data

def get_columns(filters):
 #if filters.get("report_type"):
    if filters.get("report_type")=="Daily Attendance Daitails":
        return [
            _("Employee") + ":Data:90",
            _("Employee Name") + ":Data:200",
            _("Attendance ID") + ":Link/Attendance:160",
            _("Attendance") + ":Data:100",
            _("Checkin") + ":Date:160",
            _("Checkout") + ":Date:160",
            _("Present Hours") + ":Float:120",
            _("Deductible Hours") + ":Float:130",
            _("Approved Hours") + ":Float:130"
#           _("Work From Home") + ":Float:140",
#           _("Total Working Days-WO") + ":Float:180",
#           _("Deductible Hours") + ":Float:140"
        ]
    
    if filters.get("report_type")=="Monthly Salary Summary":
        return [
            _("Employee") + ":Data:90",
            _("Employee Name") + ":Data:250",
            _("Absent") + ":Float:100",
            _("Present") + ":Float:100",
            _("On Leave") + ":Float:100",
            _("Work From Home") + ":Float:140",
            _("Total Working Days-WO") + ":Float:180",
            _("Deductible Hours") + ":Float:140",
            _("Salary Slip") + ":Link/Salary Slip:180",
#           _("Basic A'ce") + ":Float:120"
#            _("Housing A'ce") + ":Float:120",
#            _("Transport A'ce") + ":Float:120",
#            _("Mobile A'ce") + ":Float:120",
#            _("Other /nA'ce") + ":Float:120",
#            _("Social A'ce") + ":Float:120",
            _("Gross Paid") + ":Float:120",
            _("Total Deduction") + ":Float:120",
            _("Net Paid") + ":Float:120"
        ]
    
def get_data(filters):
    from_date=filters.get("from_date")    
    to_date=filters.get("to_date")
    employee=filters.get("employee")    
    if filters.get("report_type")=="Daily Attendance Daitails":
        return frappe.db.sql("""
            select
            A.employee,
            A.employee_name,
            A.attendance,
            B.status,
            B.in_time,
#           if(A.log_type="IN",A.time,0),
            B.out_time,
            B.working_hours,
            if(B.status="Present",B.ind_deductible_hours,0),
            if(B.status="Present",B.ind_approved_hours,0)
#           sum(if(A.status="On Leave",1,0)),
#           sum(if(A.status="Work From Home",1,0)),
#           sum(if(A.status="Absent",1,0))+sum(if(A.status!="Absent",1,0)),
#           sum(A.ind_deductible_hours)
					
            FROM
            `tabEmployee Checkin` as A,
            `tabAttendance` as B
        
            WHERE
            A.attendance=B.name
            &&B.attendance_date>='%s'
            &&B.attendance_date<='%s'
            &&A.employee='%s'

            GROUP BY A.attendance
            ORDER BY A.employee ASC, B.attendance_date DESC 
            """ %(from_date,to_date,employee), as_list=1)

    elif filters.get("report_type")=="Monthly Salary Summary":
        from_date=filters.get("from_date")
        to_date=filters.get("to_date")
        return frappe.db.sql("""
        select
        A.employee,
        B.employee_name,
        sum(if(A.status="Absent",1,0)),
        sum(if(A.status="Present",1,0)),
        sum(if(A.status="On Leave",1,0)),
        sum(if(A.status="Work From Home",1,0)),
        sum(if(A.status="Absent",1,0))+sum(if(A.status!="Absent",1,0)),
        sum(A.ind_deductible_hours),
        C.name,
        C.gross_pay,
        C.total_deduction,
        C.net_pay
        
        FROM
        `tabAttendance` as A,
        `tabEmployee` as B,
        `tabSalary Slip` as C,
        `tabSalary Detail` as C1
        
        WHERE
        A.employee=B.name
        &&A.employee=C.employee
        &&C.name=C1.parent
        &&A.attendance_date>='%s'
        &&A.attendance_date<='%s'
        &&C.posting_date between '%s' and '%s'
        
        GROUP BY A.employee
        ORDER BY A.employee ASC 
        """ %(from_date,to_date,from_date,to_date), as_list=1)
        

        
        