import os
import importlib.util


def load_module_from_path(path):
    spec = importlib.util.spec_from_file_location('proj_module', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_chat_with_gpt_strips(monkeypatch, tmp_path):
    root = os.path.dirname(os.path.dirname(__file__))
    path = os.path.join(root, 'Code of project.py')
    module = load_module_from_path(path)

    def fake_create(model, messages):
        return {'choices': [{'message': {'content': '  hello world  '}}]}

    # Replace ChatCompletion on the module's openai with a simple object that has create()
    class FakeChatCompletion:
        @staticmethod
        def create(model, messages):
            return fake_create(model, messages)

    monkeypatch.setattr(module.openai, 'ChatCompletion', FakeChatCompletion, raising=False)

    result = module.chat_with_gpt('hi')
    assert result == 'hello world'
