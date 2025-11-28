import React from "react";

function Select({ options, className, ...props }) {
  return (
    <select className={className} {...props}>
      {options.map((opt) => (
        <option key={opt.value} value={opt.value}>
          {opt.label}
        </option>
      ))}
    </select>
  );
}

export default Select;
