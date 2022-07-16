//Ishrat Amin
// CSCI316


#include <iostream>
#include <iomanip>

long next_Fibonacci();

int main()
{
  int count {};
  std::cout << "Enter a number : ";
  std::cin >>count;
  std::cout << "The Fibonacci  Series:\n";
  for (int i {} ; i < count ; ++i)
  {
    std::cout << std::setw(10) << next_Fibonacci();
    if (!((i + 1) % 8))                     
      std::cout << std::endl;               
  }
  std::cout << std::endl;
}

// Generate the next number in the series
long next_Fibonacci()
{
  static long last;         
  static long last_but_one {1L};            

  long next {last + last_but_one};          
  last_but_one = last;                      
  last = next;                              
  return last;                              
}