import React from "react";
import styles from "./Hero.module.css";

function Hero() {
  return (
    <div className={styles.hero}>
      <div className={styles.leftBox}></div>

      <div className={styles.textBlock}>
        <h1 className={styles.title}>Книжки для натхнення</h1>
        <p className={styles.text}>
          Відкривайте класику, нон-фікшн і фантастику в одному місці. Добірки під різні настрої,
          швидкі прев'ю та зручний каталог для читачів у всьому світі.
        </p>
      </div>
    </div>
  );
}

export default Hero;
