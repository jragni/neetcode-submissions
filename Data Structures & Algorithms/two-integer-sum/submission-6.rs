use std::collections::HashMap;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut seen = HashMap::new();
        
        for (i, &n) in nums.iter().enumerate() {
            let potential = target - n;
            if let Some(&j) = seen.get(&potential) {
                return vec![j as i32, i as i32];
            }
            seen.insert(n, i);
        }
        vec![]
    }
}
