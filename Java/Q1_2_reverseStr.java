/* #########################################################################################
* Author  : Hong
* Created : 7/19/2022
* Modified: 7/19/2022
* Notes   : [1.2] Implement a function void revers(char* str) in C or C++ which reverse a
*                null-terminated string.
 ######################################################################################### */
import java.util.Stack;
public class Q1_2_reverseStr {
    String reverseString(String str){
        if (str == null || str.isEmpty()) return "";

        StringBuilder result = new StringBuilder(str);

        return result.reverse().toString();
    }

    String reverseString2(String str){ // Stack(push, pop) structer
        if (str == null || str.isEmpty()) return "";

        Stack<Character> stack = new Stack<Character>(); //character stack
        for (int i = 0, strLength = str.length(); i < strLength; ++i) stack.push(str.charAt(i));

        StringBuilder result = new StringBuilder(str.length()-1);
        while (!stack.isEmpty()) result.append(stack.pop());

        return result.toString();
    }

}
/*
Q1_2_reverseStr q1_2_reverseStr = new Q1_2_reverseStr();
System.out.println(q1_2_reverseStr.reverseString("abcde"));
System.out.println(q1_2_reverseStr.reverseString2("hong"));
 */
