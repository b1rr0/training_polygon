public class RabinKarpSearch {
    private static final int PRIME = 101;
    private static final int BASE = 256;
    
    public static int findSubstring(String text, String pattern) {
        int n = text.length();
        int m = pattern.length();
        int patternHash = 0;
        int textHash = 0;
        int h = 1;
        
        for (int i = 0; i < m - 1; i++) {
            h = (h * BASE) % PRIME;
        }
        
        for (int i = 0; i < m; i++) {
            patternHash = (BASE * patternHash + pattern.charAt(i)) % PRIME;
            textHash = (BASE * textHash + text.charAt(i)) % PRIME;
        }
        
        for (int i = 0; i <= n - m; i++) {
            if (patternHash == textHash) {
                int j = 0;
                while (j < m && text.charAt(i + j) == pattern.charAt(j)) {
                    j++;
                }
                if (j == m) {
                    return i;
                }
            }
            
            if (i < n - m) {
                textHash = (BASE * (textHash - text.charAt(i) * h) + text.charAt(i + m)) % PRIME;
                if (textHash < 0) {
                    textHash += PRIME;
                }
            }
        }
        return -1;
    }
    
    
    private static int calculateHash(String str, int start, int end) {
        int hash = 0;
        for (int i = start; i < end; i++) {
            hash = (BASE * hash + str.charAt(i)) % PRIME;
        }
        return hash;
    }
    
    public static void main(String[] args) {
        String[] testTexts = {
            "ABABDABACDABABCABCABCABCABC",
            "Hello World Hello",
            "AAAAAAA",
            "The quick brown fox jumps over the lazy dog"
        };
        
        String[] testPatterns = {
            "ABABCAB",
            "Hello",
            "AAA",
            "fox"
        };
        
        System.out.println("=== Rabin-Karp String Search Algorithm ===");
        System.out.println("Using BASE=" + BASE + " and PRIME=" + PRIME + "\n");
        
        for (int i = 0; i < testTexts.length; i++) {
            String text = testTexts[i];
            String pattern = testPatterns[i];
            
            System.out.println("Test " + (i + 1) + ":");
            System.out.println("Text: \"" + text + "\"");
            System.out.println("Pattern: \"" + pattern + "\"");
            
            int patternHash = calculateHash(pattern, 0, pattern.length());
            System.out.println("Pattern hash: " + patternHash);
            
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