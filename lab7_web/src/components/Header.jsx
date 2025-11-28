import React from "react";
import styles from "./Header.module.css";
import { NavLink } from "react-router-dom";

const navClass = ({ isActive }) =>
  isActive ? `${styles.navLink} ${styles.active}` : styles.navLink;

function Header() {
  return (
    <header className={styles.header}>
      <div className={styles.logo}>UA Books</div>

      <nav className={styles.nav}>
        <NavLink to="/" className={navClass}>
          Головна
        </NavLink>
        <NavLink to="/catalog" className={navClass}>
          Каталог
        </NavLink>
        <NavLink to="/cart" className={navClass}>
          Кошик
        </NavLink>
      </nav>
    </header>
  );
}

export default Header;
