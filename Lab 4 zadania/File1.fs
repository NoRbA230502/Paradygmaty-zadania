module Zad2

open System


let exchangeRates = 
    Map.ofList [
        ("USD", 1.0)
        ("EUR", 0.85)
        ("GBP", 0.75)
        ("PLN", 3.8)
    ]


let convertCurrency amount sourceCurrency targetCurrency =
    let sourceRate = exchangeRates.[sourceCurrency]
    let targetRate = exchangeRates.[targetCurrency]
    amount * (targetRate / sourceRate)

module BMI =
  
    let calculateBMI weight height =
        weight / ((height / 100.0) ** 2.0)

    
    let getBMICategory bmi =
        if bmi < 18.5 then "Niedowaga"
        elif bmi < 24.9 then "Waga prawidłowa"
        elif bmi < 29.9 then "Nadwaga"
        else "Otyłość"
