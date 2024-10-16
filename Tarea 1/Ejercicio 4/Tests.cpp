#include <gtest/gtest.h>


using namespace std;


TEST(sumaTest, suma){
    double a = 1;
    double b = 2;
    double c = a + b;
    EXPECT_DOUBLE_EQ(3.0, c);
}

int main(int argc, char **argv){
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}

