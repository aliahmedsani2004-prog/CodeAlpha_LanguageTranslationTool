from deep_translator import MyMemoryTranslator

result = MyMemoryTranslator(source="english", target="spanish").translate("How are you?")
print(result)