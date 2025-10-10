public class ZAlgorithmSearch {
    
    public static int[] computeZArray(String s) {
        int n = s.length();
        int[] z = new int[n];
        int l = 0, r = 0;
        
        for (int i = 1; i < n; i++) {
            if (i <= r) {
                z[i] = Math.min(r - i + 1, z[i - l]);
            }
            
            while (i + z[i] < n && s.charAt(z[i]) == s.charAt(i + z[i])) {
                z[i]++;
            }
            
            if (i + z[i] - 1 > r) {
                l = i;
                r = i + z[i] - 1;
            }
        }
        
        return z;
    }
    
    public static int findSubstring(String text, String pattern) {
        if (pattern.isEmpty()) return 0;
        if (text.isEmpty() || pattern.length() > text.length()) return -1;
        
        String combined = pattern + "$" + text;
        int[] zArray = computeZArray(combined);
        int patternLength = pattern.length();
        
        for (int i = patternLength + 1; i < combined.length(); i++) {
            if (zArray[i] == patternLength) {
                return i - patternLength - 1;
            }
        }
        
        return -1;
    }
    
    
    public static void printZArray(String s, int[] zArray) {
        System.out.println("String: " + s);
        System.out.print("Index:  ");
        for (int i = 0; i < s.length(); i++) {
            System.out.printf("%2d ", i);
        }
        System.out.println();
        
        System.out.print("Char:   ");
        for (int i = 0; i < s.length(); i++) {
            System.out.printf("%2c ", s.charAt(i));
        }
        System.out.println();
        
        System.out.print("Z[i]:   ");
        for (int i = 0; i < zArray.length; i++) {
            System.out.printf("%2d ", zArray[i]);
        }
        System.out.println();
    }
    
    public static void main(String[] args) {
        String[] testTexts = {
            "ABABDABACDABABCABCABCABCABC",
            "Hello World Hello",
            "AAAAAAA",
            "ABABABAB",
            "The quick brown fox jumps over the lazy dog"
        };
        
        String[] testPatterns = {
            "ABABCAB",
            "Hello",
            "AAA",
            "ABAB",
            "fox"
        };
        
        System.out.println("=== Z Algorithm String Search ===\n");
        
        for (int i = 0; i < testTexts.length; i++) {
            String text = testTexts[i];
            String pattern = testPatterns[i];
            
            System.out.println("Test " + (i + 1) + ":");
            System.out.println("Text: \"" + text + "\"");
            System.out.println("Pattern: \"" + pattern + "\"");
            
            // Create combined string and compute Z array
            String combined = pattern + "$" + text;
            int[] zArray = computeZArray(combined);
            
            System.out.println("\nZ Array for combined string \"" + combined + "\":");
            printZArray(combined, zArray);
            
            long startTime = System.nanoTime();
            int firstOccurrence = findSubstring(text, pattern);
            long endTime = System.nanoTime();
            
            if (firstOccurrence != -1) {
                System.out.println("First occurrence at index: " + firstOccurrence);
                
                // Show the found substring
                String foundSubstring = text.substring(firstOccurrence, firstOccurrence + pattern.length());
                System.out.println("Found substring: \"" + foundSubstring + "\"");
            } else {
                System.out.println("Pattern not found");
            }
            
            System.out.println("Time taken: " + (endTime - startTime) + " nanoseconds");
            System.out.println("-".repeat(60));
            System.out.println();
        }
        
        // Demonstrate Z array computation for pattern analysis
        System.out.println("=== Z Array Analysis for Different Patterns ===\n");
        
        String[] patterns = {
            "ABABAB",
            "AABAAAB", 
            "ABCABCAB",
            "AAAA"
        };
        
        for (String pattern : patterns) {
            System.out.println("Pattern analysis for: \"" + pattern + "\"");
            int[] zArray = computeZArray(pattern);
            printZArray(pattern, zArray);
            
            // Show how Z values help in pattern matching
            System.out.println("Interpretation:");
            for (int i = 1; i < zArray.length; i++) {
                if (zArray[i] > 0) {
                    String prefix = pattern.substring(0, zArray[i]);
                    String suffix = pattern.substring(i, i + zArray[i]);
                    System.out.println("  Z[" + i + "] = " + zArray[i] + 
                                     " means prefix \"" + prefix + "\" matches suffix \"" + suffix + "\"");
                }
            }
            System.out.println();
        }
    }
}