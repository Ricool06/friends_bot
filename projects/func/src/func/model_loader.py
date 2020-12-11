from transformers import pipeline
from transformers.pipelines import TextGenerationPipeline


def load_friends_model(
        path: str = 'resources/') -> TextGenerationPipeline:
    model = pipeline('text-generation', model=path)
    return model
