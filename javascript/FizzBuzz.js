var random = Math.floor(Math.random() * 100)
console.log(random)
var result = (random%3==0 && random%5==0) ? "quizzbuzz" : (random%5==0) ? "buzz" : (random%3==0) ? "quizz" : "none"

console.log(result)