from django import forms
from datetime import datetime

class PaymentForm(forms.Form):
    """
    A form used for payment information of a customer.

    Fields:
    - name (CharField): The name of the customer. Required.
    - street_name (CharField): The street name of the customer's address. Required.
    - house_number (CharField): The house number of the customer's address. Required.
    - city (CharField): The city of the customer's address. Required.
    - country (CharField): The country of the customer's address. Required.
    - postal_code (CharField): The postal code of the customer's address. Required.
    - payment_method (ChoiceField): The payment method for the order. Required.
    - card_number (CharField): The card number of the customer. Optional.
    - cardholder_name (CharField): The name on the card. Optional.
    - expiration_date (CharField): The expiration date of the card in MM/YY format. Optional.
    - cvc (CharField): The CVC code of the card. Optional.
    """
    name = forms.CharField(max_length=255, label='Name')
    street_name = forms.CharField(max_length=255, label='Street Name')
    house_number = forms.CharField(max_length=255, label='House Number')
    city = forms.CharField(max_length=255, label='City')
    country = forms.CharField(max_length=255, label='Country')
    postal_code = forms.CharField(max_length=255, label='Postal Code')
    payment_method = forms.ChoiceField(choices=[('pay-at-pickup', 'Pay at Pickup'), ('pay-with-card', 'Pay with Card')], widget=forms.RadioSelect)

    card_number = forms.CharField(max_length=16, label='Card Number', required=False)
    cardholder_name = forms.CharField(max_length=255, label='Cardholder Name', required=False)
    expiration_date = forms.CharField(max_length=5, label='Expiration Date (MM/YY)', required=False)
    cvc = forms.CharField(max_length=3, label='CVC', required=False)


    def clean_card_number(self):
        """
        Cleans and validates the card number.

        Returns:
        - card_number (str): The validated card number.

        Raises:
        - forms.ValidationError: If the card number is invalid.
        """
        card_number = self.cleaned_data['card_number']
        if card_number and (not card_number.isdigit() or len(card_number) != 16):
            raise forms.ValidationError("Invalid card number.")
        raise forms.ValidationError("Please fill in all the required fields.")


    def clean_cvc(self):
        """
        Cleans and validates the CVC code.

        Returns:
        - cvc (str): The validated CVC code.

        Raises:
        - forms.ValidationError: If the CVC code is invalid.
        """
        cvc = self.cleaned_data['cvc']
        if cvc and (not cvc.isdigit() or len(cvc) != 3):
            raise forms.ValidationError("Invalid CVC.")
        return cvc


    def clean_name(self):
        """
        Cleans and validates the name.

        Returns:
        - name (str): The validated name.

        Raises:
        - forms.ValidationError: If the name is invalid.
        """
        name = self.cleaned_data['name']
        if not name.replace(' ', '').isalpha():
            raise forms.ValidationError("Invalid name.")
        return name


    def clean_street_name(self):
        """
        Cleans and validates the street name.

        Returns:
        - street_name (str): The validated street name.

        Raises:
        - forms.ValidationError: If the street name is invalid.
        """
        street_name = self.cleaned_data['street_name']
        if not street_name.replace(' ', '').isalpha():
            raise forms.ValidationError("Invalid street name.")
        return street_name


    def clean_house_number(self):
        """
        Cleans and validates the house number.

        Returns:
        - house_number (str): The validated house number.
        
        Raises:
        - forms.ValidationError: If the house number is invalid.
        """
        house_number = self.cleaned_data['house_number']
        if not house_number.isdigit():
            raise forms.ValidationError("Invalid house number.")
        return house_number


    def clean_city(self):
        """
        Cleans and validates the city.

        Returns:
        - city (str): The validated city.

        Raises:
        - forms.ValidationError: If the city is invalid.
        """
        city = self.cleaned_data['city']
        if not city.replace(' ', '').isalpha():
            raise forms.ValidationError("Invalid city.")
        return city


    def clean_country(self):
        """
        Cleans and validates the country.

        Returns:
        - country (str): The validated country.

        Raises:
        - forms.ValidationError: If the country is invalid.
        """
        country = self.cleaned_data['country']
        if not country.replace(' ', '').isalpha():
            raise forms.ValidationError("Invalid country.")
        return country


    def clean_postal_code(self):
        """
        Cleans and validates the postal code.

        Returns:
        - postal_code (str): The validated postal code.

        Raises:
        - forms.ValidationError: If the postal code is invalid.
        """
        postal_code = self.cleaned_data['postal_code']
        if not postal_code.isalnum():
            raise forms.ValidationError("Invalid postal code.")
        return postal_code


    def clean_expiration_date(self):
        """
        Cleans and validates the expiration date.

        Returns:
        - expiration_date (str): The validated expiration date.

        Raises:
        - forms.ValidationError: If the expiration date is invalid.
        """
        expiration_date = self.cleaned_data['expiration_date']
        if expiration_date:
            try:
                datetime.strptime(expiration_date, '%m/%y')
            except ValueError:
                raise forms.ValidationError("Invalid expiration date. Use MM/YY format.")
        return expiration_date
    

