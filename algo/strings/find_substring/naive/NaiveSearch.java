public class NaiveSearch {
    
    public static int findSubstring(String text, String pattern) {
        int n = text.length();
        int m = pattern.length();
        
        for (int i = 0; i <= n - m; i++) {
            int j = 0;
            while (j < m && text.charAt(i + j) == pattern.charAt(j)) {
                j++;
            }
            if (j == m) {
                return i;
            }
        }
        return -1;
    }
    
    
    public static void main(String[] args) {
        String[] testTexts = {
            "ABABDABACDABABCABCABCABCABC",
            "Hello World",
            "AAAAAAA",
            "ABCDEFGHIJKLMNOP"
        };
        
        String[] testPatterns = {
            "ABABCAB",
            "World",
            "AAA",
            "XYZ"
        };
        
        System.out.println("=== Naive String Search Algorithm ===\n");
        
        for (int i = 0; i < testTexts.length; i++) {
            String text = testTexts[i];
            String pattern = testPatterns[i];
            
            System.out.println("Test " + (i + 1) + ":");
            System.out.println("Text: \"" + text + "\"");
            System.out.println("Pattern: \"" + pattern + "\"");
            
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