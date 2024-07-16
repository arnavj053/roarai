# "Exploring Recursive Functions: A Concept That Spans Art, Nature, and Mathematics"

##  Recursive Functions. One of my favorite topics in this course. So a recursive function is a function whose body calls itself either directly or indirectly. We'll see both cases today. So what does that mean? Well, it means that sometimes when you're executing the body of a function, it's a recursive function. That might require you to apply that same function again. And recursion doesn't show up in computer science alone. It shows up in art and nature and mathematics. So for instance, Serpinsky's triangle is defined as three different Serpinsky triangles. One, two, three. Each of those, like this one, is made up of three Serpinsky triangles.

# "Exploring Digit Sums and Check Sum Digits in Credit Card Numbers"

##  As a starting example, we'll sum the digits of a number. 2013 is a number, positive integer, two plus zero plus one plus three is six. Why would we do this? Well, there are interesting properties of digits sum, such as a number A is divisible by nine, if and only if it's digits sum. It's also divisible by nine. And summing up digits is very useful for typo detection. So here's a credit card. Now, the problem with credit card numbers is that they're very long and humans type them in all the time, and humans are prone to error. So what exists in every credit card is called a check sum digit. So that 16th digit isn't really part of your account number. Instead, it's computed from all of the other digits. And the point of that is that if the check sum digit doesn't match the computation of all the other digits, that's an indication that the number was typed in wrong. It's an invalid credit card number. Now, the check sum digit is actually not just the sum of the other digits. It's something slightly more complicated, which we will compute later in this class, but we're going to start out with digit sums, and then we'll look at the actual algorithm that's used in order to compute check sums for credit cards. So we're going to sum digits without actually using a while statement.

# "Recursive Digit Summation without Using a While Statement"

##  You could probably figure out how to sum digits on your own already, but without using a while statement, we'll require recursion. Okay, so first, a building block will define the split function. To take an positive integer n and split it into two parts, all but its last digit and its last digit. And we'll do that through integer division by 10 and by taking the remainder of n divided by 10. Okay, so let's write down that split function. And we can understand what it does. It breaks up a number into all but the last digit and the last digit. So for 2013, we get the 201 and then the last digit is three. So if I can sum up the digits of 201 and I can add three to that, then I'll get the sum for 2013. Let's write that in code.

# "Summing the Digits of a Number: A Recursive Function"

##  In order to sum the digits of n, well if n is less than 10 meaning it's a single digit, we'll just return n. The sum of the digits of 7 is just 7. Otherwise, we're going to split up n into all but its last digit and its last digit. And then we'll return the sum of digits computed from those two parts. Well, what is that sum? We're going to sum up the digits of all but the last and then we'll add in the last digit. So for 2013, this would have 201 and 3. I would sum the digits of 201 to get 3. I'd add 3 more to that and I'll get 6. The answer I'm looking for. This is a recursive function. Why? We can call some digits from within some digits. This really does run. So let's look at the anatomy of a recursive function and then we can try it out. So the way it works is that the depth statement header is similar to any other function. You just give the function a name and some formal parameters. Then, typically a recursive function will start with a conditional statement that checks for base cases. Base cases are very simple versions of the problem I'm trying to solve. In this case, the base case is the really simple case where you only have one digit. So summing it up is trivial. You just return n. So base cases are evaluated without recursive calls. They can usually be computed directly, such as just returning n in this case. Now, if we're not in a base case meaning this is not a very simple problem but something more complex, where n has multiple digits, then we'll have a recursive case. And recursive cases are evaluated with recursive calls. So we split up the number that we're trying to sum the digits of and then we make a recursive call to some digits. Now notice we don't try to sum digits of n. Instead, we sum digits of a simpler problem than we had before. So if we started with 2013, now we only have 201 to sum the digits of, which is simpler because it has fewer digits to sum, getting us closer to the base case. Okay, before we move on, let's just type it in and make sure it really does work.

# "Summing Digits of a Number"

##  Def, sum digits of n. If n is less than 10, that's a test for the base case, and I'll just return n. Otherwise, I'm going to break up n by calling my split function into two parts, all but the last digit and then the last digit. And then I'll return some digits of the simpler problem just all but the last and then I have to add in the last digit. So we can sum the digits of 2013 or whatever number we wish.
