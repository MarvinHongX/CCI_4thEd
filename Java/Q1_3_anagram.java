/* #########################################################################################
* Author  : Hong
* Created : 7/19/2022
* Modified: 7/19/2022
* Notes   : [1.3] Given two strings, write a method to decide if one is a permutation of
*                the other
 ######################################################################################### */
import java.util.Arrays;
public class Q1_3_anagram {
    boolean anagram1(String str1, String str2){
        if (str1 == null || str1.isEmpty() || str2 == null || str2.isEmpty()) return false;
        if (str1.length() != str2.length()) return false;

        char[] ch1 = str1.toCharArray();
        char[] ch2 = str2.toCharArray();
        Arrays.sort(ch1);
        Arrays.sort(ch2);

        return String.valueOf(ch1).equals(String.valueOf(ch2));
    }

    boolean anagram2(String str1, String str2){
        if (str1 == null || str1.isEmpty() || str2 == null || str2.isEmpty()) return false;
        if (str1.length() != str2.length()) return false;

        int[] checker = new int[256]; // 0~255 (Extended ASCII)
        for (int i = 0, strLength = str1.length(); i < strLength; ++i) ++checker[str1.charAt(i)];
        for (int i = 0, strLength = str2.length(); i < strLength; ++i) {
            if (--checker[str2.charAt(i)] < 0) return false;
        }

        return true;
    }
}
/*
Q1_3_anagram q1_3_anagram = new Q1_3_anagram();
System.out.println(q1_3_anagram.anagram1("elvis", "lives"));
System.out.println(q1_3_anagram.anagram1("basic", "is abd"));
System.out.println(q1_3_anagram.anagram1("ba1", "1ab"));

System.out.println(q1_3_anagram.anagram2("elvis", "lives"));
System.out.println(q1_3_anagram.anagram2("basic", "is abd"));
System.out.println(q1_3_anagram.anagram2("ba1", "1ab"));

 */