import java.util.HashMap;
import java.util.Map;

// Hashmap solution: O(n) runtime, O(n) memory usage
public class Solution2 {
    public int[] twoSum(int[] nums, int target) {
        // { [val needed] : index }
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (map.containsKey(nums[i])) {
                return new int[] { map.get(nums[i]), i };
            } else {
                map.put(target - nums[i], i);
            }
        }
        return new int[] { -1, -1 };
    }
}
