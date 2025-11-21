import React from "react";
import styles from "./Footer.module.css";

function Footer() {
  return (
    <footer className={styles.footer}>
      <div className={styles.inner}>
        <div className={styles.brandBlock}>
          <div className={styles.brand}>UA Bookshelf</div>
          <p className={styles.tagline}>
            Добірки українських книг для читачів у всьому світі.
            Нова класика, переклади, дитяча література — все в одному каталозі.
          </p>
        </div>

        <div className={styles.socials}>
          <a className={styles.social} href="#" aria-label="Facebook">
            <span className={styles.icon}>f</span>
          </a>
          <a className={styles.social} href="#" aria-label="Twitter">
            <span className={styles.icon}>t</span>
          </a>
          <a className={styles.social} href="#" aria-label="LinkedIn">
            <span className={styles.icon}>in</span>
          </a>
          <a className={styles.social} href="#" aria-label="Google">
            <span className={styles.icon}>G+</span>
          </a>
        </div>
      </div>
      <div className={styles.divider}></div>
      <div className={styles.copy}>© 2025 UA Bookshelf. Всі права захищені.</div>
    </footer>
  );
}

export default Footer;
