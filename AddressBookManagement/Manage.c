#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//struct
typedef struct Node {
	char line[80];
	char name[10], address[50], number[20];
	struct Node* next;
}NODE;

//NODE FUNC
/*
//create   : 노드 생성                 --- ok
//setting  : 파일 읽음                 --- ok
//split    : 정보 분할                 --- ok
//count    : 노드 개수 (head 제외)     --- ok
//compare  : 노드 비교 후 교환         --- ok
//sort     : 전체 정렬                 --- ok
//print    : 전체 정보 출력            --- ok
//add      : 정보 추가                 --- ok
//upload   : 수정/삭제 후 파일 업로드  --- ok
//find     : 회원 이름으로 정보 탐색   --- ok
//search   : 정보 탐색 후 출력         --- ok
//rewrite  : 정보 수정                 --- ok
//delete   : 회원 삭제                 --- ok
*/

//create
NODE* create(NODE* head) {
	NODE* newnode = (NODE*)malloc(sizeof(NODE));
	NODE* horse = head;
	while (horse->next!=NULL){
		horse=horse->next;
	}
	newnode->next = NULL;
	horse->next = newnode;
	return newnode;
}

//split
void split(NODE* node){
	char tmp[3][50], tmpline[80];
	strcpy(tmpline,node->line);
	char * ptr = strtok(tmpline," ");
	for (int i=0; ptr != NULL; i++){
		strcpy(tmp[i],ptr);
		ptr = strtok(NULL," ");
	}
	strcpy(node->name,tmp[0]);
	strcpy(node->address,tmp[1]);
	strcpy(node->number,tmp[2]);
}

//setting
void setting(NODE* head){
	char line[80];
	FILE * fp = fopen("스플럭 명단관리.txt","rt");
	if (fp==NULL){
		printf("ERROR: 파일을 열지 못함\n");
		return;
	}
	//create
	while(fgets(line,sizeof(line),fp)!=NULL){
		NODE * tmp = create(head);
		strcpy(tmp->line,line);
	}
	fclose(fp);
	//split
	NODE* horse = head;
	while (horse!=NULL){
		split(horse);
		horse=horse->next;
	}
}

//count
int count(NODE* head){
	int cnt = 0;
	NODE* horse = head;
	while (horse->next!=NULL){
		cnt++;
		horse=horse->next;
	}
	return cnt;
}

//compare
void compare(NODE* current, NODE* cmp1, NODE* cmp2){
	if (strcmp(cmp1->name,cmp2->name)>0){
		NODE* tmp = cmp1;
		tmp->next = cmp2->next;
		cmp2->next = tmp;
		current->next = cmp2;
		cmp1=NULL;
	}
}

//sort
void sort(NODE* head){
	int nodecnt = count(head);
	for (int i=1; i<nodecnt; i++){
		NODE* horse = head;
		for (int j=0; j<nodecnt-i; j++){
			compare(horse,horse->next,horse->next->next);
			horse = horse->next;
		}
	}
}

//print
void print(NODE* head){
	NODE* horse = head->next;
	for (int i=1; horse !=NULL; i++){
		printf("[%d]\n",i);
		printf("name: %s\n",horse->name);
		printf("address: %s\n",horse->address);
		printf("number: %s\n",horse->number);
		horse=horse->next;
	}
}

//add
void add(NODE* head){
	NODE * newnode = create(head);
	FILE* fp = fopen("스플럭 명단관리.txt","at");
	if (fp==NULL){
		printf("ERROR: 파일을 열지 못함\n");
		return;
	}
	printf("--[이름 주소 전화번호] 입력--\n");
	scanf(" %[^\n]s",newnode->line);
	fprintf(fp,"%s\n",newnode->line);
	split(newnode);
	printf("============================\n");
	printf("추가되었습니다.\n");
	fclose(fp);
}

//search
void search(NODE* head){
	char searchfor[50];
	printf("검색할 내용을 입력하세요: ");
	scanf("%s",searchfor);
	printf("\n============================\n\n");
	NODE* horse = head;
	int cnt = 0;
	while(horse!=NULL){
		char* ptr = strstr(horse->line,searchfor);
		if (ptr!=NULL){
			cnt++;
			printf("---회원 정보---\n");
			printf("이름: %s\n",horse->name);
			printf("주소: %s\n",horse->address);
			printf("전화번호: %s\n",horse->number);
		}
		horse = horse->next;
	}
	if (cnt==0){
		printf("검색한 내용에 해당되는 회원 정보가 없습니다.\n");
	}
}

