/*
The code is used to evaluate an arithmetic expression.
It involves conversion of the expression to postfix format.
The postfix is then evluated using the postfix evaluation algorithm.
The postfix conversion and evaluation is done using Stack ADT.
I have implemented Stack ADT using Single Linked List.
*/

// Import Necessary Header Files
#include<stdio.h>
#include<stdlib.h>
#include<math.h>

// Stack Operations for Operators while Infix to Postfix Conversion
struct nodeOper {
	char data;
	struct nodeOper *next;
}*headOper=NULL;
typedef struct nodeOper nodeOper;
// Push (Insert at beginning)
void pushOper(char ch) {
	nodeOper *newnode = (nodeOper *)malloc(sizeof(nodeOper));
	newnode -> data = ch;
	newnode -> next = headOper;
	headOper = newnode;
}
// Pop (Delete from beginning)
char popOper() {
	if(headOper == NULL)
		return '\0';
	char ch = headOper -> data;
	nodeOper *temp = headOper;
	headOper = headOper -> next;
	free(temp);
	return ch;
}
// Function Returns the top element of the stack
char topOper() {
	return headOper -> data;
}

// Stack Operations for Operands while Postfix Evaluation
struct nodeVal {
	float data;
	struct nodeVal *next;
}*headVal=NULL;
typedef struct nodeVal nodeVal;
// Push (Insert at beginning)
void pushVal(float val) {
	nodeVal *newnode = (nodeVal *)malloc(sizeof(nodeVal));
	newnode -> data = val;
	newnode -> next = headVal;
	headVal = newnode;
}
// Pop (Delete from beginning)
float popVal() {
	if(headVal == NULL)
		return 0;
	float val = headVal -> data;
	nodeVal *temp = headVal;
	headVal = headVal -> next;
	free(temp);
	return val;
}

// This Function checks if the given character is a digit
int checkNum(char ch) {
	if(ch <= '9' && ch >= '0')
		return 1;
	return 0;
}

// This function checks the precedence of characters
int precedence(char ch) {
	if(ch == '(' || ch == '{' || ch == '[')
		return 0;
	if(ch == '+' || ch == '-')
		return 1;
	if(ch == '*' || ch == '/' || ch == '%')
		return 2;
	if(ch == '^')
		return 3;
}

// Infix to Postfix Conversion
char *inToPost(char *exp) {

	// Declare the required variables
	char *postfix = (char *)calloc(100, sizeof(char));
	int j = 0;

	// Loop to iterate through infix string
	for(int i=0; exp[i] != '\0'; i++) {

		// If it is a space, skip the element
		if(exp[i] == ' ')
			continue;

		// If it is a number, add it to postfix string
		else if(checkNum(exp[i]))
			postfix[j++] = exp[i];

		// If it is an operator...
		else {

			// If it is a closing bracket, pop all the elements till opening bracket
			if(exp[i] == ')') {
				while(topOper() != '(') {
					if(postfix[j] != ' ')
						postfix[j++] = ' ';
					postfix[j++] = popOper();
					postfix[j++] = ' ';
				}
				popOper();
			}
			else if(exp[i] == '}') {
				while(topOper() != '}') {
					if(postfix[j] != ' ')
						postfix[j++] = ' ';
					postfix[j++] = popOper();
					postfix[j++] = ' ';
				}
				popOper();
			}
			else if(exp[i] == ']') {
				while(topOper() != '[') {
					if(postfix[j] != ' ')
						postfix[j++] = ' ';
					postfix[j++] = popOper();
					postfix[j++] = ' ';
				}
				popOper();
			}

			// If stack is empty, exp[i] is opening bracket or if the precedence of new character is greater than previous character, push exp[i]
			else if( headOper == NULL || precedence(exp[i]) == 0 || precedence(exp[i]) > precedence(headOper->data) ) {
				if(precedence(exp[i]) != 0)
					postfix[j++] = ' ';
				pushOper(exp[i]);
			}

			// Else pop the elements till precence of new character is less than or equal to top element of stack then push exp[i]
			else {
				while(headOper != NULL && precedence(exp[i]) <= precedence(topOper())) {
					if(postfix[j] != ' ')
						postfix[j++] = ' ';
					postfix[j++] = popOper();
					postfix[j++] = ' ';
				}
				pushOper(exp[i]);
			}
		}
	}

	// Pop all elements from stack and add it to postfix string
	while(headOper != NULL) {
		if(postfix[j] != ' ')
			postfix[j++] = ' ';
		postfix[j++] = popOper();
		postfix[j++] = ' ';
	}

	// Assign NULL character at the end of string
	postfix[j++] = '\0';

	// Return the postfix string
	return postfix;
}

// Postfix Evaluation
float postfixEval(char *postfix) {

	// Declare the required variables
	int j;
	float a, b;
	char operator, *ch;

	// Loop to iterate the postfix string
	for(int i = 0; postfix[i] != '\0'; i++) {

		// If it is a string, skip the iteration
		if(postfix[i] == ' ')
			continue;

		// If it is a digit...
		else if(checkNum(postfix[i])) {
			j = 0;
			ch = (char *)calloc(6, sizeof(char));

			// Iterate till the end of number
			while(checkNum(postfix[i]))
				ch[j++] = postfix[i++];
			i--;
			ch[j++] = '\0';

			// Convert to float and push it to the stack
			pushVal(atof(ch));
		}

		// If it is an Operator...
		else {
			
			// Assign operator to a variable, pop two elements from stack
			operator = postfix[i];
			b = popVal();
			a = popVal();

			// Check the operator, do the necessary operation and push the result to the stack
			if(operator == '+') pushVal(a + b);
			if(operator == '-') pushVal(a - b);
			if(operator == '*') pushVal(a * b);
			if(operator == '/') pushVal(a / b);
			if(operator == '%') pushVal((float)((int)a % (int)b));
			if(operator == '^') pushVal(pow(a, b));
		}
	}

	// Return the resulting float value
	return headVal -> data;
}

int main() {

	// Declare the required variables
	char exp[100], *postfix;
	float result;

	// Take the infix as string input
	printf("Enter an infix expression : ");
	scanf("%[^\n]s", exp);

	// Convert infix to postfix and display it
	postfix = inToPost(exp);
	printf("Postfix : %s\n", postfix);

	// Evaluate the postfix expression and display the result
	result = postfixEval(postfix);
	printf("Result : %.2f\n", result);
}