const sumPairs = require("./sumPairs");

// Don't forget to add your tests :)
describe("tests sumPairs", () => {
    
    test("sumPairs([1, 2, 3, 4, 5], 9) === [4, 5]", () => {
        expect(sumPairs([1, 2, 3, 4, 5], 9)).toEqual([4, 5]);
    });

    test("sumPairs([1, 2, 3, 4, 5], 7) === [[2, 5], [3, 4]]", () => {
        expect(sumPairs([1, 2, 3, 4, 5], 7)).toEqual([[2, 5], [3, 4]]);
    });

    test("sumPairs([3, 1, 5, 8, 2], 27) === 'unable to find pairs", () => {
        expect(sumPairs([3, 1, 5, 8, 2], 27)).toEqual("unable to find pairs");
    });
})