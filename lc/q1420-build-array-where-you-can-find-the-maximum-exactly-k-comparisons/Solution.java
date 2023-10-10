
// We are given three integers: n, m and k
// We need to find the number of ways to build an array arr of n positive integers,
// each ranging from 1 to m, such that the 'search_cost' of the array is equal to k
// 
// 'search_cost' is defined as the number of elements in the array that are greater than all
// the elements to their left
// 
// We use dp to solve this problem, creating a 3d array dp to store intermediate results
// dp[i][cost][max_val] represents the number of ways to build an array of length i+1
// with a maximum value max_val + 1 and a search cost cost+1,
//
// We initialize the base case where i = 0, and cost = 0, setting dp[0][0][max_val] to 1
// for all possible max_val
// 
// We iterate through the remaining values of i, cost and max_val, calculating the number
// of ways to build the array based on the previous values in dp
//
// To calculate dp[i][cost][max_val], we consider two cases:
// 1. adding max_val+1 as the maximum elements to the array
// 2. Not adding max_val+1 as the maximum element to the array
//
// we update dp[i][cost][max_val] accordingly and take care of the modulo
// operation to prevent overflow
// Finally, we sum up the values of dp[n-1][k-1][max_val] for all possible max_val to get 
// the total number of arrays with the desired properties
// the result is returned as (int) ans after taking the modulo 10^9 + 7
//
// Time complexity: O(n * m * k)
// Space complexity: O(n * k * m)

import java.util.Arrays;

public class Solution {
    public int numOfArrays(int n, int m, int k) {
        long[][][] dp = new long[n][k][m];
        long mod = 1000000007;
        Arrays.fill(dp[0][0], 1);

        // loop through arr
        for (int i = 1; i < n; i++) {
            // for each ele in arr, loop through cost from 0 to min(i+1, k) - 1
            for (int cost = 0; cost < Math.min(i + 1, k); cost++) {
                // for each ele in arr, cost, loop through max_val from 0 to m-1
                for (int max = 0; max < m; max++) {
                    // for last element for arr[i], can equal from max+1 to 1
                    dp[i][cost][max] = (dp[i][cost][max] + (max + 1) * dp[i - 1][cost][max]) % mod;
                    // last element is the largest
                    if (cost != 0) {
                        long sum = 0;
                        for (int prevMax = 0; prevMax < max; prevMax++) {
                            sum += dp[i - 1][cost - 1][prevMax];
                            sum %= mod;
                        }
                        dp[i][cost][max] = (dp[i][cost][max] + sum) % mod;
                    }
                }
            }
        }

        long ans = 0;
        for (int max = 0; max < m; max++) {
            ans += dp[n - 1][k - 1][max];
            ans %= mod;
        }
        return (int) ans;
    }
}
