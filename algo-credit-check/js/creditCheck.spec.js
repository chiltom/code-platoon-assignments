const creditCheck = require("./creditCheck");

// console.log(creditCheck('5541808923795240') === "The number is valid!");
// console.log(creditCheck("4024007136512380") === "The number is valid!");
// console.log(creditCheck("6011797668867828") === "The number is valid!");

// console.log(creditCheck("5541801923795240") === "The number is invalid!");
// console.log(creditCheck("4024007106512380") === "The number is invalid!");
// console.log(creditCheck("6011797668868728") === "The number is invalid!");

describe("Validity tests", () => {

    test("Validity test 1", () => {
        expect(creditCheck('5541808923795240')).toEqual("The number is valid!");
    });

    test("Validity test 2", () => {
        expect(creditCheck("4024007136512380")).toEqual("The number is valid!");
    });

    test("Validity test 3", () => {
        expect(creditCheck("6011797668867828")).toEqual("The number is valid!");
    });
});

describe("Invalidity tests", () => {

    test("Invalidity test 1", () => {
        expect(creditCheck("5541801923795240")).toEqual("The number is invalid!");
    });

    test("Invalidity test 2", () => {
        expect(creditCheck("4024007106512380")).toEqual("The number is invalid!");
    });

    test("Invalidity test 3", () => {
        expect(creditCheck("6011797668868728")).toEqual("The number is invalid!");
    });
});