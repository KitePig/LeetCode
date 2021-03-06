# [1. 两数之和](https://leetcode-cn.com/problems/two-sum/)


## 题目大意
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

你可以按任意顺序返回答案。

### 我的题解:
```
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer[]
     */
    function twoSum($nums, $target) {
        $count = count($nums);
        $result = [];
        for ($i = 0; $i < $count; $i++){
            for ($j = 0; $j < $count; $j++){
                if($i === $j){
                    continue;
                }
                $tmp = $nums[$i] + $nums[$j];
                if($tmp === $target){
                    $result = [$i, $j];
                    break;
                }
            }
        }

        return $result;
    }
}
```

## 解题思路
双层for循环，不是最优解
