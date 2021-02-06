## don't forget to install - pip install translate
from translate import Translator
translator= Translator(to_lang="hi")
translation = translator.translate("Good Morning!")
print(translation)
