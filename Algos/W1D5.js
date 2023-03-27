/* 
String: Is Palindrome
Create a function that returns a boolean whether the string is a strict palindrome. 
    - palindrome = string that is same forwards and backwards

Do not ignore spaces, punctuation or capitalization
*/
// RIOT Read Input Output Talk
const str1 = "a x a";
const expected1 = true;

const str2 = "racecar";
const expected2 = true;

const str3 = "Dud";
const expected3 = false;

const str4 = "oho!";
const expected4 = false;

const str5 = "abba"
const expected5 = true;

const str6 = " "


function isPalindrome(str) {
    //Your code here
    for(var i =0; i<(str.length/2); i++){
        if (str[i]!=str[str.length-1-i]){
            return false
        }
        
    }
    return true



}

console.log(isPalindrome(str1)) //expected: true
console.log(isPalindrome(str2)) //expected: true
console.log(isPalindrome(str3)) //expected: false
console.log(isPalindrome(str4)) //expected: false
console.log(isPalindrome(str5)) //expected: true
console.log(isPalindrome(str6))