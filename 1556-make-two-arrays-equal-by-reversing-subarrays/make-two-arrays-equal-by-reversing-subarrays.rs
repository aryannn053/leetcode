impl Solution {
    pub fn can_be_equal(target: Vec<i32>, arr: Vec<i32>) -> bool {
        let mut arr = arr;
        let mut target = target;
        
        arr.sort();
        target.sort();

        return arr == target
    }
}