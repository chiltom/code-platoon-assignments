import { useState, useEffect } from "react";
import { Outlet } from "react-router-dom";
import MyNavbar from "./components/MyNavbar";

export default function App() {
  const [favorites, setFavorites] = useState([]);

  useEffect(() => {
    console.log(favorites);
  }, [favorites]);

  const addFavorites = (char) => {
    const updatedFavorites = [...favorites, char];
    setFavorites(updatedFavorites);
  };

  const removeFavorites = (char) => {
    const updatedFavorites = favorites.filter((c) => {
      if (c.id !== char.id) {
        return c;
      }
    });
    setFavorites(updatedFavorites);
  };

  const checkIsFavorite = (id) =>
    favorites.filter((char) => char.id === id).length > 0;

  return (
    <>
      <MyNavbar />
      <Outlet
        context={{ favorites, addFavorites, removeFavorites, checkIsFavorite }}
      />
    </>
  );
}
