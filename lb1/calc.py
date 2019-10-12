#pip install wxPython
import wx

class calc(wx.Frame):
    def __init__(self, parent, title):
        super(calc, self).__init__(parent, title=title,
            size=(350, 250))

        self.ls = []
        self.InitUI()

    # make ui and bind listeners
    def InitUI(self):
        panel = wx.Panel(self)
        font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(9)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add((0, 0))
        
        #line 0
        hbox0 = wx.BoxSizer(wx.HORIZONTAL)

        plus = wx.Button(panel, label='+', size=(70, 30))
        hbox0.Add(plus)
        plus.Bind(wx.EVT_BUTTON, self.OnClicked) 

        minus = wx.Button(panel, label='-', size=(70, 30))
        hbox0.Add(minus)
        minus.Bind(wx.EVT_BUTTON, self.OnClicked) 

        div = wx.Button(panel, label='/', size=(70, 30))
        hbox0.Add(div)
        div.Bind(wx.EVT_BUTTON, self.OnClicked)

        mul = wx.Button(panel, label='*', size=(70, 30))
        hbox0.Add(mul)
        mul.Bind(wx.EVT_BUTTON, self.OnClicked) 

        backspace = wx.Button(panel, label='del', size=(70, 30))
        hbox0.Add(backspace)
        backspace.Bind(wx.EVT_BUTTON, self.OnBackspace)

        #line 1
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)

        btn1 = wx.Button(panel, label='1', size=(70, 30))
        hbox1.Add(btn1)
        btn1.Bind(wx.EVT_BUTTON, self.OnClicked) 

        btn2 = wx.Button(panel, label='2', size=(70, 30))
        hbox1.Add(btn2)
        btn2.Bind(wx.EVT_BUTTON, self.OnClicked) 

        btn3 = wx.Button(panel, label='3', size=(70, 30))
        hbox1.Add(btn3)
        btn3.Bind(wx.EVT_BUTTON, self.OnClicked)
        
        eq = wx.Button(panel, label='=', size=(70, 30))
        hbox1.Add(eq)
        eq.Bind(wx.EVT_BUTTON, self.OnEqual) 

        #line 2
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)

        btn4 = wx.Button(panel, label='4', size=(70, 30))
        hbox2.Add(btn4)
        btn4.Bind(wx.EVT_BUTTON, self.OnClicked) 

        btn5 = wx.Button(panel, label='5', size=(70, 30))
        hbox2.Add(btn5)
        btn5.Bind(wx.EVT_BUTTON, self.OnClicked) 

        btn6 = wx.Button(panel, label='6', size=(70, 30))
        hbox2.Add(btn6)
        btn6.Bind(wx.EVT_BUTTON, self.OnClicked) 

        #line 3
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)

        btn7 = wx.Button(panel, label='7', size=(70, 30))
        hbox3.Add(btn7)
        btn7.Bind(wx.EVT_BUTTON, self.OnClicked) 

        btn8 = wx.Button(panel, label='8', size=(70, 30))
        hbox3.Add(btn8)
        btn8.Bind(wx.EVT_BUTTON, self.OnClicked) 

        btn9 = wx.Button(panel, label='9', size=(70, 30))
        hbox3.Add(btn9)
        btn9.Bind(wx.EVT_BUTTON, self.OnClicked) 

        #line output
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        self.txtbox = wx.TextCtrl ( panel, value = "", style = wx.TE_READONLY | wx.TE_CENTER )
        hbox4.Add(self.txtbox)

        # add button banks
        vbox.Add(hbox0, flag=wx.ALIGN_LEFT|wx.RIGHT, border=10)
        vbox.Add(hbox1, flag=wx.ALIGN_LEFT|wx.RIGHT, border=10)
        vbox.Add(hbox2, flag=wx.ALIGN_LEFT|wx.RIGHT, border=10)
        vbox.Add(hbox3, flag=wx.ALIGN_LEFT|wx.RIGHT, border=10)
        vbox.Add(hbox4, flag=wx.ALIGN_LEFT|wx.RIGHT, border=10)

        panel.SetSizer(vbox)

    #make list output useable
    def Tostring(self):
        if self.ls:
            st = str(self.ls)
            st = st.replace("'","").replace(",","").replace("[","").replace("]","").replace(" ","")
            return st
        else:
            return ""

    def Updatetxtbox(self, text):
        self.txtbox.ChangeValue(text)

    #On click of non eval and delete
    def OnClicked(self, event): 
        self.ls.append(event.GetEventObject().GetLabel())
        equ = self.Tostring()
        self.Updatetxtbox(equ)

    def OnBackspace(self, event):
        if self.ls:
            self.ls.pop()
        
        equ = self.Tostring()
        self.Updatetxtbox(equ)
    
    def OnEqual(self, event):
        equ = self.Tostring()
        ans = eval(equ)

        self.ls = [ans]
        self.Updatetxtbox(str(ans))


def main():
    app = wx.App()
    ex = calc(None, title='Calculator')
    ex.Show()
    app.MainLoop()
	

if __name__ == '__main__':
    main()