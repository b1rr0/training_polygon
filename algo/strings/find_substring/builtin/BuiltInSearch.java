import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class BuiltInSearch {
    
    public static int findSubstring(String text, String pattern) {
        return text.indexOf(pattern);
    }
    
    
    
    public static boolean contains(String text, String pattern) {
        return text.contains(pattern);
    }
    
    public static void main(String[] args) {
        String[] testTexts = {
            "ABABDABACDABABCABCABCABCABC",
            "Hello World Hello World",
            "AAAAAAA",
            "Java is great, Java is powerful, Java is everywhere"
        };
        
        String[] testPatterns = {
            "ABABCAB",
            "World",
            "AAA",
            "Java"
        };
        
        System.out.println("=== Built-in String Search Methods ===\n");
        
        for (int i = 0; i < testTexts.length; i++) {
            String text = testTexts[i];
            String pattern = testPatterns[i];
            
            System.out.println("Test " + (i + 1) + ":");
            System.out.println("Text: \"" + text + "\"");
            System.out.println("Pattern: \"" + pattern + "\"");
            
            // Test contains method
            long startTime1 = System.nanoTime();
            boolean found = contains(text, pattern);
            long endTime1 = System.nanoTime();
            System.out.println("Contains: " + found + " (Time: " + (endTime1 - startTime1) + " ns)");
            
            // Test indexOf method
            long startTime2 = System.nanoTime();
            int firstOccurrence = findSubstring(text, pattern);
            long endTime2 = System.nanoTime();
            
            if (firstOccurrence != -1) {
                System.out.println("First occurrence (indexOf): " + firstOccurrence + 
                                 " (Time: " + (endTime2 - startTime2) + " ns)");
                
            } else {
                System.out.println("Pattern not found");
            }
            
            System.out.println();
        }
        
        // Demonstrate other string methods
        System.out.println("=== Other Built-in String Methods ===");
        String demoText = "The quick brown fox jumps over the lazy dog";
        String demoPattern = "the";
        
        System.out.println("Text: \"" + demoText + "\"");
        System.out.println("Pattern: \"" + demoPattern + "\"");
        
        // Case sensitive
        System.out.println("Case sensitive indexOf: " + demoText.indexOf(demoPattern));
        
        // Case insensitive
        System.out.println("Case insensitive indexOf: " + 
                         demoText.toLowerCase().indexOf(demoPattern.toLowerCase()));
        
        // Last occurrence
        System.out.println("Last occurrence: " + demoText.lastIndexOf(demoPattern));
        
        // Starts with / ends with
        System.out.println("Starts with 'The': " + demoText.startsWith("The"));
        System.out.println("Ends with 'dog': " + demoText.endsWith("dog"));
    }
}