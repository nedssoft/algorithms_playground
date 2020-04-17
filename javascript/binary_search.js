function binary_search(arr, target) {
  // Get the lowest index in the array
  let low = 0;
  // Get the highest index in the array
  let high = arr.length - 1;
  // While the end of the array is not reached
  while (low <= high) {
    // Get the middle index
    let mid = Math.floor((low + high) / 2);
    // If the middle item is the target return 1
    if (arr[mid] === target) {
      return 1;
    } else if (target > arr[mid]) {
    // If the target is greater than the the middle item
    // then the target is at the RHS
      low = mid + 1;
    } else {
      // If the target is less than the the middle item
      // then the target is at the LHS
      high = mid - 1;
    }
  }
  return -1;
}

console.log(binary_search([1, 2, 3, 4, 5], 6)); // -1
console.log(binary_search([1, 2, 3, 4, 5], 5)); // 1
