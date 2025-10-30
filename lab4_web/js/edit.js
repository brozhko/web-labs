(function() {
  const STORAGE_KEY = 'book_catalog_v1';
  const form = document.getElementById('editForm');
  const idInput = document.getElementById('bookId');
  const nameInput = document.getElementById('bookName');
  const authorInput = document.getElementById('bookAuthor');
  const priceInput = document.getElementById('bookPrice');
  const imageInput = document.getElementById('bookImage');

  const bookToEdit = JSON.parse(localStorage.getItem('book_to_edit'));
  if (!bookToEdit) {
    alert('Книга не вибрана для редагування!');
    window.location.href = 'index.html';
    return;
  }

  idInput.value = bookToEdit.id;
  nameInput.value = bookToEdit.name;
  authorInput.value = bookToEdit.author;
  priceInput.value = bookToEdit.price;

  form.addEventListener('submit', e => {
    e.preventDefault();
    const books = JSON.parse(localStorage.getItem(STORAGE_KEY)) || [];
    const index = books.findIndex(b => b.id === idInput.value);
    if (index === -1) return;

    books[index].name = nameInput.value.trim();
    books[index].author = authorInput.value.trim();
    books[index].price = priceInput.value.trim();

    const file = (imageInput && imageInput.files && imageInput.files[0]) || null;
    if (file) {
      const reader = new FileReader();
      reader.onload = e => {
        books[index].image = e.target.result;
        localStorage.setItem(STORAGE_KEY, JSON.stringify(books));
        window.location.href = 'index.html';
      };
      reader.readAsDataURL(file);
    } else {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(books));
      window.location.href = 'index.html';
    }
  });
})();
