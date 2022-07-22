/* #########################################################################################
* Author  : Hong
* Created : 7/19/2022
* Modified: 7/19/2022
* Notes   : [1.5] Implement a method to perform basic string compression using the counts
*                of repeated characters. For example, the string aabcccccaaa would become
*                a2blc5a3. If the "compressed" string would not become smaller than the original
*                string, your method should return the original string.
 ######################################################################################### */
public class Q1_5_stringComp {
    String compressword(String str){
        if (str == null || str.isEmpty()) return str;

        char buffer = ' ';
        int repeat = 0;
        StringBuilder result = new StringBuilder();
        for (int i = 0, strLength = str.length(); i < strLength; ++i){
            char ch = str.charAt(i);
            if (buffer == ' ') buffer = ch;

            if (buffer == ch){
                repeat++;
            }else{
                result.append(buffer);
                result.append(repeat);
                repeat = 1;
                buffer = ch;
            }
        }
        result.append(buffer);
        result.append(repeat);

        return (str.length() <= result.toString().length()) ? str : result.toString();
    }
}
/*
Q1_5_stringComp q1_5_stringComp = new Q1_5_stringComp();

System.out.println(q1_5_stringComp.compressword("abbbbccddeeeee"));
 */
