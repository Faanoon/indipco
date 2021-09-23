// Copyright (c) 2016, Taazur and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Attendance Sheet"] = {
	"filters": [
{
"fieldname":"from_date",
"label": __("FROM Date"),
"fieldtype": "Date",
"default": frappe.datetime.month_start(date)
},

{
"fieldname":"to_date",
"label": __("To Date"),
"fieldtype": "Date",
"default": get_today()
},

{
"fieldname":"employee",
"label":__("Employee"),
"fieldtype":"Link",
"options":"Employee",
"default":""
}

	]
};
