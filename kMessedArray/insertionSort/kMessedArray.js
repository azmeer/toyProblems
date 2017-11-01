/*

  From Pramp Interview #1

  Inputs: numbers, k
  Outputs: sorted(numbers)

Straightforward solution: sorted(numbers) - but this doesn't take into account input is mostly sorted
Actual solution: use incremental insertion sort over the last k elements

 */


function sortKMessedArray(arr, k) {
  for (let i = 0; i < arr.length; i++) {
    insertionSort(arr, i, Math.min(i + k + 1, arr.length));
  }
  return arr;
}

const insertionSort = (arr, min=0, max=arr.length) => {
  console.log ('calling insertion sort on ', arr, ' with min: ', min, ' and max: ', max);
  console.log ('sorting:', arr.slice(min, max));
  for (let i = min; i < max; i++) {
    let insert_me = i;
    for (let j = i - 1; j >= min; j--) {
      if (arr[j] > arr[insert_me]) {
        let temp = arr[j];
        arr[j] = arr[insert_me];
        arr[insert_me] = temp;
        insert_me = j;
      } else {
        break;
      }
    }
  }
  console.log('sorted to: ', arr.slice(min, max));
}

arr = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9];
console.log(sortKMessedArray(arr, 2));
//insertionSort(arr, 0, 3)
//insertionSort(arr, 2, 5)
//console.log(arr);
