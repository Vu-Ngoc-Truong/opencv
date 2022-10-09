#include <stdio.h>
#include <opencv2/opencv.hpp>
using namespace cv;
int main(int argc, char** argv )
{
    if ( argc != 2 )
    {
        printf("usage: DisplayImage.out <Image_Path>\n");
        return -1;
    }
    Mat image;
    image = imread( argv[1], 1 );
    if ( !image.data )
    {
        printf("No image data \n");
        return -1;
    }
    namedWindow("Display Image", WINDOW_AUTOSIZE );
    imshow("Display Image", image);
    waitKey(0);
    return 0;
}

// int main()
// {
//     std::string image_path = samples::findFile("starry_night.jpg");
//     Mat img = imread(image_path, IMREAD_COLOR);
//     if(img.empty())
//     {
//         std::cout << "Could not read the image: " << image_path << std::endl;
//         return 1;
//     }
//     imshow("Display window", img);
//     int k = waitKey(0); // Wait for a keystroke in the window
//     if(k == 's')
//     {
//         imwrite("starry_night.png", img);
//     }
//     return 0;
// }