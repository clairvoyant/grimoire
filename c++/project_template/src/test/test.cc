#include <ostream> 
#include <iostream> 

#include "CComplex.hh"


#define BOOST_TEST_MODULE CComplexTest
#define BOOST_TEST_DYN_LINK  1
#define BOOST_TEST_MAIN   1
#include <boost/test/unit_test.hpp>

BOOST_AUTO_TEST_SUITE (CComplexTest) // name of the test suite is stringtest


BOOST_AUTO_TEST_CASE( test1 )
{
    CComplex<int> c1( 1, 2 );
    CComplex<int> c2( 3, 4 );
    CComplex<int> result( 0, 0 );

    BOOST_CHECK( (c1.getReal() == 1) and (c1.getImg() == 2));

    result = c1 + c2;

    BOOST_CHECK( (result.getReal() == 4) and (result.getImg() == 6));
};





BOOST_AUTO_TEST_SUITE_END ( )
