#include <opencv2/core.hpp>
#include <opencv2/imgcodecs.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/core/utility.hpp>
#include <iostream>
using namespace cv;
int main()
{
    Mat img = imread("aruco_1.png", IMREAD_COLOR);
    if (img.empty())
    {
        std::cout << "Could not read the image: "
                  << "aruco_1" << std::endl;
        return 1;
    }
    imshow("Display window", img);
    int k = waitKey(0); // Wait for a keystroke in the window
    if (k == 's')
    {
        imwrite("starry_night.png", img);
    }
    return 0;
}