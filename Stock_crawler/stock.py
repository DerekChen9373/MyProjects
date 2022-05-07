import investpy
import matplotlib.pyplot as plt
def main():
    print("Welcome!")
    country = str(input("Which stock market are you in?\n(Insert country name with the first letter of each word capitalized): "))
    stock=str(input("Which stock are you looking for?\n(Insert code or abbreviation eg:2330 for TSMC, AAPL for apple): "))
    date1 = str(input("Enter starting date(In a dd/mm/yyyy format): "))
    date2 = str(input("Enter the ending date(In a dd/mm/yyyy format): "))
    print("Have a nice day!")
    df = investpy.get_stock_historical_data(stock=stock,country=country,from_date=date1,to_date=date2)
    data = df.reset_index()
    plt.title("Stock: "+stock+"         From "+date1+" to "+date2)
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.xticks(rotation=45)
    plt.plot("Date", "Open", data=data, color='red')
    plt.plot("Date", "Close", data=data, color='green')
    plt.legend(loc='upper right')
    plt.show()
if __name__ == '__main__':
    main()


