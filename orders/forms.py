from django import forms

class PaymentForm(forms.Form):
    name = forms.CharField(max_length=255, label='Name')
    street_name = forms.CharField(max_length=255, label='Street Name')
    house_number = forms.CharField(max_length=255, label='House Number')
    city = forms.CharField(max_length=255, label='City')
    country = forms.CharField(max_length=255, label='Country')
    postal_code = forms.CharField(max_length=255, label='Postal Code')
    payment_method = forms.ChoiceField(choices=[('pay-at-pickup', 'Pay at Pickup'), ('pay-with-card', 'Pay with Card')], widget=forms.RadioSelect)

    card_number = forms.CharField(max_length=16, label='Card Number', required=False)
    cardholder_name = forms.CharField(max_length=255, label='Cardholder Name', required=False)
    expiration_date = forms.DateField(label='Expiration Date', required=False)
    cvc = forms.CharField(max_length=3, label='CVC', required=False)

    def clean_card_number(self):
        card_number = self.cleaned_data['card_number']
        if card_number and (not card_number.isdigit() or len(card_number) != 16):
            raise forms.ValidationError("Invalid card number.")
        return card_number

    def clean_cvc(self):
        cvc = self.cleaned_data['cvc']
        if cvc and (not cvc.isdigit() or len(cvc) != 3):
            raise forms.ValidationError("Invalid CVC.")
        return cvc

    def clean_name(self):
        name = self.cleaned_data['name']
        if not name.replace(' ', '').isalpha():
            raise forms.ValidationError("Invalid name.")
        return name

    def clean_street_name(self):
        street_name = self.cleaned_data['street_name']
        if not street_name.replace(' ', '').isalpha():
            raise forms.ValidationError("Invalid street name.")
        return street_name

    def clean_house_number(self):
        house_number = self.cleaned_data['house_number']
        if not house_number.isdigit():
            raise forms.ValidationError("Invalid house number.")
        return house_number

    def clean_city(self):
        city = self.cleaned_data['city']
        if not city.replace(' ', '').isalpha():
            raise forms.ValidationError("Invalid city.")
        return city

    def clean_country(self):
        country = self.cleaned_data['country']
        if not country.replace(' ', '').isalpha():
            raise forms.ValidationError("Invalid country.")
        return country

    def clean_postal_code(self):
        postal_code = self.cleaned_data['postal_code']
        if not postal_code.isalnum():
            raise forms.ValidationError("Invalid postal code.")
        return postal_code
