/* eslint-disable no-undef */
// Initial tests for home page
describe("Initial render test suite for homepage", () => {
  it("Check for homepage load on baseUrl render", () => {
    cy.visit("/"); // Can use / because we set baseUrl as dev server port
    cy.get("h1").should("have.text", "The Rick and Morty Encyclopedia");
  });

  it("Checks for navbar brand functionality", () => {
    cy.visit("/");
    cy.get("span").should("have.descendants", "a");
    cy.get("span > a").click();
    cy.get("span > a")
      .should("have.attr", "href")
      .and("contain", "/")
      .then((href) => cy.visit(href));
  });

  it("Checks 'About' page link for functionality", () => {
    cy.visit("/");
    cy.get("#aboutLink")
      .should("have.attr", "href")
      .and("contain", "/about/")
      .then((href) => cy.visit(href));
  });

  it("Checks 'Characters' page link for functionality", () => {
    cy.visit("/");
    cy.get("#charactersLink")
      .should("have.attr", "href")
      .and("contain", "/characters/")
      .then((href) => cy.visit(href));
  });

  it("Checks 'Favorites' page link for functionality", () => {
    cy.visit("/");
    cy.get("#favoritesLink")
      .should("have.attr", "href")
      .and("contain", "/favorites/")
      .then((href) => cy.visit(href));
  });
});
