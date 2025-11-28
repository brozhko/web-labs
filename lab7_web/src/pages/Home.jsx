import React from "react";
import Hero from "../components/Hero";
import ProductList from "../components/ProductList";

function Home() {
  return (
    <>
      <Hero />
      <ProductList limit={3} showViewMore />
    </>
  );
}

export default Home;
