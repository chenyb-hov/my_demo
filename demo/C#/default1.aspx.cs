using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace mypjo1
{
    public partial class default1 : System.Web.UI.Page
    {
        string user;
        string psw;
        protected void Page_Load(object sender, EventArgs e)
        {
            user = Request["user"];
            psw = Request["psw"];
            this.TextBox1.Text = user;
            this.TextBox2.Text = psw;
        }
    }
}