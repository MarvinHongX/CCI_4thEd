/* #########################################################################################
* Author  : Hong
* Created : 7/27/2022
* Modified: 7/27/2022
* Notes   : [2.4] Write code to partition a linked list around a value x, such that all nodes less than x
*                come before all nodes greater than or equal to x.
 ######################################################################################### */
public class Q2_4_split_merge_linkedlist {
    LinkedList partition(LinkedList list, int key){
        Node cur = list.getHead();
        LinkedList pre = new LinkedList();
        LinkedList post = new LinkedList(Integer.toString(key));

        while (cur != null){ //split
            if (Integer.parseInt(cur.getVal()) > key){
                post.add(cur.getVal());
            }else if (Integer.parseInt(cur.getVal()) < key){
                pre.add(cur.getVal());
            }
            cur = cur.getNext();
        }

        Node preCur = pre.getHead();
        Node postCur = post.getHead();
        while (preCur.getNext() != null){
            preCur = preCur.getNext();
        }
        preCur.setNext(postCur);
        return pre;
    }
}
