(function() {
  const searchInput = document.getElementById('searchInput');
  if (!searchInput) return;

  // Filter the globally-loaded books and reuse the shared renderer
  searchInput.addEventListener('input', () => {
    const query = searchInput.value.trim().toLowerCase();
    const filtered = books.filter(b =>
      b.name.toLowerCase().includes(query) ||
      b.author.toLowerCase().includes(query)
    );
    renderBooks(filtered);
  });
})();
