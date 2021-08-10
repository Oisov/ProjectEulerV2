
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
  // Where F represents the nth fibonacci number
  let [even_fib, next_even_fib] = maxEvenFibonacci(limit)
  let total = (next_even_fib + even_fib - 2) / 4
  return total
}

// This attempts to solve Project Euler 02 using mathematics
// Note that this does lead to floating point errors

let sqrt5 = Math.sqrt(5)
let goldenRatio = (1 + sqrt5) / 2
let phi = (1 + sqrt5) / 2
let psi = (1 - sqrt5) / 2
let goldenLog = Math.log(goldenRatio)
let phiLog = Math.log(phi)
let psiLog = Math.log(psi)

const logGoldenRatio = (x) => Math.log(x) / goldenLog

let logGoldenRatioSqrt5 = logGoldenRatio(sqrt5) / 3

// Creates a lookup table of every fibonacci value
// possible without involving longs (32 bits)
const fibonacciTable = [
  0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584,
  4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811,
  514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352,
  24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437,
  701408733, 1134903170, 1836311903, 2971215073, 4807526976, 7778742049,
  12586269025, 20365011074, 32951280099, 53316291173, 86267571272,
  139583862445, 225851433717, 365435296162, 591286729879, 956722026041,
  1548008755920, 2504730781961, 4052739537881, 6557470319842, 10610209857723,
  17167680177565, 27777890035288, 44945570212853, 72723460248141,
  117669030460994, 190392490709135, 308061521170129, 498454011879264,
  806515533049393, 1304969544928657, 2111485077978050, 3416454622906707,
  5527939700884757, 8944394323791464
];

// const fibonacciTableEven = [
//   0,                2,
//   8,               34,
//   144,              610,
//   2584,            10946,
//   46368,           196418,
//   832040,          3524578,
//   14930352,         63245986,
//   267914296,       1134903170,
//   4807526976,      20365011074,
//   86267571272,     365435296162,
//   1548008755920,    6557470319842,
//   27777890035288,  117669030460994,
//   498454011879264, 2111485077978050,
//   8944394323791464
// ]

const fibonacciTableEven = [
  0, 2, 8, 34, 144, 610, 2584, 10946, 46368, 196418, 832040, 3524578, 14930352,
  63245986, 267914296, 1134903170, 4807526976, 20365011074, 86267571272,
  365435296162, 1548008755920, 6557470319842, 27777890035288, 117669030460994,
  498454011879264, 2111485077978050, 8944394323791464
]

// A utility function that returns true if x is perfect square
const isPerfectSquare = (x) => {
    let s = parseInt(Math.sqrt(x))
    return (s * s == x)
}
 
// Returns true if n is a Fibinacci Number, else false
const isFibonacci = (n) =>
  // n is Fibinacci if one of 5*n*n + 4 or 5*n*n - 4 or both
  // is a perferct square
  isPerfectSquare(5 * n * n + 4) || isPerfectSquare(5 * n * n - 4)

function largestEvenFibIndex (limit) {
  // Computes the largest index such that F(index) < limit
  //
  // Note that the closed form for the nth fibonacci number [F(n)] is
  //
  //   F(n) = ( Φ^n + ψ^n ) / sqrt 5
  //
  // Where the shorthand notation 
  //
  //     Φ = (1 + sqrt 5 ) / 2 and ψ = (1 - sqrt 5 ) / 2
  //
  // was introduced. As ψ < 1 we have ψ^n → 0 as n → ∞ thus
  //
  //   F(3n) ∼ Φ^(3n) / sqrt 5
  //
  // For sufficiently large n. We wish to solve F(3n) < limit for n
  //
  //   F(3n) < limit 
  //   Φ^(3n) / sqrt 5 < limit
  //   3n * log Φ < log ( limit * sqrt(5) )
  //   3n < log sqrt(5)  / log Φ + log limit / log Φ
  //    n < [ log(sqrt(5), Φ) + log(limit, Φ) ] / 3
  //    n = floor( [ log(sqrt(5), Φ) + log( limit, Φ) ] / 3 )
  //
  // Where the right handside is our return value. Note that the value
  //
  //   log(sqrt(5), Φ) / 3
  //
  // Is always constant, and therefore is precomputed in logGoldenRatioSqrt5
  let index = Math.floor(logGoldenRatioSqrt5 + logGoldenRatio(limit) / 3)
  if (!isFibonacci(limit)) {
    return index
  }
  let next_index = 3 * (index + 1)
  if (next_index < fibonacciTable.length) {
    var next_value = fibonacciTable[next_index]
  } else {
    var next_value = fibonacci(next_index)
  }
  if (next_value > limit) {
    return index
  } else {
    return index + 1
  }
  // Note that log(x, Φ) 
  // is implemented as logGoldenRatio and is the logarithm of x
  // with base Φ (equivalent to log(x) / log(Φ) in an arbitary other base)
}


function fibonacci(n) {
  // Finds the nth fibonacci number using fast doubling in O(log n)
  //
  // Exploits the relations 
  //
  //   F(2n) = F(n) * [ F(n+1) * 2  − F(n) ]
  // F(1+2n) = F(2n) * F(2n) + F(2n+1) * F(2n)
  //
  // To get from F(n) and F(n+1) to F(2n) and F(2n+1) (top down approach)
	if (n < 0){
    throw new Error("Negative arguments not implemented")
  }
  return fibHelper(n)[0]
}

function fibHelper(n) {
	if (n == 0) {
		return [BigInt(0), BigInt(1)]
  } else {
		let [a, b] = fibHelper(Math.floor(n / 2))
		let c = a * (b * BigInt(2) - a)
		let d = a * a + b * b
		if (n % 2 == 0) {
			return [c, d]
    } else {
			return [d, c + d]
    }
  }
}

function ProjectEuler002 (limit) {
  // Finds the sum of all even fibonacci numbers below the limit
  //
  // Exploits the fact that the sum of the even values has a closed expression
  //
  //  n
  //  Σ   F(3i)  = ( F(3i + 2) - 1 ) / 2 
  // i=0
  //
  // Where F(n) is the n'th fibonacci number. Switches to BigInt
  // if the values are outside of the standard 32 bit range
 
  let index = 3 * largestEvenFibIndex(limit) + 2
  if (index < fibonacciTable.length) {
    return (fibonacciTable[index] - 1) / 2
  } else {
    return (fibonacci(index) - BigInt(1)) / BigInt(2)
  }
}

let big = 4*10**15
let limit = 10**5

// let [exact, math] = [PE_002(5), ProjectEuler002(5)]
//   for (let i = 0; i < 4*10**6; i++) {
//     [exact, math] = [PE_002(i), ProjectEuler002(i)]
//     if (exact != math) {
//       // console.log(i, exact, math, isFibonacci(i));
//   }
// }

// console.log("hello")

// let limit = 4*10 ** 300
// let startTime = performance.now();
// console.log(PE_002(limit))
// console.log((fibonacciTable[3 * largestEvenFibIndex(limit) + 2] - 1) / 2)
// console.log((fibonacci(3 * largestEvenFibIndex(limit) + 2) - BigInt(1)) / BigInt(2))
// let endTime = performance.now();
// console.log('It took ' + (endTime - startTime) + ' ms.');


