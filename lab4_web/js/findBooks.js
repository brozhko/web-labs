document.addEventListener('DOMContentLoaded', () => {
  const searchInput = document.getElementById('searchInput');
  const searchBtn = document.getElementById('btnSearch');
  const booksContainer = document.getElementById('libraryContainer');

  function filterBooks() {
    const query = searchInput.value.trim().toLowerCase();
    const allBooks = JSON.parse(localStorage.getItem('book_catalog_v1')) || [];

    const filtered = allBooks.filter(book =>
      book.name.toLowerCase().includes(query)
    );

    booksContainer.innerHTML = '';
    if (filtered.length === 0) {
      booksContainer.innerHTML = '<p style="text-align:center;">Нічого не знайдено 😢</p>';
      return;
    }

    filtered.forEach(book => {
      const card = document.createElement('div');
      card.className = 'card';
      card.innerHTML = `
        <img src="${book.image || 'img/book.jpg'}" alt="Обкладинка книги">
        <h2 class="title">${book.name}</h2>
        <p class="author">${book.author}</p>
        <p class="price"><span>${book.price}</span> грн</p>
        <button class="edit-btn" data-id="${book.id}">✏️ Редагувати</button>
      `;
      booksContainer.appendChild(card);
    });
  }

  searchBtn.addEventListener('click', filterBooks);
});
