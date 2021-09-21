// Scala


/*

What are higher-order functions?

Functions that take another function as a parameter, or functions that return another function as a result, or both. 
If it’s the latter, the returned function can be a curried function, which is a function that has its body programmatically defined in a higher-order function.

*/

object HigherOrderFunctions {
  
  /** A function that takes in the tax-rate and returns a function that calculates the total
    * based on the subtotal and the predefined tax-rate.
    * 
    *
    * @param rate - a `float` of the tax-rate
    * @return a function of `float => float` that takes in the subtotal and returns the total (subtotal * (1 + rate))
    */
  def setTaxRate(rate: float): float => float {
    return (subtotal: float) => subtotal * (1.0 + rate)
  }
  
  def main(args: Array[String]) = {
    // This function is a higher-order function that has a return type of a function
    val withSalesTax = setTaxRate(0.1)
    
    val subtotal = 500
    val total = withSalesTax(subtotal)
    
    // These functions are higher-order functions that take in function(s) as parameter(s)
    val subtotals = Seq(10.0, 323.0, 1100.0, 954.0, 177.0)
    val totals = subtotals.map(withSalesTax)
    
    val budget = 1000.0
    val totalsWithinBudget = subtotals.filter(withSalesTax(_) <= budget)
    
    val grandTotal = subtotals.fold(0.0){ case (accum, value) => accum + withSalesTax(value)}
  }
}
