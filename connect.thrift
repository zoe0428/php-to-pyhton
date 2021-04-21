namespace php mytest
namespace py mytest
namespace cpp mytest

typedef i32 Int  //

service Tester
{
	Int add(1:Int num1, 2:Int num2),  // 整数加法
	string merge(1:string str1, 2:string str2),  // 字符串连接
}