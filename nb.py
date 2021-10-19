{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "92f07395",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import seaborn as sp\n",
    "import matplotlib.pyplot as mlp"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "809d0714",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_csv(\"heart.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "e790c270",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>age</th>\n",
       "      <th>sex</th>\n",
       "      <th>cp</th>\n",
       "      <th>trestbps</th>\n",
       "      <th>chol</th>\n",
       "      <th>fbs</th>\n",
       "      <th>restecg</th>\n",
       "      <th>thalach</th>\n",
       "      <th>exang</th>\n",
       "      <th>oldpeak</th>\n",
       "      <th>slope</th>\n",
       "      <th>ca</th>\n",
       "      <th>thal</th>\n",
       "      <th>target</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>298</th>\n",
       "      <td>57</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>140</td>\n",
       "      <td>241</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>123</td>\n",
       "      <td>1</td>\n",
       "      <td>0.2</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>299</th>\n",
       "      <td>45</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>110</td>\n",
       "      <td>264</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>132</td>\n",
       "      <td>0</td>\n",
       "      <td>1.2</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>300</th>\n",
       "      <td>68</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>144</td>\n",
       "      <td>193</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>141</td>\n",
       "      <td>0</td>\n",
       "      <td>3.4</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>301</th>\n",
       "      <td>57</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>130</td>\n",
       "      <td>131</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>115</td>\n",
       "      <td>1</td>\n",
       "      <td>1.2</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>302</th>\n",
       "      <td>57</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>130</td>\n",
       "      <td>236</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>174</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     age  sex  cp  trestbps  chol  fbs  restecg  thalach  exang  oldpeak  \\\n",
       "298   57    0   0       140   241    0        1      123      1      0.2   \n",
       "299   45    1   3       110   264    0        1      132      0      1.2   \n",
       "300   68    1   0       144   193    1        1      141      0      3.4   \n",
       "301   57    1   0       130   131    0        1      115      1      1.2   \n",
       "302   57    0   1       130   236    0        0      174      0      0.0   \n",
       "\n",
       "     slope  ca  thal  target  \n",
       "298      1   0     3       0  \n",
       "299      1   0     3       0  \n",
       "300      1   2     3       0  \n",
       "301      1   1     3       0  \n",
       "302      1   1     2       0  "
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()\n",
    "df.tail()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "740a7f33",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "age         0\n",
       "sex         0\n",
       "cp          0\n",
       "trestbps    0\n",
       "chol        0\n",
       "fbs         0\n",
       "restecg     0\n",
       "thalach     0\n",
       "exang       0\n",
       "oldpeak     0\n",
       "slope       0\n",
       "ca          0\n",
       "thal        0\n",
       "target      0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "b39da3c2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[29,\n",
       " 34,\n",
       " 35,\n",
       " 37,\n",
       " 38,\n",
       " 39,\n",
       " 40,\n",
       " 41,\n",
       " 42,\n",
       " 43,\n",
       " 44,\n",
       " 45,\n",
       " 46,\n",
       " 47,\n",
       " 48,\n",
       " 49,\n",
       " 50,\n",
       " 51,\n",
       " 52,\n",
       " 53,\n",
       " 54,\n",
       " 55,\n",
       " 56,\n",
       " 57,\n",
       " 58,\n",
       " 59,\n",
       " 60,\n",
       " 61,\n",
       " 62,\n",
       " 63,\n",
       " 64,\n",
       " 65,\n",
       " 66,\n",
       " 67,\n",
       " 68,\n",
       " 69,\n",
       " 70,\n",
       " 71,\n",
       " 74,\n",
       " 76,\n",
       " 77]"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sorted(df.age.unique())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "582d1153",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "58    19\n",
       "57    17\n",
       "54    16\n",
       "59    14\n",
       "52    13\n",
       "51    12\n",
       "62    11\n",
       "60    11\n",
       "44    11\n",
       "56    11\n",
       "41    10\n",
       "64    10\n",
       "63     9\n",
       "67     9\n",
       "65     8\n",
       "55     8\n",
       "61     8\n",
       "53     8\n",
       "45     8\n",
       "43     8\n",
       "42     8\n",
       "50     7\n",
       "66     7\n",
       "48     7\n",
       "46     7\n",
       "49     5\n",
       "47     5\n",
       "70     4\n",
       "39     4\n",
       "68     4\n",
       "35     4\n",
       "69     3\n",
       "40     3\n",
       "38     3\n",
       "71     3\n",
       "37     2\n",
       "34     2\n",
       "76     1\n",
       "29     1\n",
       "74     1\n",
       "77     1\n",
       "Name: age, dtype: int64"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.age.value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "ee3e4b1d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 303 entries, 0 to 302\n",
      "Data columns (total 14 columns):\n",
      " #   Column    Non-Null Count  Dtype  \n",
      "---  ------    --------------  -----  \n",
      " 0   age       303 non-null    int64  \n",
      " 1   sex       303 non-null    int64  \n",
      " 2   cp        303 non-null    int64  \n",
      " 3   trestbps  303 non-null    int64  \n",
      " 4   chol      303 non-null    int64  \n",
      " 5   fbs       303 non-null    int64  \n",
      " 6   restecg   303 non-null    int64  \n",
      " 7   thalach   303 non-null    int64  \n",
      " 8   exang     303 non-null    int64  \n",
      " 9   oldpeak   303 non-null    float64\n",
      " 10  slope     303 non-null    int64  \n",
      " 11  ca        303 non-null    int64  \n",
      " 12  thal      303 non-null    int64  \n",
      " 13  target    303 non-null    int64  \n",
      "dtypes: float64(1), int64(13)\n",
      "memory usage: 33.3 KB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "94bd681a",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.columns = ['age', 'gender', 'chest_pain_type', 'resting_blood_pressure', 'cholestrol', 'fasting_blood_sugar', 'rest_ecg', 'max_heart_rate_achieved', 'exercise_induced_angina', 'st_depression', 'st_slope', 'num_major_vessels', 'thalassemia', 'target']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "aa66095b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 303 entries, 0 to 302\n",
      "Data columns (total 14 columns):\n",
      " #   Column                   Non-Null Count  Dtype  \n",
      "---  ------                   --------------  -----  \n",
      " 0   age                      303 non-null    int64  \n",
      " 1   gender                   303 non-null    int64  \n",
      " 2   chest_pain_type          303 non-null    int64  \n",
      " 3   resting_blood_pressure   303 non-null    int64  \n",
      " 4   cholestrol               303 non-null    int64  \n",
      " 5   fasting_blood_sugar      303 non-null    int64  \n",
      " 6   rest_ecg                 303 non-null    int64  \n",
      " 7   max_heart_rate_achieved  303 non-null    int64  \n",
      " 8   exercise_induced_angina  303 non-null    int64  \n",
      " 9   st_depression            303 non-null    float64\n",
      " 10  st_slope                 303 non-null    int64  \n",
      " 11  num_major_vessels        303 non-null    int64  \n",
      " 12  thalassemia              303 non-null    int64  \n",
      " 13  target                   303 non-null    int64  \n",
      "dtypes: float64(1), int64(13)\n",
      "memory usage: 33.3 KB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "d41f33c9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    143\n",
       "2     87\n",
       "1     50\n",
       "3     23\n",
       "Name: chest_pain_type, dtype: int64"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.chest_pain_type.value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "ee678a24",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    258\n",
       "1     45\n",
       "Name: fasting_blood_sugar, dtype: int64"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.fasting_blood_sugar.value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "49a89ea5",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
