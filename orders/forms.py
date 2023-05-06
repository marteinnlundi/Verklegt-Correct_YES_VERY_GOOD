from django import forms

class PaymentForm(forms.Form):
    card_number = forms.CharField(max_length=16, label='Card Number', required=False)
    cardholder_name = forms.CharField(max_length=255, label='Cardholder Name', required=False)
    expiration_date = forms.DateField(label='Expiration Date', required=False)
    cvc = forms.CharField(max_length=3, label='CVC', required=False)
    name = forms.CharField(max_length=255, label='Name', required=False)
    address = forms.CharField(max_length=255, label='Address', required=False)
    street_number = forms.CharField(max_length=255, label='Street Number', required=False)
    city = forms.CharField(max_length=255, label='City', required=False)
    postal_code = forms.CharField(max_length=255, label='Postal Code', required=False)


    def clean_card_number(self):
        card_number = self.cleaned_data['card_number']
        if not card_number.isdigit() or len(card_number) != 16:
            raise forms.ValidationError("Invalid card number.")
        return card_number

    def clean_cvc(self):
        cvc = self.cleaned_data['cvc']
        if not cvc.isdigit() or len(cvc) != 3:
            raise forms.ValidationError("Invalid CVC.")
        return cvc

    def clean_name(self):
        name = self.cleaned_data['name']
        if not name.replace(' ', '').isalpha():
            raise forms.ValidationError("Invalid name.")
        return name

    def clean_address(self):
        address = self.cleaned_data['address']
        if not address.replace(' ', '').isalnum():
            raise forms.ValidationError("Invalid address.")
        return address

    def clean_street_number(self):
        street_number = self.cleaned_data['street_number']
        if not street_number.isdigit():
            raise forms.ValidationError("Invalid street number.")
        return street_number

    def clean_city(self):
        city = self.cleaned_data['city']
        if not city.replace(' ', '').isalpha():
            raise forms.ValidationError("Invalid city.")
        return city

    def clean_postal_code(self):
        postal_code = self.cleaned_data['postal_code']
        if not postal_code.isalnum():
            raise forms.ValidationError("Invalid postal code.")
        return postal_code
