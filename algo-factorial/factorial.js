/**
 * A program to calculate factorials
 * @param {number} num 
 * @returns {number}
 */
function factorial(num) {
  let product = 1;
  for (let i = num; i > 0; i--) {
    product *= i;
  }
  return product;
}
module.exports = factorial;
