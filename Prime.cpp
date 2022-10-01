#include<iostream>
using namespace std;
int main(){
	int no;
	bool flag=0;
	cout<<"Enter a Number : ";
	cin>>no;
	for(int i=0;i<no;i++){
		if(no%i==0){
			flag=1;
			break;	
		}
	}
	if(flag == 0){
		cout<<no<<" is Prime";
	}
	else{
		cout<<no<<" is not Prime";
	}
}