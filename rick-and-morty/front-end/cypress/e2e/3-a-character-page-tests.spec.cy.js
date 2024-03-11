/* eslint-disable no-undef */
describe("Tests for a character page based on id", () => {
  it("Test adding favorite and removing favorite", () => {
    cy.visit("/character/1");
    cy.get(".card-body > button").should("contain", "Add Favorite");
    cy.get(".card-body > button").click();
    cy.get(".card-body > button").should("contain", "Remove Favorite");
  });

  it("Test characters button and going back to all characters", () => {
    cy.visit("character/1");
    cy.get(".btn-secondary").should("contain", "Return to Characters");
    cy.get(".btn-secondary").click();
    cy.get("#characters-container").children().should("have.length", 20);
  });
});
