#include <iostream>
#include <stack>
#include <windows.h>
using namespace std;

int board[9][9];

stack<pair<int,int>> hole;

void printBoard(){
    printf("=======================================================\n");
    for(int i=0; i<9; i++){
        for(int j=0; j<9; j++){
            printf("%d ", board[i][j]);
        }
        printf("\n");
    }
}

bool promising(int x, int y){
    for(int i=0; i<9; i++){
        if(board[i][y]==board[x][y] && i!=x){
            return false;
        }
        if(board[x][i]==board[x][y] && i!=y){
            return false;
        }
    }
    for(int i=x/3*3; i<x/3*3+3; i++){
        for(int j=y/3*3; j<y/3*3+3; j++){
            if((i!=x || j!=y) && board[i][j]==board[x][y]){
                return false;
            }
        }
    }
    return true;
}

void sudoku(){
    if(hole.empty()){
        for(int i=0; i<9; i++){
            for(int j=0; j<9; j++){
              printf("%d ", board[i][j]);
            }
        printf("\n");
        }
    }
    else{
        int temp_x = hole.top().first;
        int temp_y = hole.top().second;
        hole.pop();
        for(int i=1; i<=9; i++){
            board[temp_x][temp_y] = i;
            if(promising(temp_x, temp_y)){
                //printBoard();
                //Sleep(1500);
                sudoku();
            }
            board[temp_x][temp_y] = 0;
        }
        hole.push(make_pair(temp_x, temp_y));
    }
}

int main(){
    for(int i=0; i<9; i++){
        for(int j=0; j<9; j++){
            cin >> board[i][j];
            if(board[i][j]==0) hole.push(make_pair(i,j));
        }
    }

    sudoku();

    return 0;
}