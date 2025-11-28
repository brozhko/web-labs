// src/components/ProductCard.jsx
import React from "react";
import styles from "./ProductCard.module.css";
import PrimaryButton from "./PrimaryButton";

function ProductCard({ title, author, price, cover }) {
  return (
    <article className={styles.card}>
      <div className={styles.imageWrapper}>
        <img src={cover} alt={title} className={styles.image} />
      </div>

      <div className={styles.content}>
        <h3 className={styles.title}>{title}</h3>
        <p className={styles.author}>{author}</p>
        <p className={styles.price}>{price} грн</p>

        <PrimaryButton>Додати</PrimaryButton>
      </div>
    </article>
  );
}

export default ProductCard;
