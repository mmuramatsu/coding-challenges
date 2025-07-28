/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumUniqueSubarray = function (nums) {
    let elements = new Set([nums[0]]);
    let sum_elements = nums[0];
    let ans = nums[0];

    let left = 0;

    for (let right = 1; right < nums.length; right++) {
        if (elements.has(nums[right])) {
            while (nums[left] != nums[right]) {
                sum_elements -= nums[left];
                elements.delete(nums[left]);
                left += 1;
            }

            sum_elements -= nums[left];
            elements.delete(nums[left]);
            left += 1;
        }

        elements.add(nums[right]);
        sum_elements += nums[right];
        ans = Math.max(ans, sum_elements);
    }

    return ans;
};