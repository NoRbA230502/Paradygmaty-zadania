﻿module Program

open System
open Zad2
open Zad3
open Task3
open Zad4

[<EntryPoint>]
let main argv =
    let rec menu () =
        printfn "Wybierz opcję:"
        printfn "1. Oblicz BMI"
        printfn "2. Konwersja waluty"
        printfn "3. Analiza tekstu"
        printfn "4. Operacje bankowe"
        printfn "5. Wyjdź"
        let choice = Console.ReadLine()

        match choice with
        | "1" ->
            printfn "Podaj wagę w kilogramach:"
            let weightInput = Console.ReadLine()
            printfn "Podaj wzrost w centymetrach:"
            let heightInput = Console.ReadLine()

            let weight = float weightInput
            let height = float heightInput

            let bmi = calculateBMI weight height
            let category = getBMICategory bmi

            printfn "Twoje BMI wynosi: %.2f" bmi
            printfn "Kategoria BMI: %s" category
            menu()
        | "2" ->
            printfn "Podaj kwotę do przeliczenia:"
            let amountInput = Console.ReadLine()
            printfn "Podaj walutę źródłową (np. USD, EUR, GBP, PLN):"
            let sourceCurrency = Console.ReadLine().ToUpper()
            printfn "Podaj walutę docelową (np. USD, EUR, GBP, PLN):"
            let targetCurrency = Console.ReadLine().ToUpper()

            let amount = float amountInput
            let convertedAmount = convertCurrency amount sourceCurrency targetCurrency

            printfn "Przeliczona kwota: %.2f %s" convertedAmount targetCurrency
            menu()
        | "3" ->
            printfn "Podaj tekst do analizy:"
            let inputText = Console.ReadLine()

            let wordCount = countWords inputText
            let characterCount = countCharacters inputText
            let mostFrequentWord = findMostFrequentWord inputText

            printfn "Liczba słów: %d" wordCount
            printfn "Liczba znaków (bez spacji): %d" characterCount
            printfn "Najczęściej występujące słowo: %s" mostFrequentWord
            menu()
        | "4" ->
            printfn "Wybierz operację bankową:"
            printfn "1. Utwórz nowe konto"
            printfn "2. Depozytuj środki na konto"
            printfn "3. Wypłać środki z konta"
            printfn "4. Wyświetl saldo konta"
            let bankChoice = Console.ReadLine()

            match bankChoice with
            | "1" ->
                printfn "Podaj numer konta:"
                let accountNumber = Console.ReadLine()
                createAccount accountNumber
                menu()
            | "2" ->
                printfn "Podaj numer konta:"
                let accountNumber = Console.ReadLine()
                printfn "Podaj kwotę do depozytu:"
                let amount = float (Console.ReadLine())
                deposit accountNumber amount
                menu()
            | "3" ->
                printfn "Podaj numer konta:"
                let accountNumber = Console.ReadLine()
                printfn "Podaj kwotę do wypłaty:"
                let amount = float (Console.ReadLine())
                withdraw accountNumber amount
                menu()
            | "4" ->
                printfn "Podaj numer konta:"
                let accountNumber = Console.ReadLine()
                displayBalance accountNumber
                menu()
            | _ ->
                printfn "Nieprawidłowy wybór"
                menu()
        | "5" -> printfn "Do widzenia!"
        | _ ->
            printfn "Nieprawidłowy wybór"
            menu()

    menu()
    0