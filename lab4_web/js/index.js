const STORAGE_KEY = 'book_catalog_v1';
let books = JSON.parse(localStorage.getItem(STORAGE_KEY)) || [];
const libraryContainer = document.getElementById('libraryContainer');

function saveBooks() {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(books));
}

function renderBooks() {
  libraryContainer.innerHTML = '';

  if (books.length === 0) {
    libraryContainer.innerHTML = '<p style="text-align:center;">Немає жодної книги. Додайте нову!</p>';
    return;
  }

  books.forEach(book => {
    const card = document.createElement('div');
    card.classList.add('card');
    card.innerHTML = `
      <img src="${book.image || 'img/book.jpg'}" alt="Обкладинка книги">
      <h2 class="title">${book.name}</h2>
      <p class="author">${book.author}</p>
      <p class="price"><span>${book.price}</span> грн</p>
      <button class="edit-btn" data-id="${book.id}">✏️ Редагувати</button>
    `;
    libraryContainer.appendChild(card);
  });

  document.querySelectorAll('.edit-btn').forEach(btn => {
    btn.addEventListener('click', e => {
      const id = e.target.dataset.id;
      const bookToEdit = books.find(b => b.id === id);
      localStorage.setItem('book_to_edit', JSON.stringify(bookToEdit));
      window.location.href = 'edit.html';
    });
  });
}

document.addEventListener('DOMContentLoaded', renderBooks);
