module Zad4

open System


type Account = {
    AccountNumber: string
    Balance: float
}


let mutable accounts = Map.empty<string, Account>


let createAccount accountNumber =
    if Map.containsKey accountNumber accounts then
        printfn "Konto o numerze %s już istnieje." accountNumber
    else
        let newAccount = { AccountNumber = accountNumber; Balance = 0.0 }
        accounts <- Map.add accountNumber newAccount accounts
        printfn "Utworzono nowe konto o numerze %s." accountNumber


let deposit accountNumber amount =
    if Map.containsKey accountNumber accounts then
        let account = accounts.[accountNumber]
        let updatedAccount = { account with Balance = account.Balance + amount }
        accounts <- Map.add accountNumber updatedAccount accounts
        printfn "Wpłacono %.2f na konto %s. Nowe saldo: %.2f" amount accountNumber updatedAccount.Balance
    else
        printfn "Konto o numerze %s nie istnieje." accountNumber

let withdraw accountNumber amount =
    if Map.containsKey accountNumber accounts then
        let account = accounts.[accountNumber]
        if account.Balance >= amount then
            let updatedAccount = { account with Balance = account.Balance - amount }
            accounts <- Map.add accountNumber updatedAccount accounts
            printfn "Wypłacono %.2f z konta %s. Nowe saldo: %.2f" amount accountNumber updatedAccount.Balance
        else
            printfn "Niewystarczające środki na koncie %s." accountNumber
    else
        printfn "Konto o numerze %s nie istnieje." accountNumber

let displayBalance accountNumber =
    if Map.containsKey accountNumber accounts then
        let account = accounts.[accountNumber]
        printfn "Saldo konta %s wynosi: %.2f" accountNumber account.Balance
    else
        printfn "Konto o numerze %s nie istnieje." accountNumber

