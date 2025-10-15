const books = [
    { title: 'Кобзар', author: 'Тарас Шевченко', price: 120 },
    { title: 'Лісова пісня', author: 'Леся Українка', price: 150 },
    { title: 'Тіні забутих предків', author: 'Михайло Коцюбинський', price: 130 },
    { title: 'Захар Беркут', author: 'Іван Франко', price: 140 },
    { title: 'Тигролови', author: 'Іван Багряний', price: 160 },
];

let filteredBooks = [...books];

function renderBooks() {
    const container = document.getElementById('booksContainer');
    container.innerHTML = '';

    let displayBooks = [...filteredBooks];
    const sortToggle = document.getElementById('sortToggle').checked;
    if (sortToggle) {
        displayBooks.sort((a, b) => b.price - a.price);
    }

        displayBooks.forEach(book => {
                const imageUrl = `images/book${books.indexOf(book) + 1}.jpg`;
                const card = `
<div class="card">
    <img src="${imageUrl}" alt="Обкладинка книги ${book.title}" loading="lazy">
    <div class="body">
        <h3>${book.title}</h3>
        <p>Автор: ${book.author}</p>
        <div class="price"><span class="muted">Ціна</span><span class="badge">₴${book.price}</span></div>
    </div>
</div>
`;
                container.insertAdjacentHTML('beforeend', card);
        });
}

function searchBooks() {
    const query = document.getElementById('searchInput').value.toLowerCase();
    filteredBooks = books.filter(b => b.title.toLowerCase().includes(query) || b.author.toLowerCase().includes(query));
    renderBooks();
}

function clearSearchBooks() {
    document.getElementById('searchInput').value = '';
    filteredBooks = [...books];
    renderBooks();
}

function countTotalPrice() {
    const total = filteredBooks.reduce((sum, b) => sum + b.price, 0);
    document.getElementById('totalExpenses').textContent = total;
}

renderBooks();
