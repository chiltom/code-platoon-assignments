/* eslint-disable no-undef */
describe("Tests for adding favorites and navigating the page", () => {
  it("Test adding 2 favorites and navigating to page", () => {
    cy.visit("/characters/");
    cy.get("#1 > .card-body > .btn-group > .favorite").click();
    cy.get("#2 > .card-body > .btn-group > .favorite").click();
    cy.get("#favoritesLink").click();
    cy.get("#favorites-container").children().should("have.length", 2);
  });
});
