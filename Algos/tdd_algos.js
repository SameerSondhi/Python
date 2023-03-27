// REVERSE LIST - Write a function that reverses the values in the list (optional: without creating a temporary array).
// const str1 = [6,7,8,9,0]

// function reverseList(str){
//     var newstr = []
//     for (var i = str.length-1; i>=0; i--){
//         newstr += str[i]
//     }
//     return newstr
// }
// console.log(reverseList(str1))



// PALINDROME - Write a function that checks whether the given word is a palindrome (a word that spells the same backward).
// const str2 = "123321"
// const expected2 = True

// function isPalindrome(str){
//     for (i=0; i<str.length; i++){
//         if(str[i] == str[str.length-1-i]){
//             return true
//         }
//         else {
//             return false
//         }
//     }
// }
// console.log(isPalindrome(str2))


// COINS - Write a function that determines how many quarters, dimes, nickels, and pennies to give to a customer for a change 
// where you minimize the number of coins you give out.

const amount1 = 37
const expected3 = "3 Quarters, 1 Dime, 0 Nickels, 2 Pennies"

function coin(amount){
    var numbers = {
        num1 : 0,
        num2 : 0,
        num3 : 0,
        num4 : 0
    }
    const values = {
        quarters : 25,
        dimes : 10,
        nickels : 5,
        pennies : 1
    }

    if (amount % values.quarters == 0){
        numbers.num1 = amount/values.quarters
        console.log(numbers.num1 + " Quarters, " + numbers.num2 + " Dimes, " + numbers.num3 + " Nickels, " + numbers.num4 + " Pennies")
    }

    if (amount == 10){
        numbers.num2 = amount/values.dimes
        console.log(numbers.num1 + " Quarters, " + numbers.num2 + " Dimes, " + numbers.num3 + " Nickels, " + numbers.num4 + " Pennies")
    }

    if (amount==5){
        numbers.num3 = amount/values.nickels
        console.log(numbers.num1 + " Quarters, " + numbers.num2 + " Dimes, " + numbers.num3 + " Nickels, " + numbers.num4 + " Pennies")
    }

    if (amount<5){
        numbers.num4 = amount/values.pennies
        console.log(numbers.num1 + " Quarters, " + numbers.num2 + " Dimes, " + numbers.num3 + " Nickels, " + numbers.num4 + " Pennies")
    }

    if (amount % values.quarters !=0){
        var remainder1 = amount%values.quarters
        var remainder2 = remainder1%values.dimes
        var remainder3 = remainder2%values.nickels
        numbers.num1 = Math.floor(amount/values.quarters)
        numbers.num2 = Math.floor(remainder1/values.dimes)
        numbers.num3 = Math.floor(remainder2/values.nickels)
        numbers.num4 = Math.floor(remainder3)
        console.log(numbers.num1 + " Quarters, " + numbers.num2 + " Dimes, " + numbers.num3 + " Nickels, " + numbers.num4 + " Pennies")
    }

}
coin(amount1)


// BONUS - FACTORIAL - Write a recursive function that returns the factorial of a given number. 
// Remember that the factorial of a number is the product of all the numbers between 1 and the given number (eg. 4! = 4*3*2*1).






// BONUS - fibonacci - Write a recursive function that accepts a number, n, and returns the nth Fibonacci number from the sequence. 
// The first two Fibonacci numbers are 0 and 1. Every number after that is calculated by adding the previous 2 numbers from the sequence. 
// (i.e. 0, 1, 1, 2, 3, 5, 8, 13, 21 ...)