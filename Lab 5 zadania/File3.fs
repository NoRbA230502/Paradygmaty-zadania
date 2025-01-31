module Zad3

let rec insertAtAllPositions x lst =
    match lst with
    | [] -> [[x]]
    | head :: tail ->
        (x :: lst) :: [for perm in insertAtAllPositions x tail -> head :: perm]

let rec permutations lst =
    match lst with
    | [] -> [[]]
    | head :: tail ->
        [for perm in permutations tail do
            for permWithHead in insertAtAllPositions head perm -> permWithHead]