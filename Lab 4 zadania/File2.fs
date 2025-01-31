module Zad3

open System
open System.Text.RegularExpressions


let countWords (text: string) =
    let words = text.Split([|' '; '\t'; '\n'; '\r'|], StringSplitOptions.RemoveEmptyEntries)
    words.Length


let countCharacters (text: string) =
    text.Replace(" ", "").Length


let findMostFrequentWord (text: string) =
    let words = text.Split([|' '; '\t'; '\n'; '\r'|], StringSplitOptions.RemoveEmptyEntries)
    let wordCounts = 
        words 
        |> Array.fold (fun acc word -> 
            if Map.containsKey word acc then 
                Map.add word (acc.[word] + 1) acc 
            else 
                Map.add word 1 acc) Map.empty
    wordCounts |> Map.toSeq |> Seq.maxBy snd |> fst

