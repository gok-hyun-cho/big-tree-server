
import importlib.util
import sys

# 정확한 경로 지정
module_path = '/mnt/c/robot_project/ai_models/fire_ai_model.py'  # ← 이 경로 사용!

spec = importlib.util.spec_from_file_location("fire_ai_model", module_path)
fire_ai_model = importlib.util.module_from_spec(spec)
sys.modules["fire_ai_model"] = fire_ai_model
spec.loader.exec_module(fire_ai_model)

# 모델 생성 및 저장
model = fire_ai_model.create_model(input_shape=4)
model.save('input_data/trained_models/fire_model.h5')
