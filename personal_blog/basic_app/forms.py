from django import forms

class FormName(forms.Form):
    IP_Address_Block = forms.CharField()
    Number_of_host_per_subnet = forms.CharField()
    #text = forms.CharField(widget=forms.Textarea)

class FormName1(forms.Form):
    Date_and_Time = forms.CharField()
    Given_Time_zone = forms.CharField()
    New_Time_zone = forms.CharField()

class FormName2(forms.Form):
    cost = forms.CharField()
    money = forms.CharField()

class FormName3(forms.Form):
    Binary_value = forms.CharField()

class FormName4(forms.Form):
    Decimal_value = forms.CharField()

class FormName5(forms.Form):
    IPv4_Address = forms.CharField()
