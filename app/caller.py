
import wx
from scrapers.profile.igramscraper.instagram import Instagram
from preprocess_data import *
from time import sleep

class Example(wx.Frame):

    

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        self.InitUI()
        self.Centre()

    def InitUI(self):

        panel = wx.Panel(self)

        font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)

        font.SetPointSize(9)

        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(panel, label='Username')
        st1.SetFont(font)
        hbox1.Add(st1, flag=wx.RIGHT, border=8)
        tc = wx.TextCtrl(panel)
        hbox1.Add(tc, proportion=1)
        vbox.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)


        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        st2 = wx.StaticText(panel, label='Profile Data:')
        st2.SetFont(font)
        hbox2.Add(st2)
        vbox.Add(hbox2, flag=wx.LEFT | wx.TOP, border=10)

        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        prf = wx.StaticText(panel, label='Profile Pic:')
        prfc = wx.StaticText(panel, label='-')        
        hbox3.Add(prf, proportion=1, flag=wx.EXPAND)
        hbox3.Add(prfc, proportion=1, flag=wx.EXPAND)

        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        bio = wx.StaticText(panel, label='Biograpy Length:')
        bioc = wx.StaticText(panel, label='-')        
        hbox4.Add(bio, proportion=1, flag=wx.EXPAND)
        hbox4.Add(bioc, proportion=1, flag=wx.EXPAND)
        
        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        flw = wx.StaticText(panel, label='Follow:')
        flwc = wx.StaticText(panel, label='-')        
        hbox5.Add(flw, proportion=1, flag=wx.EXPAND)
        hbox5.Add(flwc, proportion=1, flag=wx.EXPAND)

        hbox6 = wx.BoxSizer(wx.HORIZONTAL)
        fld = wx.StaticText(panel, label='Followed By:')
        fldc = wx.StaticText(panel, label='-')        
        hbox6.Add(fld, proportion=1, flag=wx.EXPAND)
        hbox6.Add(fldc, proportion=1, flag=wx.EXPAND)

        hbox7 = wx.BoxSizer(wx.HORIZONTAL)
        md = wx.StaticText(panel, label='Medias:')
        mdc = wx.StaticText(panel, label='-')        
        hbox7.Add(md, proportion=1, flag=wx.EXPAND)
        hbox7.Add(mdc, proportion=1, flag=wx.EXPAND)

        hbox8 = wx.BoxSizer(wx.HORIZONTAL)
        prv = wx.StaticText(panel, label='Private:')
        prvc = wx.StaticText(panel, label='-')        
        hbox8.Add(prv, proportion=1, flag=wx.EXPAND)
        hbox8.Add(prvc, proportion=1, flag=wx.EXPAND)

        hbox9 = wx.BoxSizer(wx.HORIZONTAL)
        rea = wx.StaticText(panel, label='Real:')
        reac = wx.StaticText(panel, label='-')        
        hbox9.Add(rea, proportion=1, flag=wx.EXPAND)
        hbox9.Add(reac, proportion=1, flag=wx.EXPAND)





        vbox.Add(hbox3, proportion=1, flag=wx.LEFT|wx.RIGHT|wx.EXPAND, border=10)
        vbox.Add(hbox4, proportion=1, flag=wx.LEFT|wx.RIGHT|wx.EXPAND, border=10)
        vbox.Add(hbox5, proportion=1, flag=wx.LEFT|wx.RIGHT|wx.EXPAND, border=10)
        vbox.Add(hbox6, proportion=1, flag=wx.LEFT|wx.RIGHT|wx.EXPAND, border=10)
        vbox.Add(hbox7, proportion=1, flag=wx.LEFT|wx.RIGHT|wx.EXPAND, border=10)
        vbox.Add(hbox8, proportion=1, flag=wx.LEFT|wx.RIGHT|wx.EXPAND, border=10)
        vbox.Add(hbox9, proportion=1, flag=wx.LEFT|wx.RIGHT|wx.EXPAND, border=10)

        
             
        ButtonBox = wx.BoxSizer(wx.HORIZONTAL)
        btn1 = wx.Button(panel, label='Ok', size=(70, 30))
        ButtonBox.Add(btn1)
        self.Bind(wx.EVT_BUTTON, lambda event: self.OnClicked(event, tc, prfc, bioc, flwc, fldc, mdc, prvc, reac), btn1)
        #btn1.Bind(wx.EVT_BUTTON,self.OnClicked)
        btn2 = wx.Button(panel, label='Close', size=(70, 30))
        ButtonBox.Add(btn2, flag=wx.LEFT|wx.BOTTOM, border=5)
        vbox.Add(ButtonBox, flag=wx.ALIGN_RIGHT|wx.RIGHT, border=10)

        panel.SetSizer(vbox)

    def OnClicked(self, event, tc, prfc, bioc, flwc, fldc, mdc, prvc, reac):
        username = tc.Value
        instagram = Instagram()
        instagram.with_credentials('donatella.marchese.7', 'vietatofumare')
        instagram.login()
        sleep(2) # Delay to mimic user
        account = instagram.get_account(username)    
        ProfileData = account.__dict__
        # sleep(2)
        # medias = instagram.get_medias(username, 25)
        # for media in medias:
        #     print(media)
        # item = GenerateData(ProfileData)
        emptyPicURL="44884218_345707102882519_2446069589734326272_n.jpg"
        pic = "False" if emptyPicURL in ProfileData['profile_pic_url'] else "True"
    
        prfc.SetLabel(pic)
        bioc.SetLabel("0" if ProfileData["biography"] == "" else str(len(ProfileData["biography"])))
        flwc.SetLabel(str(ProfileData['follows_count']))
        fldc.SetLabel(str(ProfileData['followed_by_count']))
        mdc.SetLabel(str(ProfileData['media_count']))
        prvc.SetLabel(str(ProfileData['is_private']))
        reac.SetLabel("???")
        #self.sizer.Layout()



def main():
    
    app = wx.App()
    ex = Example(None, title='Instagram Profile Checker')
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()

