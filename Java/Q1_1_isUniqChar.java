/* #########################################################################################
* Author  : Hong
* Created : 7/18/2022
* Modified: 7/18/2022
* Notes   : [1.1] Implement an algorithm to determine if a string has all unique characters.
*                What if you cannot use additional data structures?
*                (We'll assume that the character set is ASCII not Unicode string.)
 ######################################################################################### */
public class Q1_1_isUniqChar {
    boolean isUniqChar(String str) {     // List
        if (str == null || str.isEmpty()) return false;
        if (str.length() > 256) return false;

        boolean[] hash = new boolean[256]; // 0~255 (Extended ASCII)

        for (int i = 0, strLength = str.length(); i < strLength; ++i) {
            char ch = str.charAt(i);
            if (hash[ch]) return false;
            else hash[ch] = true;
        }
        return true;
    }

    // Assume that the string only uses the lowercase letters a through z
    boolean isUniqChar2(String str) { // Bitwise operation
        if (str == null || str.isEmpty()) return false;
        if (str.length() > 256) return false;

        int checker = 0;

        for (int i = 0, strLength = str.length(); i < strLength; ++i) {
            int val = str.charAt(i) - 'a';
            if ((checker & (1 << val)) > 0) return false;
            else checker |= (1 << val);
        }
        return true;
    }
}

/*
Q1_1_isUniqChar q1_1_isUniqChar = new Q1_1_isUniqChar();

System.out.println(q1_1_isUniqChar.isUniqChar("abcda"));
System.out.println(q1_1_isUniqChar.isUniqChar("abcde"));
System.out.println(q1_1_isUniqChar.isUniqChar("apple"));

System.out.println(q1_1_isUniqChar.isUniqChar2("abcda"));
System.out.println(q1_1_isUniqChar.isUniqChar2("abcde"));
System.out.println(q1_1_isUniqChar.isUniqChar2("apple"));
 */