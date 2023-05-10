
const searchButton = document.getElementById('search-button');
const clearButton = document.getElementById('clear-button');
const searchInput = document.querySelector('.search-form input');

const filterButton = document.getElementById('filter-button');
const clearFilterButton = document.getElementById('clear-filter-button');
const typeSelect = document.getElementById('type');

searchButton.addEventListener('click', () => {
clearButton.style.display = 'inline-block';
searchButton.style.display = 'none';
});

clearButton.addEventListener('click', () => {
searchInput.value = '';
clearButton.style.display = 'none';
searchButton.style.display = 'inline-block';
});

if (!searchInput.value) {
clearButton.style.display = 'none';
searchButton.style.display = 'inline-block';
} else {
clearButton.style.display = 'inline-block';
searchButton.style.display = 'none';
}

filterButton.addEventListener('click', () => {
clearFilterButton.style.display = 'inline-block';
filterButton.style.display = 'none';
});

clearFilterButton.addEventListener('click', () => {
typeSelect.value = '';
clearFilterButton.style.display = 'none';
filterButton.style.display = 'inline-block';
});

if (!typeSelect.value) {
clearFilterButton.style.display = 'none';
filterButton.style.display = 'inline-block';
} else {
clearFilterButton.style.display = 'inline-block';
filterButton.style.display = 'none';
}

