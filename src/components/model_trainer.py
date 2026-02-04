import os 
import sys 
from dataclasses import dataclass 

from src.logger import logging 
from src.exception import CustomException
from src.utils import save_object

from sklearn.model_selection import RandomizedSearchCV
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
            
            models_config = {
                "LinearRegression" : {
                    'model' : LinearRegression() , 
                    'params' : {}
                } ,
                
                "KNeighborsRegressor" : {
                    'model' : KNeighborsRegressor() , 
                    'params' : {
                        'n_neighbors' : list(range(1,31)) ,
                        'weights' : ['uniform' , 'distance'] ,
                        'metric' : ['euclidean' , 'manhattan' , 'minkowski']
                    } , 
                } ,
                
                "DecisionTreeRegressor" : {
                    'model' : DecisionTreeRegressor() , 
                    'params' : {
                        'criterion' : ['squared_error' , 'friedman_mse'] ,
                        'splitter' : ['best'] ,
                        'max_depth' : [2,3,4,5,6,8,10,None] ,
                        'min_samples_split' : [2,5,10,20,30] ,
                        'min_samples_leaf' : [1,2,5,10] ,
                        'max_features' : [None , 'sqrt' , 'log2']
                    } 
                } , 
                
                "AdaBoostRegressor" : {
                    'model' : AdaBoostRegressor() , 
                    'params' : {
                        'n_estimators': [50, 100, 200, 300],
                        'learning_rate': [0.01, 0.05, 0.1, 0.5, 1.0],
                        'loss': ['linear', 'square', 'exponential']
                    }
                } , 
                
                "GradientBoostingRegressor" : {
                    'model' : GradientBoostingRegressor() , 
                    'params' : {
                        'n_estimators' : [100 , 200] , 
                        'learning_rate' : [0.01 , 0.1] , 
                        'max_depth' : [3 , 5]
                    }
                } , 
                
                "RandomForestRegressor" : {
                    'model' : RandomForestRegressor() , 
                    'params' : {
                        'n_estimators' : [100 , 200 , 500] , 
                        'max_depth' : [None , 10 , 20 , 30] , 
                        'min_samples_split' : [2 , 5 , 10]
                    }
                } ,
                
                "XGBRegressor" : {
                    'model' : XGBRegressor(objective = "reg:squarederror" , random_state = 42) ,  
                    'params' : {
                        'n_estimators' : [200 , 400] , 
                        'learning_rate' : [0.05 , 0.1] , 
                        'max_depth' : [3 , 6]
                    }
                } , 
                
                "CatBoostRegressor" : {
                    'model' : CatBoostRegressor(verbose = False) , 
                    'params' : {
                        'depth' : [4 , 6 , 8] , 
                        'learning_rate' : [0.03 , 0.1] , 
                        'iterations' : [300 , 500]
                    }
                } 
            }    
            
            best_model_name = None #Model name Ex: 'LinearRegression'
            best_model = None  # Trained model object LinearRegression()
            best_model_score = -float("inf") # This accepts the fist model as 'best so far'
            
            for model_name , config in models_config.items():
                logging.info(f"Training & Tuning {model_name}")
                
                #Extracting model and params
                model =  config['model'] 
                params = config['params'] 
                
                if params:
                    search = RandomizedSearchCV(
                        estimator = model , 
                        param_distributions = params , 
                        n_iter = 10 , 
                        cv = 5 , 
                        scoring = 'r2' , 
                        n_jobs = -1 , 
                        random_state = 42
                    )
                    
                    search.fit(X_train , y_train)
                    candidate_model = search.best_estimator_
                    score = search.best_score_ 
                    
                else:
                    #Models without hyperparameter (LinearRegression)
                    model.fit(X_train , y_train) 
                    score = r2_score(y_test , model.predict(X_test))
                    candidate_model = model     
                    
                    logging.info(f"{model_name} score: {score}")
                    
                    if score > best_model_score:
                        best_model_score = score 
                        best_model = candidate_model 
                        best_model_name = model_name 
                        
            if best_model_score < 0.6:
                raise CustomException("No suitable model found", sys)
            
            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

            logging.info(f"Best model: {best_model_name} | R2: {best_model_score}")

            return best_model_name, best_model_score

        except Exception as e:
            raise CustomException(e, sys)            
                        
                
            
             
               
               
                   
            