module Zad4

let rec hanoi n source target auxiliary =
    if n > 0 then
        hanoi (n - 1) source auxiliary target
        printfn "Przenieś dysk z %s do %s" source target
        hanoi (n - 1) auxiliary target source

let hanoiIterative n source target auxiliary =
    let totalMoves = pown 2 n - 1
    let pegs = [| source; auxiliary; target |]
    for i in 1 .. totalMoves do
        let fromPeg = pegs.[(i &&& i - 1) % 3]
        let toPeg = pegs.[((i ||| i - 1) + 1) % 3]
        printfn "Przenieś dysk z %s do %s" fromPeg toPeg