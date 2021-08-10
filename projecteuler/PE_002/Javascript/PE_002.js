
function* evenFibonacciGenerator() {
  // yields the next 2 even fibonacci number using the relation
  // E(n) = 4 * E(n-1) + E(n - 2) where E(0) = 0 and E(1) = 2
  // where E(n) represents the nth even fibonacci number: 0, 2, 8, 34, ...
  let [even_fib, even_fib_next] = [0, 2]
  while (true) {
    yield [even_fib, even_fib_next];
    [even_fib, even_fib_next] = [even_fib_next, 4 * even_fib_next + even_fib]
  }
}

const maxEvenFibonacci = (limit) => {
  // Returns the two largest even fibonacci numbers below and above a limit
  for (let [even_fib, next_even_fib] of evenFibonacciGenerator()) {
    if (next_even_fib > limit) {
      return [even_fib, next_even_fib]
    }
  }
}

function PE_002(limit) {
  // Finds the sum of the even fibonacci numbers below a limit
  //
  // Takes advantage of the following relation 
  //
  //  n
  //  Σ   E(i)  = ( E(n) + E(n + 1) - 2) / 2 
  // i=0
  //
  // Where E(i) represents the ith even fibonacci number this
  // is equivalent to 
  //
  //  n
  //  Σ   F(3i)  = ( F(3i + 2) - 1 ) / 2 
  // i=0
  //
  // since every third fibonacci number (F(n)) is even.
  let [even_fib, next_even_fib] = maxEvenFibonacci(limit)
  let total = (next_even_fib + even_fib - 2) / 4
  return total
}

let startTime = performance.now();
console.log(PE_002(4 * 10**300))
let totalTime = performance.now() - startTime;
console.log('It took ' + totalTime + ' ms.');
