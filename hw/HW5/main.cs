// Reference : 
// https://www.geeksforgeeks.org/bubble-sort/?ref=gcse
// https://www.tutorialspoint.com/Bubble-Sort-program-in-Chash


// Ishrat Amin
// CSCI316

using System;

namespace BubbleSort
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] myarray = {4,1,9,90, 56, 81, 34,60, 88};
            Console.WriteLine("Array before sorting:");
            foreach (int x in myarray)
                Console.Write(x + "  ");
            Sort.BubbleSort(myarray);
            Console.WriteLine("\nArray after sorting:");
            foreach (int x in myarray)
                Console.Write(x + "  ");
            Console.WriteLine();
        }
    }
    class Sort
    {
        public static void BubbleSort(int[] arr)
        {
            for(int i=0;i<arr.Length-1;i++)
            {
                for(int j=0;j<arr.Length-i-1;j++)
                {
                    if (arr[j] > arr[j + 1])
                        swap(ref arr[j], ref arr[j + 1]);
                }
            }
        }
        static void swap(ref int x, ref int n)
        {
            int t = x;
            x = n;
            n = t;
        }
    }
}