/* #########################################################################################
* Author  : Hong
* Created : 7/27/2022
* Modified: 7/27/2022
* Notes   : [2.2] Implement an algorithm to find the kth to last element of a singly linked list
 ######################################################################################### */
public class Q2_2_last_n_val_linkedlist {
    private int kthToLastByNode1(Node head, int k){
        if (head == null || k <= 0) return 0;

        int i = kthToLastByNode1(head.getNext(), k) + 1;
        if (i == k) System.out.println(head.getVal());
        return i;
    }
    int kthToLast1(LinkedList list, int k){
        if (list == null || k <= 0) return 0;

        Node head = list.getHead();
        return kthToLastByNode1(head, k);
    }

    Node kthToLast2(LinkedList list, int k){
        if (list == null || list.getHead() == null || k <= 0) return null;

        Node p1 = list.getHead();
        Node p2 = list.getHead();
        for (int i = 1; i < k; ++i){
            if (p2 == null) return null;
            p2 = p2.getNext();
        }
        if (p2 == null) return null;
        while (p2.getNext() != null){
            p2 = p2.getNext();
            p1 = p1.getNext();
        }
        return p1;
    }
}
/*
Q2_2_last_n_val_linkedlist q2_2_last_n_val_linkedlist = new Q2_2_last_n_val_linkedlist();

LinkedList list = new LinkedList("1");
list.add("2");
list.add("3");
list.add("4");
list.add("5");
q2_2_last_n_val_linkedlist.kthToLast1(list,2);
Node q = q2_2_last_n_val_linkedlist.kthToLast2(list,5);
if (q != null) System.out.println(q.getVal());

 */