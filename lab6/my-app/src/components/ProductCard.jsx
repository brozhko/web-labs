import React from "react";
import cardPlaceholder from "../assets/book-placeholder.svg";
import styles from "./ProductCard.module.css";

function ProductCard({ title, author, description }) {
  return (
    <div className={styles.card}>
      <img className={styles.image} src={cardPlaceholder} alt={title} />

      <h3 className={styles.cardTitle}>{title}</h3>
      <p className={styles.author}>{author}</p>

      <p className={styles.desc}>{description}</p>
    </div>
  );
}

export default ProductCard;
