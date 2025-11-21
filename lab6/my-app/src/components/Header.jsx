import React from "react";
import styles from "./Header.module.css";
import { NavLink } from "react-router-dom";

function Header() {
    return (
        <header className={styles.header}>
            <div className={styles.logo}>UA Books</div>

            <nav className={styles.nav}>
                <NavLink
                    to="/"
                    className={({ isActive }) =>
                        isActive ? `${styles.navLink} ${styles.active}` : styles.navLink
                    }
                >
                    Головна
                </NavLink>

                <NavLink
                    to="/catalog"
                    className={({ isActive }) =>
                        isActive ? `${styles.navLink} ${styles.active}` : styles.navLink
                    }
                >
                    Каталог
                </NavLink>

                <NavLink
                    to="/cart"
                    className={({ isActive }) =>
                        isActive ? `${styles.navLink} ${styles.active}` : styles.navLink
                    }
                >
                    Кошик
                </NavLink>
            </nav>
        </header>
    );
}

export default Header;
