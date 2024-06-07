public class Array {
    public static void main(String[]args) {
        int[] numbers = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,
        37,38,39,40,41,42,43,44,45,46,47,48,49,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70};

        //        find missing number

        int n = numbers.length + 1;
        int sum = (n*(n+1))/2;
        for(int i=0; i<numbers.length;i++){
            sum = sum - numbers[i];
        }
        System.out.println("missing number is : " + sum);

        // Print the elements of the array in reverse order
        System.out.println("Original array:");
        for (int number : numbers) {
            System.out.print(number + " ");
        }

        System.out.println("\nArray in reverse order:");
        for (int i = numbers.length - 1; i >= 0; i--) {
            System.out.print(numbers[i] + " ");
        }
    }
}