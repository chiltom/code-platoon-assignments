function fibonacci(num) {
  // Coverage for first two nums of sequence
  if (num === 0) {
    return 0;
  } else if (num === 1) {
    return 1;
  }

  // Set first nums of fibonacci sequence
  let twoBack = 0;
  let oneBack = 1;

  // Placeholder
  let current = 0;

  // Iterate num amount of times for nth term in sequence past 1
  for (let i = 1; i < num; i++) {
    current = oneBack + twoBack;
    twoBack = oneBack;
    oneBack = current;
  }

  return current;
}

module.exports = fibonacci;
