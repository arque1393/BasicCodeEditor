#include<stdio.h>
#include<stdlib.h>
int main(){
    int i, c,p;
    char state[10]={'T','T','T','T','T'};
    char chop[10]={'F','F','F','F','F'};
    while(1)	{
    for(i=0;i<5;i++)
        printf("Index= %d \tState= %c \tChopstick= %c \n",i,state[i],chop[i]);
    printf("\nThe philosopher wants to perform the following state:\n1.Eating\n2.Eating completed\n3.Exit");
    printf("\nEnter your choice:");
    scanf("%d", &c);
    
        switch(c)    {
            case 1: printf("\nEnter the philosopher number who wants to eat: ");
                    scanf("%d", &p);
                    if(state[p]=='T' && chop[p]=='F' && chop[(p+1)%5]=='F')
                    {
                        state[p]='E';
                        chop[p]=chop[(p+1)%5]='B';
                    }
                    else if(state[p]=='T')
                    {
                        state[p]='H';
                    }
                    else
                    {
                        printf("\nThe philosopher is either eating or hungry state.");
                    }
                    break;
            case 2: printf("\nEnter the philosopher number who wants to eat: ");
                    scanf("%d", &p);
                    if(state[p]=='E' && chop[p]=='B' && chop[(p+1)%5]=='B')
                    {
                        state[p]='T';
                        chop[p]=chop[(p+1)%5]='F';
                        if(state[(p+1)%5]=='H' && chop[(p+2)%5]=='F')
                        {
                            state[(p+1)%5]='E';
                            chop[(p+1)%5]=chop[(p+2)%5]='B';
                        }
                        if(p==0)
                        {
                            p=5;
                        }
                        if(state[p-1]=='H' && chop[p-1]=='F')
                        {
                            state[p-1]='E';
                            chop[p-1]=chop[p%5]='B';
                        }
                    }
                    else
                    {
                        printf("\nThe philosopher is either eating or hungry state.");
                    }
                    break;
            case 3:exit(0);
            default: printf("Wrong choice!!");
        }
    }
    


}