:'

Hackerank Domains: https://www.hackerrank.com/domains

Linux Shell https://www.hackerrank.com/domains/shell/bash

Bash Challenges: https://www.hackerrank.com/domains/shell/bash

Hackerrank - Linux Shell  - Bash - Compute the Average

Given  integers, compute their average correct to three decimal places.

Input Format
The first line contains an integer, .
 lines follow, each containing a single integer.

Output Format
Display the average of the  integers, rounded off to three decimal places.

Input Constraints

 ( refers to elements of the list of integers for which the average is to be computed)

Sample Input

4
1
2
9
8
Sample Output

5.000
Explanation
The '4' in the first line indicates that there are four integers whose average is to be computed. The average = (1 + 2 + 9 + 8)/4 = 20/4 = 5.000 (correct to three decimal places) Please include the zeroes even if they are redundant (e.g. 0.000 instead of 0).


'

total=0; read n
while read -r integer || [[ -n "$integer" ]]; do total=$(($total + $integer))
done
printf "%.3f" $(echo "scale=10; $total/$n" | bc -l)
