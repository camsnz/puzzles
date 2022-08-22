import _ from "lodash";

export const jumpByIteration = (nums:number[]) => {
    const len = nums.length;
    if(len == 0 || len == 1) {
        return true;
    }
    let farthestIdx = 0;
    for(let i=0; i<len && farthestIdx >= i; i++) {
        if(i + nums[i] >= len-1) {
            return true;
        }
        farthestIdx = Math.max(farthestIdx, i + nums[i]);
    }
    return false;
}

type NumBoolMap = {[key:number]:boolean};

const recurse = (nums:number[], numIdx:number, visited:NumBoolMap):boolean => {
    if(visited[numIdx]===true) {
        return false;
    }
    visited[numIdx] = true;

    const numVal = nums[numIdx];
    if(nums.length-1 <= numIdx + numVal) {
        return true;
    }

    if(numVal == 0) {
        return false;
    }

    for(let i=numIdx+1; i<=numIdx+numVal; i++) {
        if(recurse(nums, i, visited)) {
            return true;
        }
    }

    return false;
}

export const jumpByRecursion = (nums:number[]):boolean => {
    const len = nums.length;
    if(len <= 1) {
        return true;
    }
    const visited:NumBoolMap = {};
    return recurse(nums, 0, visited);
}

