
#include <bits/stdc++.h>
using namespace std;

struct move{
	int row,col,score;
};

struct Tictactoe{
	char player,cpu,board[3][3];
	Tictactoe(){
		for(int i=0;i<3;i++){
			for(int j=0; j<3;j++){
				board[i][j]=' ';
			}
		}
	}
	void show(){
		cout<<endl;
		for(int i=0;i<3;i++)
		{
			if(i){
				cout<<"-----------\n";
			}
			for(int j=0;j<3;j++)
			{
				if(j){
					cout<<"|";
				}
				cout<<' ';
				if(board[i][j]==' ')
				{
					cout<< 3 * i + j + 1;
				}
				else 
					cout<<board[i][j];
					
				cout<<' ';
			}
			cout<<endl;
		}
		cout<<endl;
	}
	
	void play()
	{
		while(true){
			cout<<"Choose your symbol(X or O): ";
			cin>>player;
			
			if(player=='X' || player=='O'){
			break;
			}
		}
		cpu = player == 'X' ? 'O' : 'X';
		if(player == 'O'){
			cputurn();
		}
		show();
		while(true)
		{
			playerturn();
			show();
			if(win()){
				cout<<"Player wins"<<endl;
				return;
			}
			else if(tie()){
				cout<<"Tie!!"<<endl;
				return; 
			}
			cout<<"Computer's Turn.............\n";
			cputurn();
			show();
				if(win()){
				cout<<"Computer wins"<<endl;
				return;
			}
			else if(tie()){
				cout<<"Tie!!"<<endl;
				return; 
			}
		}
	}
	
	void playerturn(){
		while(true)
		{
			cout<<"Enter the cell number (1-9): ";
			int cell;
			cin>>cell;
			int row = (cell-1)/3 , col = (cell-1)%3;
			if(cell >= 1 && cell <= 9 && board[row][col] == ' ')
			{
				board[row][col]=player;
				break;
			}
		}
	}
	
	bool win()
	{
		int vic[8][3] = {{0,1,2},{3,4,5},{6,7,8},{0,3,6},{1,4,7},{2,5,8},{0,4,8},{2,4,6}};
		for(int i=0;i<8;i++){
			bool win =true;
			int row1 = vic[i][0]/3, col1 = vic[i][0]%3;
			for(int j=0;j<3;j++){
				int row2 = vic[i][j]/3, col2 = vic[i][j]%3;
				if(board[row1][col1]==' ' || board[row1][col1]!=board[row2][col2]){
				win = false;
				}
			}
			if(win)
				return true;
		}
		return false;
	}
	
	bool tie(){
		if(win())
			return false;
			
		for(int i=0;i<3;i++){
			for(int j =0;j<3;j++){
				if(board[i][j]==' '){
					return false;
				}
			}
		}
		return true;
	}
	
	void cputurn(){
		move cpumove = minimax();
		board[cpumove.row][cpumove.col] = cpu;
	}
	
	move minimax(bool maxplayer = true){
		move cpumove;
		if(win()){
			if(maxplayer){
				cpumove.score = -1;
			}
			else{
				cpumove.score = 1;
			}
			return cpumove;
		}
		else if(tie()){
			cpumove.score = 0;
			return cpumove;
		}
		
		cpumove.score = maxplayer ? -2 : 2;
		for(int i =0 ; i<3; i++){
			for(int j =0 ;j<3;j++){
				if(board[i][j]==' '){
					board[i][j]= maxplayer ? cpu : player;
					move boardnow = minimax(!maxplayer);
					if(maxplayer){
						if(boardnow.score > cpumove.score){
							cpumove.score = boardnow.score;
							cpumove.row = i;
							cpumove.col = j;
						}
					}
					else{
						if(boardnow.score < cpumove.score){
							cpumove.score = boardnow.score;
							cpumove.row = i;
							cpumove.col = j;
						}
					}
					board[i][j] = ' ';
				}
			}
		}
		return cpumove;
	}
};

int main(){
	Tictactoe obj;
	obj.play();
}

