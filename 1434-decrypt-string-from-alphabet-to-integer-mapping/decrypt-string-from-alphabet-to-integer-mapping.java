class Solution {
    public String freqAlphabets(String s) {

        StringBuilder sb = new StringBuilder();
        int n = s.length();
        int i=0;

        while(i<n){
            
            if(i+2 < s.length() && s.charAt(i+2) == '#'){
                String str = s.substring(i,i+2);
                int temp = Integer.parseInt(str);
                char ch = (char)(temp+96);
                sb.append(ch);
                i=i+3;
            } 
            else {
                char ch = s.charAt(i);
                int temp = Character.getNumericValue(ch);
                char letsee = (char)(temp+96);
                sb.append(letsee);
                i=i+1;
               
            }

        }
        return sb.toString();
    }
}