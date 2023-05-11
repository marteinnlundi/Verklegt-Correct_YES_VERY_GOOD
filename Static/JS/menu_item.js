const pizzaForm = document.querySelector('.pizza-form');
const sideDrinksForm = document.querySelector('.sideDrinks-form');
if ('{{ product.type|lower }}' === 'pizza') {
  sideDrinksForm.style.display = 'none';
} else {
  pizzaForm.style.display = 'none';
}