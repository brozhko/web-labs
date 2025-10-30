document.getElementById('btnSort').addEventListener('click', () => {
  const books = JSON.parse(localStorage.getItem('book_catalog_v1')) || [];
  books.sort((a, b) => a.price - b.price);
  localStorage.setItem('book_catalog_v1', JSON.stringify(books));
  window.location.reload();
});
