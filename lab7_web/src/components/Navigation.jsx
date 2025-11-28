import React from "react";
import { NavLink } from "react-router-dom";
import styles from "./Navigation.module.css";

const buildLinkClass = ({ isActive }) =>
  isActive ? `${styles.link} ${styles.active}` : styles.link;

function Navigation() {
  return (
    <header className={styles.navbar}>
      <div className={styles.logo}>UA Books</div>

      <nav className={styles.links}>
        <NavLink to="/" className={buildLinkClass}>
          Головна
        </NavLink>
        <NavLink to="/catalog" className={buildLinkClass}>
          Каталог
        </NavLink>
        <button className={styles.cta}>Увійти</button>
      </nav>
    </header>
  );
}

export default Navigation;
