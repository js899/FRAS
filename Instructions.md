# Instructions to execute :
  1. Install all the [required packages](https://github.com/ritesh-nitjsr/FRAS/blob/master/requirements.txt)
  2. Add images to the folder ./Image_data/&lt;branch&gt;/&lt;semester&gt;
      * &lt;branch&gt; is one of the strings : CS,EE,EC,CE,MM,ME
      * &lt;semester&gt; is one the following strings : I,II,III,IV,V,VI,VII,VIII
      * The name of images must be according to the convention :  &lt;Year of admission&gt;&lt;Course Type&gt;&lt;Branch&gt;&lt;Roll Number&gt; &lt;index&gt;
        - E.g : 2015UGCS001 1.jpg , 2015UGCS012 1.jpg , 2015UGCS012 2.jpg
        - This naming convention is the one followed by my college. If you need, you can make changes as per other naming convenstions.
  3. Run main.py ```python main.py```
      * Execute the 2nd option ```2. Add into students database```. Add the number of student in the class. Return back to main menu.
      * Execute the 4th option ```4. Convert images to pickle```. Return back to main menu.
      * Execute the 1st option ```1. Take Attendance```. Return back to main menu.
      * Execute the 3rd option ```3. View current attendance```. This would genrate a csv file of the current attendance of any month of any year. Return back to main menu.
