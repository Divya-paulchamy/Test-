
class Account {
    protected double balance;
    protected double interest;
    public Account(double balance) {
        this.balance = balance;
        this.interest = 0.0;
    }
    public void calculateInterest() {
        interest = balance * 0.02;

    }
    public void addInterest() {
        balance += interest;

    }
 
    public void displayBalance() {
        System.out.println("Current Balance: $" + balance);
    }

}

class SavingAccount extends Account {
    public SavingAccount(double balance) {
        super(balance);

    }
    @Override

    public void calculateInterest() {
        interest = balance * 0.04;
    }

}

class CurrentAccount extends Account {

    public CurrentAccount(double balance) {
        super(balance);
    }

 
    @Override
    public void calculateInterest() {
        interest = balance * 0.01;
    }
}

public class Main {

    public static void main(String[] args) {

        SavingAccount savingAccount = new SavingAccount(1000.0);
        savingAccount.calculateInterest();
        savingAccount.addInterest();
        savingAccount.displayBalance();

        CurrentAccount currentAccount = new CurrentAccount(1000.0);
        currentAccount.calculateInterest();
        currentAccount.addInterest();
        currentAccount.displayBalance();
    }

}