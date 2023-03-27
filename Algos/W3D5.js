/* 
  Given an int to represent how much change is needed
  calculate the fewest number of coins needed to create that change,
  using the standard US denominations
*/
// quarter = 25 cents, dime = 10, nickel = 5, penny = 1
const cents1 = 25;
const expected1 = { quarter: 1 };

const cents2 = 50;
const expected2 = { quarter: 2 };

const cents3 = 9;
const expected3 = { nickel: 1, penny: 4 };

const cents4 = 99;
const expected4 = { quarter: 3, dime: 2, penny: 4 };

/**
 * Calculates the fewest coins of the standard American denominations needed
 *    to reach the given cents amount.
 * @param {number} cents
 * @returns {Object<string, number>} - A denomination table where the keys are
 *    denomination names and the value is the amount of that denomination
 *    needed.
 */

 function fewestCoinChange(cents) {
    //Your code here
}

console.log(fewestCoinChange(cents1)) // { quarter: 1 }
console.log(fewestCoinChange(cents2)) // { quarter: 2 }
console.log(fewestCoinChange(cents3)) // { nickel: 1, penny: 4 }
console.log(fewestCoinChange(cents4)) // { quarter: 3, dime: 2, penny: 4 }



function fewestCoinChange(cents) {
    result = {};
    var remainder = 0;
    // if (cents % 25 == 0) {
        quarterCount = Math.floor(cents / 25); 
        remainder = cents % 25;
        if (quarterCount > 0) {
            result.quarter = quarterCount
        }
    // }
    // else if (remainder % 10 == 0) {
        dimeCount = Math.floor(remainder / 10); 
        remainder = remainder % 10;
        if (dimeCount > 0) {
            result.dime = dimeCount
        }
    // }
    // else if (remainder % 5 == 0) {
        nickelCount = Math.floor(remainder / 5); 
        remainder = remainder % 5;
        if (nickelCount > 0) {
            result.nickel = nickelCount
        }
    // }
    // else if (remainder % 1 == 0) {
        pennyCount = Math.floor(remainder / 1); 
        if (pennyCount > 0) {
            result.penny = pennyCount
        }
    // }
    return result;
}