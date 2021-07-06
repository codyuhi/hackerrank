if(nums.length === 1) {
    return nums[0];
}
for(let i = 0; i < nums.length; i++) {
    nums[i] = parseInt(nums[i]);
}
nums.sort((a, b) => a - b);
let newNums = [];
for(let i = 1; i < nums.length; i++) {
    if(nums[i] === nums[i - 1]) {
        continue;
    }
    newNums.push(nums[i]);
}
return newNums[newNums.length - 2];