(function() {
  const STORAGE_KEY = 'book_catalog_v1';
  const form = document.getElementById('bookForm');
  const nameInput = document.getElementById('bookName');
  const authorInput = document.getElementById('bookAuthor');
  const priceInput = document.getElementById('bookPrice');
  const imageInput = document.getElementById('bookImage');

  form.addEventListener('submit', e => {
    e.preventDefault();

    const name = nameInput.value.trim();
    const author = authorInput.value.trim();
    const price = priceInput.value.trim();
    if (!name || !author || !price) return alert('Заповніть усі поля!');

    const books = JSON.parse(localStorage.getItem(STORAGE_KEY)) || [];
    const newBook = {
      id: Date.now().toString(),
      name,
      author,
      price
    };

    const file = (imageInput && imageInput.files && imageInput.files[0]) || null;
    if (file) {
      const reader = new FileReader();
      reader.onload = e => {
        newBook.image = e.target.result;
        books.push(newBook);
        localStorage.setItem(STORAGE_KEY, JSON.stringify(books));
        window.location.href = 'index.html';
      };
      reader.readAsDataURL(file);
    } else {
      newBook.image = 'img/book.jpg';
      books.push(newBook);
      localStorage.setItem(STORAGE_KEY, JSON.stringify(books));
      window.location.href = 'index.html';
    }
  });
})();