//upload
void upload(NODE* head, NODE* tmp){
	FILE* fp = fopen("스플럭 명단관리.txt","w");
	NODE* horse = head;
	while (horse!=NULL){
		if (horse==tmp){
			fprintf(fp,"%s\n",horse->line);
		}
		else{
			fprintf(fp,"%s",horse->line);
		}
		horse = horse->next;
	}
	fclose(fp);
}

//find
NODE* find(NODE* head){
	char name[10];
	scanf("%s",name);
	NODE* horse = head;
	while(horse!=NULL){
		if (strcmp(horse->name,name)==0){
			break;
		}
		horse = horse->next;
	}
	if (horse == NULL){
		printf("해당 이름의 회원 정보가 없습니다.");
	}
	return horse;
}

//rewrite
NODE* rewrite(NODE* head){
	char tmp[80], yn;
	printf("수정할 회원의 이름을 입력하세요: ");
	NODE* renode = find(head);
	if (renode==NULL){
		return NULL;
	}
	//modify
	printf("--[이름 주소 전화번호] 입력--\n");
	scanf(" %[^\n]s",tmp);
	printf("저장하시겠습니까? (y/n): ");
	scanf(" %c",&yn);
	if ((yn=='Y')||(yn=='y')){
		strcpy(renode->line,tmp);
		split(renode);
		printf("저장되었습니다.\n");
		return renode;
	}
	printf("취소되었습니다.\n");
}

//delete
void delete(NODE* head){
	if (head == NULL){
		printf("리스트가 비어있습니다.\n");
		return;
	}
	printf("삭제할 회원의 이름을 입력하세요: ");
	NODE* renode = find(head);
	if (renode==NULL){
		return;
	}
	char yn;
	printf("삭제하시겠습니까? (y/n): ");
	scanf(" %c",&yn);
	if ((yn=='N')||(yn=='n')){
		printf("취소되었습니다.\n");
		return;
	}
	//삭제
	NODE* horse = head;
	while(horse!=NULL){
		if (horse->next==NULL){
			if (horse==renode){
				renode=NULL;
				free(renode);
			}
			break;
		}
		if(horse->next==renode){
			horse->next=renode->next;
			renode=NULL;
			free(renode);
		}
		horse=horse->next;
	}
	printf("삭제되었습니다.\n");
}

//menu
char menu(void) {
	char option;
	printf("\n\n\t\t\t [ 메뉴 ]\n\n");
	printf("\t\t1. 모든 주소록 정보 출력\n");
	printf("\t\t2. 회원 등록\n");
	printf("\t\t3. 회원 정보 검색\n");
	printf("\t\t4. 회원 정보 수정\n");
	printf("\t\t5. 회원 삭제\n");
	printf("\t\t6. 프로그램 종료\n\n");
	printf("============================\n");
	printf("선택할 기능을 입력하세요: ");
	scanf(" %c",&option);
	printf("============================\n\n");
	return option;
}

//main
int main(void) {
	NODE* head = (NODE*)malloc(sizeof(NODE));
	head->next = NULL;
	setting(head);
	char option;
	while (1) {
		option = menu();
		switch (option) {
		case '1': 
			printf("---모든 주소록 정보 출력---\n\n");
			sort(head);
			print(head);
			break;
		case '2':
			printf("---회원 등록---\n\n");
			add(head);
			break;
		case '3': 
			printf("---회원 정보 검색---\n\n");
			search(head);
			break;
		case '4':
			printf("---회원 정보 수정---\n\n");
			NODE* tmp = rewrite(head);
			upload(head,tmp);
			break;
		case '5':
			printf("---회원 삭제---\n\n");
			delete(head);
			upload(head,NULL);
			break;
		case '6':
			printf("1초 후 프로그램 종료\n\n");
			free(head);
			sleep(1);
			exit(1);
		default:
			printf("ERROR: 다시 선택하세요.\n");
		}
	}
}
