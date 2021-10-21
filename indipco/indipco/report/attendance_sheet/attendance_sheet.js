// Copyright (c) 2016, Taazur and contributors
// For license information, please see license.txt
/* eslint-disable */
//from frappe.utils import today, getdate, get_last_day


frappe.query_reports["Attendance Sheet"] = {
	"filters": [
{
"fieldname":"from_date",
"label": __("From Date"),
"fieldtype": "Date",
"default": frappe.datetime.add_days(frappe.datetime.add_months(frappe.datetime.month_start(date),-1),14)
},

{
"fieldname":"to_date",
"label": __("To Date"),
"fieldtype": "Date",
"default": get_today()
},

{
"fieldname":"doc_status",
"label": __("Attendance Status"),
"fieldtype": "Read Only",
"options": ["Draft","Submited","Cancelled"],
"default": "Submited"
}



	]
};
