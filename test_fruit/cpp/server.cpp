#include "ros/ros.h"
#include "yh_tuto_service/yh_srv.h"    //서비스를 사용하니까 서비스 파일.h
 
 
bool calculation(yh_tuto_service::yh_srv::Request &req, yh_tuto_service::yh_srv::Response &res) //req, res선언
//                패키지이름 , 서비스파일이름, 요청      ,                          응답
//메세지파일에 요청 응답이 나뉘어 있음
{
    res.result = req.a + req.b;  //메시지파일에 있는 변수
 
    ROS_INFO("request : x = %ld, y = %ld",(long int)req.a, (long int)req.b);
    
    ROS_INFO("sending back response : %ld",(long int)res.result);
 
    return true;    // bool형이기때문에 return이 true
}                 // 함수 만들기
 
 
//main 문 만들기
 
int main(int argc, char **argv)
{
    ros::init(argc, argv, "srv_server");  // 초기화
    ros::NodeHandle nh;  // 노드핸들 선언
 
    ros::ServiceServer server = nh.advertiseService("hamburger", calculation);
 
    ROS_INFO("ready srv server!!");
 
    ros::spin();   //요청이 올때까지 기다린다.spin 
 
    return 0;
}
