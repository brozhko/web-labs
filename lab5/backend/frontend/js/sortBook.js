document.getElementById('btnSort').addEventListener('click', () => {
  const sorted = [...books].sort((a, b) => Number(a.price) - Number(b.price));
  renderBooks(sorted);
});

