/* eslint-disable no-undef */
describe("Tests for characters page", () => {
  it("Initial page load contains first 20 characters", () => {
    cy.visit("/characters/");
    cy.get("#characters-container").children().should("have.length", 20);
  });

  it("Test searching for characters functionality", () => {
    cy.visit("/characters/");
    cy.get("#inputQuery").type("Morty");
    cy.get("#submitButton").click();
    cy.get(".card-title:first").should("contain", "Morty Smith");
  });

  it("Test clicking see details to bring to character page", () => {
    cy.visit("/characters/");
    cy.get(".see-details:first").click();
    cy.get(".card-title").should("contain", "Rick Sanchez");
  });
});
