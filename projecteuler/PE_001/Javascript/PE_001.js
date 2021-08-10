// define a nice alias for creating a range
// https://stackoverflow.com/a/29559308/3198973
const range = (start, stop) =>
  new Array(stop - start).fill().map((_, i) => i + start)

const divisibleBy = (divisors) => (number) => 
  divisors.some((divisor) => number % divisor === 0)

const sum = (acc, val) => acc + val

const PE_001 = (start, stop, divisors) =>
  range(start, stop)
   .filter(divisibleBy(divisors))
   .reduce(sum)

let [start, stop, divisors] = [1, 1000, [3, 5]]
console.log(PE_001(start, stop, divisors))
