// Private attributes
private String id;
private int mileage;
private int mpg;
private double cost;
private double salesPrice;
private boolean sold;
private double priceSold;
private double profit;



// Constructors



// Default Constructor
public Car()
{
id = "";
mileage = 0;
mpg = 0;
cost = 0.0;
salesPrice = 0.0;
sold = false;
priceSold = 0.0;
profit = 0.0;
}

//constructor to set all variables in class
Car(String id, int mileage, int mpg, double cost, double salesPrice)
{
this.id = id;
this.mileage = mileage;
this.mpg = mpg;
this.cost = cost;
this.salesPrice = salesPrice;
}

//getter for id
public String getID()
{
return id;
}

//setter for id
public void setID(String id)
{
this.id = id;
}

//getter for mileage
public int getMileage()
{
return mileage;
}

//setter for mileage
public void setMileage(int mileage)
{
this.mileage = mileage;
}

//getter for mpg
public int getMpg()
{
return mpg;
}

//setter for mpg
public void setMpg(int mpg)
{
this.mpg = mpg;
}

//getter for cost
public double getCost()
{
return cost;
}

//setter for cost
public void setCost(double cost)
{
this.cost = cost;
}

//getter for salesPrice
public double getSalesPrice()
{
return salesPrice;
}

//setter for salesPrice
public void setSalesPrice(double salesPrice)
{
this.salesPrice = salesPrice;
}

//getter for is sold
public boolean isSold()
{
return sold;
}

//setter for issold
public void setSold(boolean sold)
{
this.sold = sold;
}

//getter for profit
public double getProfit()
{
return profit;
}

//setter for profit
public void setProfit(double profit)
{
this.profit = profit;
}


//mark as sold and get profit
public void sellCar(double priceSold)
{
setSold(true);
setPriceSold(priceSold);
setProfit(priceSold-getCost());
}

// toString method
public String toString(){
String str = "Car: "+ ID +", Mileage: "+getMileage()+", MPG: "+getMpg()+", Sold: "+((isSold())?"Yes":"No")
+", Cost: $"+getCost()+", Selling price: $"+getSalesPrice();
if(isSold())
{
str = str + ", Sold For: $"+getPriceSold()+". Profit: $"+getProfit();
}
return str;
}

//getter for price sold
public double getPriceSold() {
return priceSold;
}

//setter for pricesold
public void setPriceSold(double priceSold) {
this.priceSold = priceSold;
}

//compare mpg method
public int compareMPG(Car otherCar)
{
return mpg - otherCar.getMpg();
}

//compare miles method
public int compareMiles(Car otherCar)
{
return mileage - otherCar.getMileage();
}

//compare price method
public int comparePrice(Car otherCar)
{
return (int) (salesPrice - otherCar.getSalesPrice());
}
}
