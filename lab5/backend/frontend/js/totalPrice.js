document.getElementById('btnTotal').addEventListener('click', async () => {
  const API_URL = 'http://localhost:5000/api/books';
  const res = await fetch(API_URL);
  const books = await res.json();
  const total = books.reduce((sum, b) => sum + Number(b.price), 0);
  document.getElementById('sumOutput').textContent = `${total} грн`;
});
