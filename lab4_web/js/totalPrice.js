document.getElementById('btnTotal').addEventListener('click', () => {
  const books = JSON.parse(localStorage.getItem('book_catalog_v1')) || [];
  const total = books.reduce((sum, book) => sum + Number(book.price), 0);
  document.getElementById('sumOutput').textContent = total;
});
