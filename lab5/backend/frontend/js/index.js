const API_URL = 'http://localhost:5000/api/books';
let books = [];
const libraryContainer = document.getElementById('libraryContainer');

async function loadBooks() {
  try {
    const res = await fetch(API_URL);
    books = await res.json();
    renderBooks();
  } catch (err) {
    console.error('Помилка при завантаженні книг:', err);
    libraryContainer.innerHTML = '<p style="text-align:center;color:red;">⚠️ Не вдалося завантажити книги.</p>';
  }
}

function renderBooks(list = books) {
  libraryContainer.innerHTML = '';

  if (list.length === 0) {
    libraryContainer.innerHTML = '<p style="text-align:center;">Немає жодної книги. Додайте нову!</p>';
    return;
  }

  list.forEach(book => {
    const card = document.createElement('div');
    card.classList.add('card');
    card.innerHTML = `
      <img src="${book.image || 'img/book.jpg'}" alt="Обкладинка книги">
      <h2 class="title">${book.name}</h2>
      <p class="author">${book.author}</p>
      <p class="price"><span>${book.price}</span> грн</p>
      <button class="edit-btn" data-id="${book.id}">✏️ Редагувати</button>
      <button class="delete-btn" data-id="${book.id}">🗑️ Видалити</button>
    `;
    libraryContainer.appendChild(card);
  });

  // редагування
  document.querySelectorAll('.edit-btn').forEach(btn => {
    btn.addEventListener('click', e => {
      const id = e.target.dataset.id;
      const bookToEdit = books.find(b => b.id === id);
      localStorage.setItem('book_to_edit', JSON.stringify(bookToEdit));
      window.location.href = 'edit.html';
    });
  });

  // видалення
  document.querySelectorAll('.delete-btn').forEach(btn => {
    btn.addEventListener('click', async e => {
      const id = e.target.dataset.id;
      if (confirm('Видалити книгу?')) {
        await fetch(`${API_URL}/${id}`, { method: 'DELETE' });
        loadBooks();
      }
    });
  });
}

document.addEventListener('DOMContentLoaded', loadBooks);

