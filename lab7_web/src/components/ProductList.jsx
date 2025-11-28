// src/components/ProductList.jsx
import React from "react";
import ProductCard from "./ProductCard";
import PrimaryButton from "./PrimaryButton";
import styles from "./ProductList.module.css";
import booksCover from "../assets/books.jpg";

const products = [
  {
    id: 1,
    title: "Майстер і Маргарита",
    author: "Михайло Булгаков",
    price: 320,
    cover: booksCover,
  },
  {
    id: 2,
    title: "1984",
    author: "Джордж Орвелл",
    price: 290,
    cover: booksCover,
  },
  {
    id: 3,
    title: "Три товариші",
    author: "Еріх Марія Ремарк",
    price: 310,
    cover: booksCover,
  },
  {
    id: 4,
    title: "Гра престолів",
    author: "Джордж Мартін",
    price: 450,
    cover: booksCover,
  },
  {
    id: 5,
    title: "Дюна",
    author: "Френк Герберт",
    price: 380,
    cover: booksCover,
  },
  {
    id: 6,
    title: "Кобзар",
    author: "Тарас Шевченко",
    price: 250,
    cover: booksCover,
  },
  {
    id: 7,
    title: "Пікнік на узбіччі",
    author: "Аркадій і Борис Стругацькі",
    price: 270,
    cover: booksCover,
  },
  {
    id: 8,
    title: "451° за Фаренгейтом",
    author: "Рей Бредбері",
    price: 260,
    cover: booksCover,
  },
];

function ProductList({ limit, showViewMore }) {
  const items = limit ? products.slice(0, limit) : products;

  return (
    <section className={styles.wrapper}>
      <div className={styles.list}>
        {items.map((item) => (
          <ProductCard key={item.id} {...item} />
        ))}
      </div>
      {showViewMore && (
        <div className={styles.viewMoreWrapper}>
          <PrimaryButton>View more</PrimaryButton>
        </div>
      )}
    </section>
  );
}

export default ProductList;
