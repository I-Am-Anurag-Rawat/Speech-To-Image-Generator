import os
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation
import warnings
import uuid

class ImageGenerator:
    def __init__(self):
        # Set your Stability API key here
        self.api_key = "Replace with your actual stability.ai api_key"  # Replace with your actual key
        self.stability_api = client.StabilityInference(
            key=self.api_key,
            verbose=True
        )
        self.output_dir = "generated_images"
        os.makedirs(self.output_dir, exist_ok=True)

    def generate_image(self, prompt):
        try:
            # Generate image
            response = self.stability_api.generate(
                prompt=prompt,
                steps=30,
                cfg_scale=8.0,
                width=512,
                height=512,
                samples=1
            )
            
            # Process response
            for resp in response:
                for artifact in resp.artifacts:
                    if artifact.type == generation.ARTIFACT_IMAGE:
                        img_path = os.path.join(self.output_dir, f"image_{uuid.uuid4()}.png")
                        with open(img_path, "wb") as f:
                            f.write(artifact.binary)
                        return img_path
                    elif artifact.finish_reason == generation.FILTER:
                        warnings.warn("Image generation was filtered due to content policy.")
                        return None
            return None
        except Exception as e:
            print(f"Image generation error: {str(e)}")
            return None