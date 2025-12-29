from mlproject.config.configuration import ConfigurationManager
from mlproject.components.model_training import ModelTrainer
from mlproject import logger


STAGE_NAME = "Model Training stage"
class ModelTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()