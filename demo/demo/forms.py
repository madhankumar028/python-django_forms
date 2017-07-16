from django import forms

class POAForm(forms.Form):
	first_name = forms.charField(label="YourName",
						error_messages={'required': 'Please enter your first_name'})
	phonenumber = forms.RegexField(regex=r'^\+?1?\d{9,15}$', 
                                error_message = ("Phone number must be entered in the format: '+999999999'.")
