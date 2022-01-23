# Bank Note Authentication

Bank Note Authenticator is a Streamlit web application that detects whether banknotes are authentic or not based on certain parameters such as wavelet variance, wavelet skewness, wavelet kurtosis, and image entropy which are extracted from the images. The code is written in Python 3.8.10.

According to research, for variance values ​​between -3.3203 and -0.4080 and having elt asymmetry; = 0.7201, the model includes an additional entropy predictor, which detects that around 95% of banknotes are fake if their entropy values ​​are less than or equal to 0.2077, while for higher entropy values at -0.2077 they have 100% note detection. Moreover, for variance between –0.4080 and 0.4957 and a kurtosis less than –0.1965, 71% of counterfeit notes can be predicted and for a Kurtosis value greater than –0.1965, it is possible to detect 75% of authentic banknotes. Similarly, other decision conditions are taken as a function of independent variables chosen in the model which make it possible to distinguish the counterfeit note from the real notes.

## Machine Learning Model
Implemented Random Forest Classifier and the Support Vector Machine, with the Random Forest achieving 99.6% accuracy. As a result, we have included it in our deployed model classifier.
## Application Link

End-to-end implementation and deployment of Machine Learning Bank Notes Authenticator web application has been created on AWS EC2 Instance and can be accessed from [ec2-3-131-133-134.us-east-2.compute.amazonaws.com](http://3.131.133.134:8501/)




## Usage
First, clone the repository in your local system then perform certain commands in the command prompt given below in the project directory.

```bash
pip install -r Requirements.txt
```
```bash
streamlit run streamlit_app.py
```



## Contributing
Pull requests are welcome. 
If you have any questions, open an issue.
