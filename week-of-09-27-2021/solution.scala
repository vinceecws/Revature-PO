object Main {
  
  def main(args: Array[String]): Unit = {
    
    /*
      Failure-prone code in the "try" block
    */
    try {
      val x = 1.0 / 0.0
    }
    
    /*
      Error-handling code in the "catch" block
      Case matching is used
    */
    catch {
      case e: ArithmeticException => println("Invalid operation. Division by 0")
      case _: Throwable => println("Unknown error encountered.")
    }
    
    /*
      Code that is expected to be executed irregardless of whether "catch" block was triggered
    */
    finally {
      println("Completed with errors.")
    }
  }
}
