뱅킹시스템 과제

#include <iostream>

#include <cstring>

using namespace std;

const int accSize = 10;//최대 계좌수

const int adminPassword = 0000;//관리자 암호 설정



void Menu(void);//메뉴 출력

void MakeAccount(void);//계좌개설

void Deposit(void);//입금

void Withdraw(void);//출금

void Balance(void);//잔액조회

void allBalance(void);//모든계좌 정보조회



typedef struct

{

	int accID;

	char name[20];

	int balance;

} Account;



Account accSave[accSize];

int accNum = 0;



int main(void)

{

	int select;



	while (1)

	{

		Menu();

		cout << "선택 : ";

		cin >> select;

		cout << endl;



		switch (select)

		{

		case 1:

			MakeAccount();

			break;

		case 2:

			Deposit();

			break;

		case 3:

			Withdraw();

			break;

		case 4:

			Balance();

			break;

		case 5:

			allBalance();

			break;

		case 6:

			return 0;

		default:

			cout << "올바른 선택이 아닙니다." << endl;

		}

	}

	return 0;

}



void Menu(void)

{

	cout << "-----Menu-----" << endl;

	cout << "1.계좌개설" << endl;

	cout << "2.입 금" << endl;

	cout << "3.출 금" << endl;

	cout << "4.잔액조회" << endl;

	cout << "5.모든계좌 정보 출력" << endl;

	cout << "6.프로그램 종료" << endl;

}



void MakeAccount(void)

{

	int id;

	char name[20];

	int money;



	cout << "[계좌개설]" << endl;

	cout << "계좌ID : "; cin >> id;

	cout << "이 름 : "; cin >> name;

	cout << "입금액 : "; cin >> money;

	cout << endl;



	accSave[accNum].accID = id;

	strcpy(accSave[accNum].name, name);

	accSave[accNum].balance = money;

	accNum++;

}



void Deposit(void)

{

	int id;

	int money;



	cout << "[입  금]" << endl;

	cout << "계좌ID : "; cin >> id;

	cout << "입금액 : "; cin >> money;

	for (int i = 0; i < accNum; i++)

	{

		if (accSave[i].accID == id)

		{

			accSave[i].balance += money;

			cout << "입금완료" << endl;

			return;

		}

	}

	cout << "잘못된 ID 입니다!" << endl << endl;

}



void Withdraw(void)

{

	int id;

	int money;



	cout << "[출  금]" << endl;

	cout << "계좌ID : "; cin >> id;

	cout << "출금액 : "; cin >> money;

	for (int i = 0; i < accNum; i++)

	{

		if (accSave[i].accID == id)

		{

			if (accSave[i].balance < money)

			{

				cout << "잔액이 부족합니다." << endl;

				return;

			}

			accSave[i].balance -= money;

			cout << "출금완료" << endl;

			return;

		}

	}

	cout << "잘못된 ID 입니다!" << endl << endl;

}



void Balance(void)

{

	int id;



	cout << "[잔액조회]" << endl;

	cout << "계좌ID : "; cin >> id;

	for (int i = 0; i < accNum; i++)

	{

		if (accSave[i].accID == id)

		{

			cout << "ID : " << accSave[i].accID << endl;

			cout << "이름 : " << accSave[i].name << endl;

			cout << "잔액 : " << accSave[i].balance << endl << endl;

			return;

		}

	}

	cout << "잘못된 ID 입니다!" << endl << endl;

}



void allBalance(void)

{



	int confirm_password;

	cout << "[관리자 모드]" << endl;

	cout << "Input the admin password : "; cin >> confirm_password;

	if (accNum == 0)

	{

		cout << "Bank has no account..." << endl << endl;

		return;

	}

	if (confirm_password == adminPassword)

	{

		for (int i = 0; i < accNum; i++)

		{

			cout << "ID : " << accSave[i].accID << endl;

			cout << "이름 : " << accSave[i].name << endl;

			cout << "잔액 : " << accSave[i].balance << endl << endl;

		}

	}

	else

	{

		cout << "You are not admin!!!" << endl << endl;

		return;

	}



}