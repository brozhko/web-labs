const express = require('express');
const cors = require('cors');
const app = express();
const PORT = 5000;

app.use(cors());
app.use(express.json({ limit: '10mb' }));

// --- Тимчасова база даних книг ---
let books = [
  {
    id: "1",
    name: "Тіні забутих предків",
    author: "Михайло Коцюбинський",
    price: "250",
    image: null
  }
];

// --- CRUD ОПЕРАЦІЇ ---

// READ — усі книги
app.get('/api/books', (req, res) => {
  console.log('GET /api/books - all books');
  res.json(books);
});

// READ — одна книга
app.get('/api/books/:id', (req, res) => {
  const { id } = req.params;
  const book = books.find(b => b.id === id);
  if (book) {
    console.log(`GET /api/books/${id} - found book: ${book.name}`);
    res.json(book);
  } else {
    res.status(404).json({ message: 'Book not found' });
  }
});

// CREATE — додати книгу
app.post('/api/books', (req, res) => {
  const newBook = {
    id: Date.now().toString(),
    ...req.body
  };
  books.push(newBook);
  console.log('POST /api/books - added:', newBook.name);
  res.status(201).json(newBook);
});

// UPDATE — оновити книгу
app.put('/api/books/:id', (req, res) => {
  const { id } = req.params;
  const index = books.findIndex(b => b.id === id);
  if (index === -1) {
    return res.status(404).json({ message: 'Book not found' });
  }

  books[index] = { ...books[index], ...req.body };
  console.log(`PUT /api/books/${id} - updated: ${books[index].name}`);
  res.json(books[index]);
});

// DELETE — видалити книгу
app.delete('/api/books/:id', (req, res) => {
  const { id } = req.params;
  const exists = books.some(b => b.id === id);
  if (!exists) {
    return res.status(404).json({ message: 'Book not found' });
  }

  books = books.filter(b => b.id !== id);
  console.log(`DELETE /api/books/${id} - deleted`);
  res.status(204).send();
});

// --- Запуск ---
app.listen(PORT, () => {
  console.log(`✅ Server running on http://localhost:${PORT}`);
});
