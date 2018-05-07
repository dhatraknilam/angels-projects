int Solution::pow(int x, int n, int d) {
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details
    // int t;
//   long long t=1; 
    // t=power(x,n)%d;
     long long t=1, y=x,b=n; 
    while (b > 0) {
        if (b%2 == 1) {
            t = (t*y) % d; // multiplying with base
        }
        y = (y*y) % d; // squaring the base
        b /= 2;
    }
    t= t % d;
    if(t<0)
        t=t+d;
    // cout << t;
    return t;
    
}
