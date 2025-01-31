module Main

open Zad1
open Zad2
open Zad3
open Zad4
open Zad5

let menu () =
    printfn "Wybierz zadanie:"
    printfn "1. Zadanie 1 (Fibonacci)"
    printfn "2. Zadanie 2 (Binary Tree Search)"
    printfn "3. Zadanie 3 (Permutacje listy)"
    printfn "4. Zadanie 4 (Wieże Hanoi)"
    printfn "5. Zadanie 5 (QuickSort)"
    printf "Wybór: "
    let choice = System.Console.ReadLine()
    match choice with
    | "1" -> 
        printf "Podaj wartość dla obliczenia Fibonacciego: "
        let n = System.Console.ReadLine() |> int
        printfn "Fibonacci = %d" (fibonacci n)
    | "2" -> 
        let tree = Node(10, Node(5, Empty, Empty), Node(15, Empty, Empty))
        printf "Podaj wartość do wyszukania w drzewie: "
        let value = System.Console.ReadLine() |> int
        printfn "searchRecursive %d tree = %b" value (searchRecursive value tree)
        printfn "searchIterative %d tree = %b" value (searchIterative value tree)
    | "3" -> 
        printf "Podaj listę liczb całkowitych (oddzielone spacjami): "
        let input = System.Console.ReadLine()
        let lst = input.Split(' ') |> Array.map int |> Array.toList
        let perms = permutations lst
        printfn "Permutacje: %A" perms
    | "4" -> 
        printf "Podaj liczbę dysków: "
        let n = System.Console.ReadLine() |> int
        printfn "Rekurencyjne rozwiązanie:"
        hanoi n "A" "C" "B"
        printfn "Iteracyjne rozwiązanie:"
        hanoiIterative n "A" "C" "B"
    | "5" -> 
        printf "Podaj listę liczb całkowitych do posortowania (oddzielone spacjami): "
        let input = System.Console.ReadLine()
        let lst = input.Split(' ') |> Array.map int |> Array.toList
        let sortedRecursive = quicksort lst
        let sortedIterative = quicksortIterative lst
        printfn "Posortowane (rekurencyjnie): %A" sortedRecursive
        printfn "Posortowane (iteracyjnie): %A" sortedIterative
    | _ -> printfn "Nieprawidłowy wybór"

[<EntryPoint>]
let main argv =
    menu()
    0
