  // Hide/show forms based on product type
  const pizzaForm = document.querySelector(".pizza-form");
  const sideDrinksForm = document.querySelector(".sideDrinks-form");
  if ("{{ product.type|lower }}" === "pizza") {
    sideDrinksForm.style.display = "none";
  } else {
    pizzaForm.style.display = "none";
  }

  function updateFormAction(size) {
    const form = document.getElementById("add-to-cart-form");
    form.action = '{% url "add_to_cart" product.id %}?size=' + size;
  }