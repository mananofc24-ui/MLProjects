import os 
import sys 
from dataclasses import dataclass 

from src.logger import logging 
from src.exception import CustomException
from src.utils import save_object


from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor

from sklearn.ensemble import (
    AdaBoostRegressor , 
    GradientBoostingRegressor , 
    RandomForestRegressor
)

from catboost import CatBoostRegressor
from xgboost import XGBRegressor

@dataclass 
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('artifacts' , 'model.pkl')
    
class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()    
        
    def initiate_model_trainer(self , train_array , test_array):
        try:
            logging.info('Split training and test input data')
            
            X_train , y_train , X_test , y_test = (
                train_array[:,:-1] , #All rows and all columns except the last one (target feature)
                train_array[:,-1] , #All rows and only last column (target feature)
                test_array[:,:-1] , #All rows and all columns except the last one (target feature)
                test_array[:,-1] #All rows and only last column (target feature)
            )
            
            models = {
                'LinearRegression' : LinearRegression() , 
                'KNeighborsRegressor' : KNeighborsRegressor() ,
                'DecisionTreeRegressor' : DecisionTreeRegressor() , 
                'AdaBoostRegressor' :  AdaBoostRegressor() , 
                'GradientBoostingRegressor' :  GradientBoostingRegressor() , 
                'RandomForestRegressor' :  RandomForestRegressor() , 
                'CatBoostRegressor' : CatBoostRegressor(verbose = False) , 
                'XGBRegressor' : XGBRegressor()
            }
            
            best_model_name = None #Model name
            best_model = None # Trained model object
            best_model_score = -float("inf") # This accepts the fist model as 'best so far'
           
            for name , model in models.items():
               model.fit(X_train , y_train) 
               
               y_test_pred = model.predict(X_test)
               score = r2_score(y_test , y_test_pred) 
               
               logging.info(f"{name} R2 score : {score}")
               
               if score > best_model_score:
                   best_model_score = score # best_model_score = 0.88
                   best_model_name = name #best_model_name = "LinearRegression"
                   best_model = model #best_model = LinearRegression()
                   
            if best_model_score < 0.6:
                raise CustomException('No suitable model found' , sys) 
            
            logging.info(f"Best Model : {best_model_name} | R2 : {best_model_score}") 
            
            save_object(
                file_path = self.model_trainer_config.trained_model_file_path , 
                obj = best_model 
            
            )      
            
            return best_model_name , best_model_score 
           
        except Exception as e:
            raise CustomException(e , sys)    