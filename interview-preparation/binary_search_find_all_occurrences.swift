//  create sorted array
let arr:[Int] = [0, 0, 0, 0, 0, 1, 1 , 1 ,1, 4, 5, 6, 7]

// binary search recursive function that returns all occurences of a number
// if the mid element is equal to desired element we add 1 to the recursion tree
// otherwise we add 0, and repeat recursively this proccess according with the binary search logic
func binarySearch(arr: Array<Int>, element: Int) -> Int {

  // base cases for the binary-search recursion 
  
  // when the arr(ay) only has 1 element we check for the desired element and return 1 or 0
  if (arr.count == 1) { return arr[0] == element ? 1 : 0}
  // when the arr(ay) only has 2 elements, 
  if (arr.count == 2) { return ((arr[0] == element ? 1 : 0) + (arr[1] == element ? 1 : 0))}

  // edge cases handling
  // if the desired element is lower than the first or higher than the last
  // we return 0
  if((element < arr[0]) || (element > arr[arr.count - 1])) { return 0 }

  // find the array mid element index
  let midElementIndex = Int(arr.count / 2)

  // check the mid element value to decide the next recursion steps

  // check if it's equal to the desired element
  // if it is, we have found 1 ocurrence and there might be other occurences on both sides of array
  // therefore we make recursive calls to both halves(excluding the mid element), and add 1 to our recursion tree since we found 1 ocurrence
  if arr[midElementIndex] == element {
    // create recursive calls for both halves(excluding the mid element) adding 1 to the recursive call
    return (
      1 +
      // checking for the lower values side of the array
      binarySearch(arr: Array(arr[0...(midElementIndex - 1)]), element: element) + 
      // checking for the higher values side of the array
      binarySearch(arr: Array(arr[(midElementIndex + 1)...(arr.count - 1)]), element: element)
    )
  }
  // check if the mid element is lower than the desired element, if so, we add 0 to the recursion tree
  // and look for the half with bigger elements
  else if arr[midElementIndex] < element {
    return 0 + binarySearch(arr: Array(arr[midElementIndex + 1...arr.count - 1]), element: element)

  }
  // if the mid element is higher than the desired element, therefore we add 0 to the recursion tree
  // and look for the half with smaller elements
  else{
    return 0 + binarySearch(arr: Array(arr[0...midElementIndex - 1]), element: element)
  }
}

print(binarySearch(arr: arr, element: 4))