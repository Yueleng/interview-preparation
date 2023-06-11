
class ListNode {
    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}

class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode added = new ListNode();

        int extraAdd = 0;

        ListNode pointerNode = added;
        ListNode pointerNode1 = l1;
        ListNode pointerNode2 = l2;

        do {
            int a1 = pointerNode1 == null ? 0 : pointerNode1.val;
            int a2 = pointerNode2 == null ? 0 : pointerNode2.val;

            if (a1 + a2 + extraAdd > 9) {
                pointerNode.val = a1 + a2 + extraAdd - 10;
                extraAdd = 1;
            } else {
                pointerNode.val = a1 + a2 + extraAdd;
                extraAdd = 0;
            }

            // point to next
            pointerNode1 = pointerNode1 == null ? null : pointerNode1.next;
            pointerNode2 = pointerNode2 == null ? null : pointerNode2.next;

            if (pointerNode1 != null || pointerNode2 != null) {
                pointerNode.next = new ListNode();
                pointerNode = pointerNode.next;
            }
            
        } while (pointerNode1 != null || pointerNode2 != null);

        if (extraAdd == 1) {
            pointerNode.next = new ListNode();
            pointerNode.next.val = 1;
        }

        return added;
    }
}