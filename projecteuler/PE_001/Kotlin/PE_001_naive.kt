val divisible:(Int, Int) -> Boolean = { num, div -> num % div == 0 }

fun isDivisible (number: Int, divisors: List<Int>): Boolean { 
  return divisors.any{ divisible(number, it) }
}

fun projectEuler001 (start: Int, stop: Int, divisors: List<Int>): Int {
  return (start..stop-1)
         .filter{ isDivisible(it, divisors) }
         .sum()
}

fun main() {
  val divisors = listOf(3, 5)
  val start = 1
  val stop = 1000
  println(projectEuler001(start, stop, divisors))
}
