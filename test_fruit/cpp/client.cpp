#include "ros/ros.h"
#include "yh_tuto_service/yh_srv.h"  // 서비스파일 헤더
#include <cstdlib>   //atoll 이라는 함수를 쓰려고 넣어준 라인
 
int main(int argc, char **argv)
{
    ros::init(argc, argv, "srv_client");
    
    if(argc !=3)   // 요청시 노드이름 , 숫자1 , 숫자2로 요청하기때문에 3개가 되어야한다.(예제)
    {
        ROS_INFO("cmd : rosrun yh_tuto_service srv_client arg0 arg1");
        ROS_INFO("arg0 : double number, arg1 : double number");
        return 1;    
    }
 
    ros::NodeHandle nh;
 
    ros::ServiceClient client = nh.serviceClient<yh_tuto_service::yh_srv>("hamburger");
 
    yh_tuto_service::yh_srv srv;
 
    srv.request.a = atoll(argv[1]); //atoll은 입력되는 값을 분리하는 함수.
    srv.request.b = atoll(argv[2]);
 
    if(client.call(srv))     // 요청을 보내는곳
    {
        ROS_INFO("send srv, srv.Request.a and b : %ld, %ld", (long int)srv.request.a, (long int)srv.request.b);
        ROS_INFO("receive srv, srv.Response.result : %ld",(long int)srv.response.result);    
    }
    else
    {
        ROS_ERROR("Failed to call service");
        return 1;
    }
    return 0;
 
}
