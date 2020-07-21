#!/usr/local/bin/python3
'''
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3
Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99


SOLUTION LOGIC 1:
We can sum the bits in same positions for all the numbers and take modulo with 3. The bits for which sum is not multiple of 3, are the bits of number with single occurrence.
Let us consider the example array {5, 5, 5, 8}. The 101, 101, 101, 1000
Sum of first bits%3 = (1 + 1 + 1 + 0)%3 = 0;
Sum of second bits%3 = (0 + 0 + 0 + 0)%0 = 0;
Sum of third bits%3 = (1 + 1 + 1 + 0)%3 = 0;
Sum of fourth bits%3 = (1)%3 = 1;
Hence number which appears once is 1000

'''
INT_SIZE = 4
def single_number(nums) -> int:
    print(nums)
    result = 0
    for i in range(0,INT_SIZE):
        sm = 0
        x = (1 << i)
        for j in range(0,len(nums)):
            print(nums[j],x,nums[j]&x)
            if (nums[j] & x):
                sm += 1


if __name__ == '__main__':
    input = [2,2,3,2]
    print(single_number(input))
