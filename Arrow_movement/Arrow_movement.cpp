#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <conio.h>

#define DIM 20

struct Player{
	int x=DIM/2;
	int y=DIM/2;
};

void draw_dungeon(char dungeon[DIM][DIM], int px, int py);
void tooltip();

int main(){
	int key;
	bool flag=false;
	Player p;
	
	char dungeon[DIM][DIM];
	
	//creazione e prima stampa
	for(int i=0; i<DIM; i++){
		for(int j=0; j<DIM; j++){
			if(i==0 || i==DIM-1 || j==0 || j==DIM-1){
				dungeon[i][j]='#';
			}
			else{
				dungeon[i][j]='.';
			}
			if(i==DIM/2 && j==DIM/2){
					dungeon[i][j]='@';
			}
			putchar(dungeon[i][j]);
		}
		printf("\n");
	}
	tooltip();

	
	
	while(key!='q'){
		key=getch();
		if(flag==false){
			if(key==224){
				flag=true;
			}
		}
		else{
			switch(key){
				case 72:{			//UP 
					p.y--;
					system("cls");
					draw_dungeon(dungeon, p.x, p.y);
					tooltip();
					break;
				}
				case 75:{			//LEFT
					p.x--;
					system("cls");
					draw_dungeon(dungeon, p.x, p.y);
					tooltip();
					break;
				}
				case 77:{			//RIGHT
					p.x++;
					system("cls");
					draw_dungeon(dungeon, p.x, p.y);
					tooltip();
					break;
				}
				case 80:{			//DOWN
					p.y++;
					system("cls");
					draw_dungeon(dungeon, p.x, p.y);
					tooltip();
					break;
				}
			}
			flag=false;
		}
	}
	return 0;
}


void draw_dungeon(char dungeon[DIM][DIM], int px, int py){
	for(int i=0; i<DIM; i++){
		for(int j=0; j<DIM; j++){
			if(i==0 || i==DIM-1 || j==0 || j==DIM-1){
				dungeon[i][j]='#';
			}
			else{
				dungeon[i][j]='.';
			}
			if(i==py && j==px){
				dungeon[i][j]='@';
			}
			putchar(dungeon[i][j]);
		}
		printf("\n");
	}
}


void tooltip(){
	printf("\nUse the arrow keys to move.\nUse \'q\' to quit.");
}






