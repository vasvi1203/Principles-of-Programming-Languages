int fact(int i) {
	if(i <= 1)
		return 1;
	else
		return (i * fact(i - 1));
}

int main() {
	int n = 4, f;
	f = fact(n);
	return 0;
}
