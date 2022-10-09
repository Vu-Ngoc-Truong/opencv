#include <opencv2/core.hpp>
#include <opencv2/imgcodecs.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/aruco.hpp>
#include <stdio.h>
#include <iostream>
using namespace cv;
using namespace std;
int main(int argc, char **argv)
{
    // if (argc != 2)
    // {
    //     printf("usage: DisplayImage.out <Image_Path>\n");
    //     return -1;
    // }
    // printf(CV_VERSION);
    // // Creat marker
    // cv::Mat markerImage;
    // cv::Ptr<cv::aruco::Dictionary> dictionary = cv::aruco::getPredefinedDictionary(cv::aruco::DICT_6X6_250);
    // cv::aruco::drawMarker(dictionary, 24, 200, markerImage, 1);
    // cv::imwrite("./marker255_1000.png", markerImage);

    /******* Get marker from image *****/
    // cv::Mat inputImage;
    // inputImage = imread("singlemarkerssource.png");

    // std::vector<int>
    //     markerIds;
    // std::vector<std::vector<cv::Point2f>> markerCorners, rejectedCandidates;
    // cv::Ptr<cv::aruco::DetectorParameters> parameters = cv::aruco::DetectorParameters::create();
    // cv::Ptr<cv::aruco::Dictionary> dictionary = cv::aruco::getPredefinedDictionary(cv::aruco::DICT_6X6_250);
    // cv::aruco::detectMarkers(inputImage, dictionary, markerCorners, markerIds, parameters, rejectedCandidates);
    // cv::Mat outputImage = inputImage.clone();
    // cv::aruco::drawDetectedMarkers(outputImage, markerCorners, markerIds);
    // cv::imshow("outputImage", outputImage);
    // waitKey(0);
    // destroyAllWindows();

    /******* Get marker from video *****/
    cv::VideoCapture inputVideo;
    inputVideo.open(0);
    cv::Ptr<cv::aruco::Dictionary> dictionary = cv::aruco::getPredefinedDictionary(cv::aruco::DICT_4X4_250);
    while (inputVideo.grab())
    {
        cv::Mat image, imageCopy;
        inputVideo.retrieve(image);
        image.copyTo(imageCopy);
        std::vector<int> ids;
        std::vector<std::vector<cv::Point2f>> corners;
        cv::aruco::detectMarkers(image, dictionary, corners, ids);
        // if at least one marker detected
        if (ids.size() > 0)
            cv::aruco::drawDetectedMarkers(imageCopy, corners, ids);
        cv::imshow("out", imageCopy);
        char key = (char)cv::waitKey(10);
        if (key == 27)
            break;
    }
    inputVideo.release();
    return 0;
}