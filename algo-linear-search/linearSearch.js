function linearSearch(searchTerm, arr) {
  // Iterate over arr
  for (let elem of arr) {
    // If searchTerm matches elem of arr, return index of elem
    if (searchTerm === elem) {
      return arr.indexOf(elem);
    }
  }

  // If searchTerm is not found in arr
  return undefined;
}

function globalLinearSearch(searchTerm, arr) {
  // Arr to contain indices of found elements
  let indices = [];
  // Iterate over arr
  for (let i = 0; i < arr.length; i++) {
    // If searchTerm matches elem of arr, push to indices arr and
    // continue search
    if (searchTerm === arr[i]) {
      indices.push(i);
    }
  }
  // If indices contains elements, return it; otherwise, return
  // undefined
  if (indices.length > 0) {
    return indices;
  } else {
    return undefined;
  }
}

module.exports = { linearSearch, globalLinearSearch };
