const longestSubstringLength = (s) => {
  const n = s.length;
  const mp = {};
  let pointer = 0;
  let res = 0;
  for (let j = 0; j<n; j++) {
    const char = s[j]
    if (mp[char]) {
      pointer = Math.max(pointer, mp[char])
    }
    res = Math.max(res, j - pointer + 1)
    mp[char] = j +1
  }
  return res;
}

const res = longestSubstringLength('abcabcbb');
console.log(res)