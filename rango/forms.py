from django import forms


class ContactForm(forms.Form):
	name=forms.CharField()
	email = forms.EmailField(required=False , label="your email adress")
   	message = forms.CharField(widget=forms.Textarea)

	def clean_message(self):
		message=self.cleaned_data['message']
		num_words=len(message.split())
	
		if num_words < 4:
			raise forms.ValidationError("Not enough words!")
		return message
	def clean_name(self):
		name=self.cleaned_data['name']
		num_letters=len(list(name))
		if num_letters < 3:
			raise forms.ValidationError("name correctly")

		return name


class LoginForm(forms.Form):
	username=forms.CharField()
	password=forms.CharField(widget=forms.PasswordInput())


class SearchForm(forms.Form):
	search=forms.CharField()	
