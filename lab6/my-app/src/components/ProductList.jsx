import React from "react";
import ProductCard from "./ProductCard";
import styles from "./ProductList.module.css";

function ProductList() {
  const items = [
    {
      title: "Класика та поезія",
      author: "Збірки Шевченка, Франка, Українки",
      description:
        "Основи української ідентичності: поезія, яку варто перечитувати і передавати далі.",
    },
    {
      title: "Сучасна проза",
      author: "Забужко, Андрухович, Жадан",
      description:
        "Голоси сьогодення про місто, війну, свободу й щоденні історії, що формують наше завтра.",
    },
    {
      title: "Дитяча та підліткова",
      author: "Казки й пригоди українською",
      description:
        "Книжки, що виховують любов до мови з дитинства: яскраві ілюстрації, прості сюжети й теплі герої.",
    },
  ];

  return (
    <div className={styles.wrapper}>
      <div className={styles.cards}>
        {items.map((item) => (
          <ProductCard
            key={item.title}
            title={item.title}
            author={item.author}
            description={item.description}
          />
        ))}
      </div>

      <button className={styles.viewBtn}>Дивитися більше</button>
    </div>
  );
}

export default ProductList;
