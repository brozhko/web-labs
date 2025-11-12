(function() {
  const API_URL = 'http://localhost:5000/api/books';
  const form = document.getElementById('bookForm');
  const nameInput = document.getElementById('bookName');
  const authorInput = document.getElementById('bookAuthor');
  const priceInput = document.getElementById('bookPrice');

  form.addEventListener('submit', async e => {
    e.preventDefault(); // щоб сторінка не перезавантажувалась

    const name = nameInput.value.trim();
    const author = authorInput.value.trim();
    const price = priceInput.value.trim();

    if (!name || !author || !price) {
      return alert('Заповніть усі поля!');
    }

    const newBook = { name, author, price };

    try {
      const response = await fetch(API_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(newBook),
      });

      if (response.ok) {
        alert('✅ Книгу успішно додано!');
        form.reset();
        window.location.href = 'index.html';
      } else {
        alert('❌ Помилка при додаванні книги.');
      }
    } catch (error) {
      console.error('Помилка при збереженні книги:', error);
      alert('⚠️ Сталася помилка при збереженні.');
    }
  });
})();
