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

    public static int[] slowZFunction(String s) {
        int n = s.length();
        int[] z = new int[n];
        for (int i = 1; i < n; i++)
            while (i + z[i] < n && s.charAt(z[i]) == s.charAt(i + z[i]))
                z[i]++;
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
}