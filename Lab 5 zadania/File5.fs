module Zad5

let rec quicksort lst =
    match lst with
    | [] -> []
    | pivot :: tail ->
        let smallerOrEqual = List.filter (fun x -> x <= pivot) tail
        let larger = List.filter (fun x -> x > pivot) tail
        quicksort smallerOrEqual @ [pivot] @ quicksort larger

let quicksortIterative lst =
    let arr = List.toArray lst
    let stack = System.Collections.Generic.Stack<_>()
    stack.Push(0, arr.Length - 1)
    while stack.Count > 0 do
        let (low, high) = stack.Pop()
        if low < high then
            let pivot = arr.[high]
            let mutable i = low - 1
            for j in low .. high - 1 do
                if arr.[j] <= pivot then
                    i <- i + 1
                    let temp = arr.[i]
                    arr.[i] <- arr.[j]
                    arr.[j] <- temp
            let temp = arr.[i + 1]
            arr.[i + 1] <- arr.[high]
            arr.[high] <- temp
            let p = i + 1
            stack.Push(low, p - 1)
            stack.Push(p + 1, high)
    Array.toList arr