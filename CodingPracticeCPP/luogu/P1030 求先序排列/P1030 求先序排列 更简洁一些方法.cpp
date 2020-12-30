//代码很短 很容易理解
//后序的最后一个是根
//先序是先输出数的根 那就找一次输出一次
//然后继续找出左树和右树
//之道空树时停止 
//P1030 luogu
//DinnerHunt
//P1030 luogu
//DinnerHunt
#include <iostream>
using namespace std;
string in_str,post_str;
void build(int l1,int r1,int l2,int r2)        //当前树的在中序遍地的范围 l1-r1  在后序遍地的范围 l2-r2
{
    if(l1>r1) return;                        //当前为空树 则直接返回
    cout << post_str[r2];                    //后序遍地的最后一个一定是节点的根，输出根的值
    int p = l1;                                
    while(in_str[p] != post_str[r2]) p++;    //从中序遍地中找出左树的范围
    int cnt = p-l1;                            //左树节点有多少个
    build(l1,p-1,l2,l2+cnt-1);                //递归遍地左树 中序（从l1开始的p-1个，因为当前节点不算左树部分） 后序（与左树类似，但右边部分不能用p-1，自己思考下为什么）
    build(p+1,r1,l2+cnt,r2-1);                //递归遍地右树 中序（从p+1开始，刚好接上左树部分到末尾） 后序（刚好接上后序的左树部分，因为根在结尾所以中间不必减1，最后减1）
}
int main(){
    ios::sync_with_stdio(false);            //加速
    cin  >> in_str >> post_str;                //中序和后序
    int n=in_str.length()-1;                //长度
    build(0,n,0,n);                            
}