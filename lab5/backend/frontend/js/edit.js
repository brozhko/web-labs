(function() {
  const API_URL = 'http://localhost:5000/api/books';
  const form = document.getElementById('editForm');
  const idInput = document.getElementById('bookId');
  const nameInput = document.getElementById('bookName');
  const authorInput = document.getElementById('bookAuthor');
  const priceInput = document.getElementById('bookPrice');

  // Отримуємо дані про книгу з localStorage
  const bookToEdit = JSON.parse(localStorage.getItem('book_to_edit'));
  if (!bookToEdit) {
    alert('Книга для редагування не знайдена!');
    window.location.href = 'index.html';
    return;
  }

  // Заповнюємо форму
  idInput.value = bookToEdit.id;
  nameInput.value = bookToEdit.name;
  authorInput.value = bookToEdit.author;
  priceInput.value = bookToEdit.price;

  // Обробник форми
  form.addEventListener('submit', async e => {
    e.preventDefault();

    const updatedBook = {
      name: nameInput.value.trim(),
      author: authorInput.value.trim(),
      price: priceInput.value.trim()
    };

    try {
      const response = await fetch(`${API_URL}/${idInput.value}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(updatedBook)
      });

      if (response.ok) {
        alert('✅ Книгу оновлено успішно!');
        localStorage.removeItem('book_to_edit');
        window.location.href = 'index.html';
      } else {
        alert('❌ Помилка при оновленні книги.');
      }
    } catch (err) {
      console.error('Помилка оновлення книги:', err);
      alert('⚠️ Сталася помилка при оновленні.');
    }
  });
})();
