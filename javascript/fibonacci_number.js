/**
 * Calculate fibonacci number using The Golden Ratio algorithm
 * The golden ratio constant k = 1.618034
 * the formula is  k^n - (1-k)^n / sqrt(5)
 */

function fib_number(n) {
  const ans =
    (Math.pow(1.618034, n) - Math.pow(1 - 1.618034, n)) / Math.sqrt(5);
  return Math.round(ans);
}
console.log(fib_number(8))
