
class ListNode {
    val: number;
    next: ListNode | null;
    constructor(val,next: ListNode | null = null) {
        this.val = val;
        this.next = next;
    }

}

function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
    
  const dummyHead = new ListNode(0);
  let curr = dummyHead;
  let carry = 0;
  while (l1 !== null || l2 !== null || carry !== 0) {
      const x = l1 ? l1.val : 0;
      const y = l2 ? l2.val : 0;
      const sum = carry + x + y;
      carry = Math.floor(sum/10);
      curr.next = new ListNode(sum % 10)
      curr = curr.next;

      if (l1 !== null) l1 = l1.next;
      if (l2 !== null) l2 = l2.next;
  }
  
  return dummyHead.next

};

const arr2List = (arr: number[], List) => {
  
    return arr.reduce((acc, curr) => {
      if (acc == null) {
        acc = new List(curr)
      } else {
        acc = new List(curr, acc)
      }
      return acc;
    }, null)
  }
  
const a1 = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
const a2 = [5,6,4]

const l1 = arr2List(a1.reverse(), ListNode);
const l2 = arr2List(a2.reverse(), ListNode);
const r = addTwoNumbers(l1, l2);