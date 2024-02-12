/**
 *
 * @param {number} num
 * @returns {string} romanNumeral
 */
function toRomanLazy(num) {
  // Object containing roman numerals and arabic equivalents
  const romanNumeralToArabic = {
    M: 1000,
    D: 500,
    C: 100,
    L: 50,
    X: 10,
    V: 5,
    I: 1,
  };

  // Array for descendance precedence of romanNumerals
  // const romanNumeralPriorityOrder = ['M', 'D', 'C', 'L', 'X', 'V', 'I'];

  // Better way to gather precedence order using already established object
  const romanNumeralPriorityOrder = Object.keys(romanNumeralToArabic);

  // Placeholder for romanNumeral string
  let romanNumeral = "";

  // Iterate over arr containing romanNumeral precedence
  for (let elem of romanNumeralPriorityOrder) {
    count = Math.floor(num / romanNumeralToArabic[elem]);
    for (let i = 0; i < count; i++) {
      romanNumeral += elem;
    }
    num -= romanNumeralToArabic[elem] * count;
    if (num <= 0) {
      break;
    }
  }

  return romanNumeral;
}

function toRoman(num) {
  // Object containing roman numerals and arabic equivalents
  const romanNumeralToArabic = {
    M: 1000,
    CM: 900,
    D: 500,
    CD: 400,
    C: 100,
    L: 50,
    XL: 40,
    X: 10,
    IX: 9,
    V: 5,
    IV: 4,
    I: 1,
  };

  // Array for descendance precedence of romanNumerals
  const romanNumeralPriorityOrder = [
    "M",
    "CM",
    "D",
    "CD",
    "C",
    "L",
    "XL",
    "X",
    "IX",
    "V",
    "IV",
    "I",
  ];

  // Placeholder for romanNumeral string
  let romanNumeral = "";

  // Iterate over arr containing romanNumeral precedence
  for (let elem of romanNumeralPriorityOrder) {
    count = Math.floor(num / romanNumeralToArabic[elem]);
    for (let i = 0; i < count; i++) {
      romanNumeral += elem;
    }
    num -= romanNumeralToArabic[elem] * count;
    if (num <= 0) {
      break;
    }
  }

  return romanNumeral;
}

module.exports = { toRoman, toRomanLazy };
