let dataPizzaItems = [
  {name: "The Green Monster", description: " Spinach, roasted garlic, artichoke hearts, sliced mushrooms, sliced red onion, and mozzarella cheese on a whole wheat crust. (Vegetarian, Vegan, Gluten-Free)"},
  {name: "The Big Kahuna", description: "Grilled pineapple, smoked ham, red onion, and mozzarella cheese on a tomato sauce base. (Vegetarian option: substitute ham with grilled tofu) (Vegan option: substitute cheese with vegan cheese) (Gluten-Free)"},
  {name: "The Garden of Eden", description: "Roasted red pepper, sliced zucchini, caramelized onion, black olives, fresh basil, and mozzarella cheese on a tomato sauce base. (Vegetarian, Vegan option: substitute cheese with vegan cheese) (Gluten-Free)"},
  {name: "The Meat Lovers", description: "Pepperoni, Italian sausage, bacon, ground beef, and mozzarella cheese on a tomato sauce base. (Vegetarian option: substitute meat with Impossible Meat) (Vegan option: substitute meat with vegan meat, substitute cheese with vegan cheese) (Gluten-Free)"},
  {name: "The Margherita", description: "Fresh mozzarella cheese, sliced roma tomatoes, and fresh basil on a tomato sauce base. (Vegetarian, Vegan option: substitute cheese with vegan cheese) (Gluten-Free)"},
  {name: "The BBQ Chicken", description: "Grilled chicken, red onion, and mozzarella cheese on a BBQ sauce base. (Vegetarian option: substitute chicken with grilled tofu) (Vegan option: substitute chicken with vegan chicken, substitute cheese with vegan cheese) (Gluten-Free)"},
];

let dataKidsPizzaItems = [
  {name: "The Cheese", description: "Mozzarella cheese on a tomato sauce base. (Vegetarian, Vegan option: substitute cheese with vegan cheese) (Gluten-Free)"},  
  {name: "Chicken Nuggets", description: "Breaded and fried chicken nuggets served with a side of ketchup or ranch dressing. (Gluten-Free option: substitute breading with gluten-free breading)"},
  {name: "Grilled Cheese Sandwich", description: "Melted cheddar cheese on toasted bread. (Vegetarian option: substitute cheese with vegan cheese) (Gluten-Free option: substitute bread with gluten-free bread)"},   
];

let dataSideItems = [
  {name: "Cheese Pizza", description: "Mozzarella cheese on a tomato sauce base. (Vegetarian, Vegan option: substitute cheese with vegan cheese) (Gluten-Free)"},
  {name: "Onion Rings", description: "Breaded and fried onion rings served with a side of ranch dressing. (Vegetarian, Vegan option: substitute ranch with vegan dressing) (Gluten-Free option: substitute breading with gluten-free breading)"},
  {name: "Sweet Potato Fries", description: "Baked sweet potato fries seasoned with sea salt and black pepper. (Vegetarian, Vegan, Gluten-Free)"},
  {name: "French Fries", description: "Baked french fries seasoned with sea salt and black pepper. (Vegetarian, Vegan, Gluten-Free)"},
];

let dataSaladItems = [
{name: "The Caesar", description: "Romaine lettuce, parmesan cheese, croutons, and Caesar dressing. (Vegetarian option: substitute parmesan with vegan cheese) (Gluten-Free option: substitute croutons with gluten-free croutons)"},
{name: "The Garden", description: "Mixed greens, cherry tomatoes, cucumbers, red onions, and balsamic vinaigrette. (Vegetarian, Vegan option: substitute dressing with vegan dressing) (Gluten-Free)"},
];

let dataDrinksItems = [
{name: "Coca-Cola", description: "Soft drink"},
{name: "Sprite", description: "Soft drink"},
{name: "Fanta", description: "Soft drink"},
{name: "Iced tea", description: "tea"},
{name: "Lemonade", description: "Soft drink"},
{name: "Bear", description: "Alcoholic drink"},
{name: "Wine", description: "Alcoholic drink"},
];

function createItems(dataArray, parentElement) {
dataArray.forEach((item) => {
  let div = document.createElement("div");
  div.classList.add("item");

  let name = document.createElement("div");
  name.classList.add("name");
  name.innerText = item.name;
  div.appendChild(name);

  let description = document.createElement("div");
  description.classList.add("description");
  description.innerText = item.description;
  div.appendChild(description);

  parentElement.appendChild(div);
});
}

createItems(dataPizzaItems, document.getElementById("pizzaItems"));
createItems(dataKidsPizzaItems, document.getElementById("kidsPizzaItems"));
createItems(dataSideItems, document.getElementById("sidesItems"));
createItems(dataDrinksItems, document.getElementById("drinksItems"));

const f = document.getElementById('form');
const q = document.getElementById('query');
const google = 'https://www.google.com/search?q=site%3A+';
const site = 'pagedart.com';

function submitted(event) {
event.preventDefault();
const url = google + site + '+' + q.value;
const win = window.open(url, '_blank');
win.focus();
}

f.addEventListener('submit', submitted);

