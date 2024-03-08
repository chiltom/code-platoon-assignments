/* eslint-disable no-undef */
// Tests for about page
describe("Initial tests for about page structure", () => {
  it("Find container of show information and check contents", () => {
    cy.visit("/about/");
    cy.get("#show-description > h1").should("contain", "About the Show");
  });

  it("Find the container of creators and voice actors and check contents", () => {
    cy.visit("/about/");
    cy.get("#creators-credits > h1").should(
      "contain",
      "Creators and Voice Actors"
    );
  });
});
