# lambdata-tyler9937
##What is it?

lambdata_tyler9937 is a Python package that does its best to provide random but usfull functions all designed 
to demonstrate the power of Python packages. Please feel free to explore the rest of this README file so 
that you may become fully aware of what the lambdata_tyler9937 Python package has brought to the world.

##Main Features
Listed below are the main functions included in this package and a little about what each of them do

	- list_to_df(list, df), a function that takes on the challenge of converting a list of lists 
		and converting them into a pandas series. please note this function originally did other
		stuff but we found it must useful if we could call it to just get a pandas series back.

	- null_check(df), a function that runs the .isnull() method on a given dataframe. Extremly usful 
		if you need a printed out list of Boolean values based off of the original value being null or not

	- plot_confustion_matrix(true, predicted), do you have have predicted data and pre analyised actule data? 
		well then this function might be the function for you. It plot a confustion matrix given true and
		predicted data inputs.

	- train_split_test(data, target), a function that splits a main data souce into train, val, and test data
		for predictive modeling purposes. It is a useful function. However, its flexibility is rather limited.

	- generate_more_data(df, random_amount=3), a function that takes in a dataframe and automaticly generates
		and adds a new column of random numbers to your pre existing dataframe. it can add as many columns 
		as needed.

##Where to get it
it is currently hosted on GitHub at: https://github.com/Tyler9937/lambdata

It can be istalled via pip 

pip install -i https://test.pypi.org/simple/ lambdata-tyler9937==0.1.2


##Dependencies

	-NumPy
	-Pandas

##License
MIT license - https://opensource.org/licenses/MIT