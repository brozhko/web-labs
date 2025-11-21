import React from "react";
import booksPhoto from "../assets/books.jpg";
import styles from "./Hero.module.css";

function Hero() {
    return (
        <div className={styles.hero}>
            <img
                className={styles.leftBox}
                src={booksPhoto}
                alt="Стос українських книг"
            />

            <div className={styles.textBlock}>
                <h1 className={styles.title}>Українські книги</h1>
                <p className={styles.text}>
                    Книги зберігають мову, пам’ять і досвід, який не зникає у стрічках соцмереж.
                    Читаючи українських авторів, ми підтримуємо культуру, розширюємо світогляд
                    і передаємо історії далі.
                </p>
            </div>
        </div>
    );
}

export default Hero;
