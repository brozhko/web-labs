import React from "react";
import ProductList from "../components/ProductList";
import Select from "../components/Select";
import styles from "./Catalog.module.css";

const categoryOptions = [
  { value: "all", label: "Всі категорії" },
  { value: "classic", label: "Класика" },
  { value: "modern", label: "Сучасна проза" },
  { value: "fantasy", label: "Фентезі" },
];

function Catalog() {
  return (
    <main className={styles.catalogPage}>
      <h1 className={styles.title}>Каталог книжок</h1>

      <div className={styles.filters}>
        <input
          type="text"
          placeholder="Пошук книги..."
          className={styles.searchInput}
        />

        <Select
          className={styles.sortSelect}
          options={categoryOptions}
          defaultValue="all"
        />
      </div>

      <ProductList />
    </main>
  );
}

export default Catalog;
