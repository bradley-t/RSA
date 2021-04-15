from Crypto.Util import number

def gcd( a, b ):
    ''' Calculate GCD of a and b '''
    while ( b != 0 ):
        temp = b
        b = a % b
        a = temp
    return a

def extended_gcd( a, b ):
    ''' Extended Euclids Algorithm '''
    old_r, r = ( a, b )
    old_s, s = ( 1, 0 )
    old_t, t = ( 0, 1 )
    
    while ( r != 0 ):
        quotient = old_r // r
        old_r, r = ( r, old_r - quotient * r )
        old_s, s = ( s, old_s - quotient * s )
        old_t, t = ( t, old_t - quotient * t )

    return (old_r, old_s, old_t)

def mod_inv( a, n ):
    '''
    Find modular inverse of a mod n if exists.
    This is a slight modification to extended euclids algorithm.
    @return inverse of a mod n or None   
    '''
    old_t, t = ( 0, 1 )
    old_r, r = ( n, a )

    while ( r != 0 ):
        quotient = old_r // r
        old_r, r = ( r, old_r - quotient * r )
        old_t, t = ( t, old_t - quotient * t )

    if old_r > 1:
        return None

    if old_t < 0:
        old_t = old_t + n

    return old_t


def mod_exp( base, exp, N ):
    ''' Calculate base ^ exp mod N '''
    if N == 1:
        return 0
    result = 1
    base = base % N
    while ( exp > 0 ):
        if ( exp % 2 == 1 ):
            result = ( result * base ) % N
        exp = exp >> 1
        base = ( base * base ) % N
    return result

def mod_exp_r( x, y, N ):
    ''' Calculate x ^ y mod N recursively '''
    if y == 0: #base case
        return 1
    z = mod_exp_r( x, y // 2, N ) # recursive call
    if ( y % 2 ) == 0: # y is even case
        return pow( z, 2 ) % N
    else: # y is odd case
        return ( x * pow( z, 2 ) ) % N

def random_large_prime( N ):
    ''' return an N-bit prime number '''
    return number.getPrime( N )

