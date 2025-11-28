import React from "react";
import styles from "./PrimaryButton.module.css";

function PrimaryButton({ children, onClick, type = "button", className }) {
  const mergedClass = className
    ? `${styles.primaryButton} ${className}`
    : styles.primaryButton;

  return (
    <button type={type} className={mergedClass} onClick={onClick}>
      {children}
    </button>
  );
}

export default PrimaryButton;
