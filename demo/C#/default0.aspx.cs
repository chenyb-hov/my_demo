using System;
using System.Collections;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace mypjo1
{
    public partial class default0 : System.Web.UI.Page
    {
        public string user;
        public string password;
        protected void Page_Load(object sender, EventArgs e)
        {
            user = Request["user"];
            password = Request["psw"];
            Console.WriteLine(user);
            var list1 = new ArrayList();
            list1.Add("a");
            list1.Add("b");
            list1.Add("c");
            list1.Add("d");
            list1.TrimToSize();
            list1.Sort();
            this.RadioButtonList1.DataSource = list1;
            this.RadioButtonList1.DataBind();

            var list2 = new Hashtable();
            list2.Add("z", "zzz");
            list2.Add("x", "xxx");
            list2.Add("v", "vvv");
            list2.Add("n", "nnn");
            this.CheckBoxList1.DataSource = list2;
            this.CheckBoxList1.DataValueField = "Key";
            this.CheckBoxList1.DataTextField = "Value";
            this.CheckBoxList1.DataBind();

            var list3 = new SortedList();
            list3.Add("s", "sss");
            list3.Add("f", "fff");
            list3.Add("g", "ggg");
            list3.Add("h", "hhh");
            this.DropDownList1.DataSource = list3;
            this.DropDownList1.DataValueField = "Key";
            this.DropDownList1.DataTextField = "Value";
            this.DropDownList1.DataBind();

            var list4 = new DataSet();
            list4.ReadXml(MapPath("cs.xml"));
            this.radio2.DataSource = list4;
            this.radio2.DataValueField = "value";
            this.radio2.DataTextField = "text";
            this.radio2.DataBind();

            var list5 = new DataSet();
            list5.ReadXml(MapPath("cs1.xml"));
            this.repeater.DataSource = list5;
            this.repeater.DataBind();

            var list6 = new DataSet();
            list6.ReadXml(MapPath("cs1.xml"));
            
            this.DataList1.DataSource = list6;
            this.DataList1.DataBind();
            
        }
        protected void Button1_Click(object sender, EventArgs e)
        {
            this.Input1.Text = password;
            Server.Transfer("default1.aspx?user=" + user + "&psw=" + password, true);
        }
    }
}