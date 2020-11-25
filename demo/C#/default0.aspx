<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="default0.aspx.cs" Inherits="mypjo1.default0" %>
<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <title></title>
</head>
<body>
    <form id="form1" runat="server" action="default0.aspx" onsubmit ="return resgiter()">
        <div>
            username : <input class ="user" name="user"/><br/>
            password : <input class ="psw" name ="psw" type="password"/><br/>
            <input type="submit"/>
        </div>
        <div>
            <asp:TextBox ID="Input1" runat="server" Text ="input"/>
            <asp:Button ID="Button1" runat="server" Text="Button" onclick="Button1_Click" />
            <asp:Label ID="Label1" runat="server" Text="Label"></asp:Label>
        </div>
        </br>
        <asp:TextBox ID="onblur" TextMode="MultiLine" ontextchanged="Button1_Click" runat="server"/>
        <asp:RadioButtonList ID="countrylist" runat="server">
            <asp:ListItem Value="N" Text="Norway" />
            <asp:ListItem Value="S" Text="Sweden" />
            <asp:ListItem Value="F" Text="France" />
            <asp:ListItem Value="I" Text="Italy" />
        </asp:RadioButtonList>
        <asp:CheckBoxList ID="RadioButtonList1" runat="server">
        </asp:CheckBoxList>
        <asp:DropDownList ID="CheckBoxList1" runat="server">
        </asp:DropDownList>
        <asp:ListBox ID="DropDownList1" runat="server">
        </asp:ListBox>
        <asp:RadioButtonList ID="radio2" runat="server">
        </asp:RadioButtonList>
        
        <asp:Repeater ID="repeater" runat="server">
            <HeaderTemplate>
                <table border="1">
                <tr>
                    <th>Title</th>
                    <th>Artist</th>
                    <th>Country</th>
                    <th>Company</th>
                    <th>Price</th>
                    <th>Year</th>
                </tr>
                </HeaderTemplate>
                <ItemTemplate>
                <tr>
                    <td><%#DataBinder.Eval(Container.DataItem,"title")%></td>
                    <td><%#DataBinder.Eval(Container.DataItem,"artist")%></td>
                    <td><%#DataBinder.Eval(Container.DataItem,"country")%></td>
                    <td><%#DataBinder.Eval(Container.DataItem,"company")%></td>
                    <td><%#DataBinder.Eval(Container.DataItem,"price")%></td>
                    <td><%#DataBinder.Eval(Container.DataItem,"year")%></td>
                </tr>
                </ItemTemplate>

            <alternatingitemtemplate>
                <tr bgcolor="#e8e8e8">
                    <td><%#DataBinder.Eval(Container.DataItem,"title")%></td>
                    <td><%#DataBinder.Eval(Container.DataItem,"artist")%></td>
                    <td><%#DataBinder.Eval(Container.DataItem,"country")%></td>
                    <td><%#DataBinder.Eval(Container.DataItem,"company")%></td>
                    <td><%#DataBinder.Eval(Container.DataItem,"price")%></td>
                    <td><%#DataBinder.Eval(Container.DataItem,"year")%></td>
                </tr>
            </alternatingitemtemplate>

            <FooterTemplate>
                </table>
            </FooterTemplate>
        
        </asp:Repeater>
        <asp:DataList ID="DataList1" GridLines="Both" runat="server">
            <HeaderTemplate>
                this is title
            </HeaderTemplate>
            <ItemTemplate>
                "<%#DataBinder.Eval(Container.DataItem,"title")%>" of
                <%#DataBinder.Eval(Container.DataItem,"artist")%> -
                $<%#DataBinder.Eval(Container.DataItem,"price")%>
            </ItemTemplate>
            <FooterTemplate>
                this is end
            </FooterTemplate>
        </asp:DataList>
    </form>
    <p><%Response.Write(DateTime.Now.ToString()); %></p>
    
    <%--<p>
        <asp:RangeValidator
            ControlToValidate="Input1"
            MinimumValue="1"
            MaximumValue="100"
            Type="Integer"
            Text="The value must be from 1 to 100!"
            runat="server" />
    </p>--%>
    <script>
        function resgiter() {
            var user = document.getElementsByClassName("user")[0].value;
            var psw = document.getElementsByClassName("psw")[0].value;
            console.log(user);
            console.log(psw);
            if (user.length > 0 && psw.length > 0) {
                return true;
            }
            else {
                return false;
            }
        }
    </script>
</body>
</html>
