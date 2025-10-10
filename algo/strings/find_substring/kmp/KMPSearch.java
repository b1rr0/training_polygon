public class KMPSearch {
    
    public static int[] computeLPS(String pattern) {
        int m = pattern.length();
        int[] lps = new int[m];
        int len = 0;
        int i = 1;
        
        while (i < m) {
            if (pattern.charAt(i) == pattern.charAt(len)) {
                len++;
                lps[i] = len;
                i++;
            } else {
                if (len != 0) {
                    len = lps[len - 1];
                } else {
                    lps[i] = 0;
                    i++;
                }
            }
        }
        return lps;
    }
    
    public static int findSubstring(String text, String pattern) {
        int n = text.length();
        int m = pattern.length();
        int[] lps = computeLPS(pattern);
        
        int i = 0;
        int j = 0;
        
        while (i < n) {
            if (pattern.charAt(j) == text.charAt(i)) {
                i++;
                j++;
            }
            
            if (j == m) {
                return i - j;
            } else if (i < n && pattern.charAt(j) != text.charAt(i)) {
                if (j != 0) {
                    j = lps[j - 1];
                } else {
                    i++;
                }
            }
        }
        return -1;
    }
    
    
    public static void main(String[] args) {
        String[] testTexts = {
            "ABABDABACDABABCABCABCABCABC",
            "Hello World Hello",
            "AAAAAAA",
            "ABABABAB"
        };
        
        String[] testPatterns = {
            "ABABCAB",
            "Hello",
            "AAA",
            "ABAB"
        };
        
        System.out.println("=== KMP String Search Algorithm ===\n");
        
        for (int i = 0; i < testTexts.length; i++) {
            String text = testTexts[i];
            String pattern = testPatterns[i];
            
            System.out.println("Test " + (i + 1) + ":");
            System.out.println("Text: \"" + text + "\"");
            System.out.println("Pattern: \"" + pattern + "\"");
            
            int[] lps = computeLPS(pattern);
            System.out.print("LPS Array: ");
            for (int j = 0; j < lps.length; j++) {
                System.out.print(lps[j]);
                if (j < lps.length - 1) System.out.print(", ");
            }
            System.out.println();
            
            long startTime = System.nanoTime();
            int firstOccurrence = findSubstring(text, pattern);
            long endTime = System.nanoTime();
            
            if (firstOccurrence != -1) {
                System.out.println("First occurrence at index: " + firstOccurrence);
            } else {
                System.out.println("Pattern not found");
            }
            
            System.out.println("Time taken: " + (endTime - startTime) + " nanoseconds");
            System.out.println();
        }
    }
}