module Zad2

type BinaryTree<'T> =
    | Empty
    | Node of 'T * BinaryTree<'T> * BinaryTree<'T>

let rec searchRecursive value tree =
    match tree with
    | Empty -> false
    | Node(v, left, right) ->
        if value = v then true
        else searchRecursive value left || searchRecursive value right

let searchIterative value tree =
    let rec loop stack =
        match stack with
        | [] -> false
        | Empty :: rest -> loop rest
        | Node(v, left, right) :: rest ->
            if value = v then true
            else loop (left :: right :: rest)
    loop [tree]